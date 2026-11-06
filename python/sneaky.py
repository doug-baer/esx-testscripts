#!/usr/bin/env python
import os
import sys

script_name = os.path.basename(sys.argv[0])

if "admin" in script_name:
    print("==> Approved administrative script ran")
elif "evil" in script_name:
    print("==> All your files are belong to us $$$$")
else:
    print(f"==> Unrecognized script name: {script_name}")