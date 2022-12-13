import pickle

import aiofiles
from wechaty_puppet import get_logger

from wechaty_puppet_uos import PuppetUOS
from wechaty_puppet_uos.config import BASE_URL
from wechaty_puppet_uos.const import VERSION

log = get_logger('UOSPuppet')

async def login(self):
    pass
async def read_login(self,login_file:str):
    try:
        async with aiofiles.open(login_file,"rb") as f:
            j = pickle.loads(await f.read())
    except:
        log.warning("找不到登录缓存")
    if j.get('version','') != VERSION:
        log.warning(f"缓存文件版本不匹配,应为{VERSION},实际为{j.get('version','老版本')}")
async def login(self: PuppetUOS,):
    if self.alive:
        log.warning('已登录，无需重复登陆')
        return
    while True:pass
async def push_login(self: PuppetUOS):
    cookies = self.session.cookie_jar.filter_cookies()
    if 'wxuin' in cookies:
        url = f'{BASE_URL}/cgi-bin/mmwebwx-bin/webwxpushloginurl?uin={cookies["wxuin"].value}'
        async with self.session.get(url) as r:
            r=await r.json()
            if 'uuid' in r and r.get("ret") in (0,'0'):
                self.uuid = r["uuid"]
                return r["uuid"]
    return False
async def push_login(self):
    cookies = self.session.cookie_jar.filter_cookies()
    if 'wxuin' in cookies:
        url = f'{BASE_URL}/cgi-bin/mmwebwx-bin/webwxpushloginurl?uin={cookies["wxuin"]}'
        async with self.session.get(url).json() as r:
            if 'uuid' in r and r.get('ret') in (0, '0'):
                self.uuid = r['uuid']
                return r['uuid']
    return False



