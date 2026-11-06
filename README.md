# esx-testscripts
Scripts used during HyperArmor Demos and POCs

Initial idea consists of 2 types of scripts: Python and Shell

Each type consists of 3 use cases:
1. admin - this script will be permitted by security policy allowlist (and should be compared against its hash)
2. evil - this script should not be permitted to run (should be denied via implicit "no" guardrail)
3. sneaky - this script will execute different payloads based on the name of the script

October 2026