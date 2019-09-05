report_file = r"C:\Users\vava\Desktop\research\att\search_services\nohup.out"
matches = "@vah_13 status code: 302"
scan_path = "/services/"
_except = "sbcglobal"


def get_domain_from_scan(str):
    if " " in str and "(" in str:
        str = str.split(" ")[0]
    return str


with open(report_file, 'r') as f:
    lines = f.readlines()

i = 0
for line in lines:
    i += 1
    if matches in line:
        domain = get_domain_from_scan(lines[i - 7].strip())
        if _except not in domain:
            print "https://" + domain + scan_path
