#!/bin/sh
script_name=$(basename "$0")

case "$script_name" in
    *admin*)
        echo "==> Approved administrative script ran"
        ;;
    *evil*)
        echo "==> All your files are belong to us $$$$"
        ;;
    *)
        echo "==> Unrecognized script name: $script_name"
        ;;
esac