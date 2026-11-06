#!/bin/sh

# Ensure a World ID parameter is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <WORLD_ID>"
    exit 1
fi

WORLD_ID="$1"

echo "==> Executing forced process kill for World ID: $WORLD_ID"
esxcli vm process kill --type=force --world-id="$WORLD_ID"