# 0x13-firewall


1. Uncomment forwarding line in /etc/ufw/sysctl.conf
2. Update `/etc/default/ufw` set the line: `DEFAULT_FORWARD_POLICY="ACCEPT"`
3. Added the following lines to `/etc/ufw/before.rules` (before the `*filter` section):
```
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
```
