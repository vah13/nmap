import requests

report_file = r"C:\Users\vava\Desktop\research\att\search_services\nohup.out"
matches = "@vah_13 status code: 302"
_scan_content = ""
scan_path = "/services/"
_except = "sbcglobal"


def get_domain_from_scan(str):
    if " " in str and "(" in str:
        str = str.split(" ")[0]
    return str


def get_content_from_uri(uri):
    _content = requests.get(uri, verify=False, allow_redirects=True).content
    if _scan_content in _content:
        return "OK"


with open(report_file, 'r') as f:
    lines = f.readlines()

i = 0
for line in lines:
    i += 1
    if matches in line:
        domain = get_domain_from_scan(lines[i - 7].strip())
        if _except not in domain:
            URI =  "https://" + domain + scan_path
            print "[*] Start scan {0}".format(URI)
            print get_content_from_uri(URI)
