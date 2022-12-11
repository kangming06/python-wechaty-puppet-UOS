import aiohttp
from wechaty_puppet import Puppet, PuppetOptions

from wechaty_puppet_uos.config import USER_AGENT


class PuppetUOS(Puppet):
    def __init__(self, options: PuppetOptions, name: str = 'puppet_UOS'):
        super().__init__(options, name)
        self.alive=False
        self.session=aiohttp.ClientSession(headers=USER_AGENT)
        self.uuid=None
    from login import login
