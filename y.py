import requests

url = 'http://202.204.122.1/checkLogin.jsp'
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) AppleWebKit/604.5.6 (KHTML, like Gecko)",
    "Accept-Encoding": "gzip, deflate"
}
params = {
    "username": "171002312", # input yours
    "password": "fangzidong", # input yours
    "ip": "172.23.101.150",
    "action": "connect"
}


sess = requests.Session()
r = sess.post(url, headers=header, data=params)
if (r.status_code == 200):
    print("success")
    print(r.headers)