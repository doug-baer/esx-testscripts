#!/usr/bin/env python
import re
import subprocess
import sys


def get_running_vms():
  """Parses 'esxcli vm process list' and returns a mapping of VM name to World ID."""
  try:
    output = subprocess.check_output(
        ["esxcli", "vm", "process", "list"], universal_newlines=True
    )
  except (subprocess.CalledProcessError, FileNotFoundError) as e:
    print(f"Error executing esxcli: {e}", file=sys.stderr)
    sys.exit(1)

  vms = {}
  current_wid = None

  for line in output.splitlines():
    line = line.strip()

    # Capture the World ID
    wid_match = re.match(r"^World ID:\s*(\d+)", line)
    if wid_match:
      current_wid = wid_match.group(1)

    # Capture Display Name and map to the current block's World ID
    name_match = re.match(r"^Display Name:\s*(.+)$", line)
    if name_match and current_wid:
      display_name = name_match.group(1).strip()
      vms[display_name] = current_wid

    # Reset per-record tracker on empty lines
    if not line:
      current_wid = None

  return vms


def kill_vm(vm_name):
  vms = get_running_vms()

  if vm_name not in vms:
    print(f"Error: VM '{vm_name}' not found or not running.", file=sys.stderr)
    if vms:
      print("Currently running VMs on this host:", file=sys.stderr)
      for name in sorted(vms.keys()):
        print(f"  - {name}", file=sys.stderr)
    sys.exit(1)

  world_id = vms[vm_name]
  print(f"==> Target VM: {vm_name}")
  print(f"==> Identified World ID: {world_id}")
  print("==> Executing forced process kill...")

  cmd = [
      "esxcli",
      "vm",
      "process",
      "kill",
      "--type=force",
      f"--world-id={world_id}",
  ]
  try:
    subprocess.check_call(cmd)
    print(f"==> Process for '{vm_name}' (World ID: {world_id}) terminated.")
  except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}", file=sys.stderr)
    sys.exit(e.returncode)


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <VM_NAME>")
    sys.exit(1)

  kill_vm(sys.argv[1])