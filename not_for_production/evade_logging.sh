#!/bin/sh

# Legitimate Admin Use: Reconfiguring or migrating central SIEM/syslog targets 
#    during network infrastructure changes.
# Malicious Use: Clears the remote log aggregator IP, preventing security logs 
#    and audit events from being shipped off-box to an external SOC or SIEM.
esxcli system syslog config set --loghost="" && esxcli system syslog reload