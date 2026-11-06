#!/bin/sh

# Legitimate Admin Use: Allowing the installation of third-party hardware drivers 
#    (e.g., some NICs or unsupported storage controllers) in homelabs or custom builds.
# Malicious Use: Lowers the host's integrity boundary to allow the installation of unsigned, 
#    untrusted VIB packages (such as kernel-level persistence mechanisms or hypervisor rootkits).
esxcli software acceptance set --level=CommunitySupported