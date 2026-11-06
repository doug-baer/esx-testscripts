#!/bin/sh

# Legitimate Admin Use: Decommissioning a KMS/key provider setup or reconfiguring 
#    vSphere Native Key Provider settings during host reconfiguration.
# Malicious Use: Disables or downgrades host-level encryption enforcement, potentially 
#    loosening cryptographic controls on VM cores and sensitive host secrets.
esxcli system settings encryption set --mode=none