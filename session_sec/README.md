## Setup
- Must add new hosts in order to attack a simluated enterprise;

```shell
  TARGET_IP=ENTER SPAWNED TARGET IP HERE
  printf "%s\t%s\n\n" "$TARGET_IP" "xss.htb.net csrf.htb.net oredirect.htb.net minilab.htb.net" | sudo tee -a /etc/hosts
```
