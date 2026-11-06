#!/bin/sh

if [ -z "$1" ]; then
    echo "Usage: $0 <VM_NAME>"
    exit 1
fi

VM_NAME="$1"

# Parse esxcli output for the World ID associated with the target VM Display Name
WORLD_ID=$(esxcli vm process list | awk -v target="$VM_NAME" '
    BEGIN { wid="" }
    /^[[:space:]]*World ID:/ {
        wid=$3
    }
    /^[[:space:]]*Display Name:/ {
        sub(/^[[:space:]]*Display Name:[[:space:]]*/, "")
        if ($0 == target && wid != "") {
            print wid
            exit
        }
    }
    /^$/ {
        wid=""
    }
')

if [ -z "$WORLD_ID" ]; then
    echo "Error: VM '$VM_NAME' not found or is not currently running."
    exit 1
fi

echo "==> Target VM: $VM_NAME"
echo "==> Identified World ID: $WORLD_ID"
echo "==> Executing forced process kill..."

esxcli vm process kill --type=force --world-id="$WORLD_ID"