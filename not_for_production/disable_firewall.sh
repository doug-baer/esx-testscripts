#!/bin/sh

# Legitimate Admin Use: Temporarily troubleshooting network connectivity issues 
#    during installation or maintenance.
# Malicious Use: Disables host-level packet filtering entirely, exposing management 
#    ports, SSH, and internal listening services directly to adjacent networks.
esxcli network firewall set --enabled false