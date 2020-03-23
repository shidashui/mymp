import requests

AppId="wx4ed9c279fda6e3de"
AppSecret="ec6de8ebf2c5fa06daedcfb6e97d1e81"
code2Session="https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code"

def login(code):
    url = code2Session.format(AppId, AppSecret, code)
    response = requests.get(url=url)
    data = response.json()
    if data.get("session_key"):
        return data
    else:
        return False

if __name__ == '__main__':
    a = login("0236JJrO19QhL71fE3tO18pOrO16JJrL")
    print(a)