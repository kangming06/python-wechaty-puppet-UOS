from fake_useragent import UserAgent
ua=UserAgent()
BASE_URL = 'https://login.weixin.qq.com'
def USER_AGENT():
    return ua.random
print(USER_AGENT())
