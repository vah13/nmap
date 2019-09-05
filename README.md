# nmap
nmap  -Pn --script http-methods --script-args http-methods.url-path=/weblogin.htm
Nmap scan report for 12.0.204.41
Host is up (0.060s latency).

PORT    STATE SERVICE
443/tcp open  https
| http-methods:
|   @vah_13 status code: 302
|   Supported Methods: GET
|_  Path tested: /services/
