# esx-testscripts
Scripts used during HyperArmor Demos and POCs

Note that these are very basic scripts to test the command blocking capabilities of console-based security tools on VMware ESX hosts. 

The initial idea consists of 2 types of scripts: Python and Shell

Each type consists of 3 use cases:
1. admin - this script will be permitted by security policy allowlist (and should be compared against its hash)
2. evil - this script should not be permitted to run (should be denied via implicit "no" guardrail)
3. sneaky - this script will execute different payloads based on the name of the script

Note that while the above scripts do not attempt to perform any reconfiguration or potentially destructive actions, the  scripts within the not_for_production directory attempt to perform actions similar to those of a bad actor.  Most of these are shell scripts.

DO NOT RUN IN PRODUCTION ENVIRONMENTS! 

not_for_production:
1. alter_vib_acceptance - change VIB acceptance level to CommunitySupported
2. disable_encryption - disable encryption
3. disable_firewall - disable ESX host firewall
4. evade_logging - disable syslog target and reload logger
5. drop_vm_by_id - kill VM process given the worldID of the running VM
6. drop-vm_by-name - kill VM process given the name of the running VM

October 2026