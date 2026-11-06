#!/usr/bin/env python
import subprocess
import sys


def kill_vm_by_id(world_id):
  print(f"==> Executing forced process kill for World ID: {world_id}")

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
    print("==> Process termination command sent.")
  except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}", file=sys.stderr)
    sys.exit(e.returncode)


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <WORLD_ID>")
    sys.exit(1)

  kill_vm_by_id(sys.argv[1])