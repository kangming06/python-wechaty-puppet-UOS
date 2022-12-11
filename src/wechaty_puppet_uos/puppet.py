from __future__ import annotations
import sys
import os
if os.name == 'nt':
    sys.path.insert(0,f'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/wechaty_puppet_itchat')
    
sys.path.insert(0,f'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/wechaty_puppet_itchat')
    
from itchat  import load_async_itchat
from itchat.content import (
    TEXT,
    MAP,
    CARD,
    NOTE,
    SHARING,
    PICTURE,
    RECORDING,
    VOICE,
    ATTACHMENT,
    VIDEO,
    FRIENDS
)
import asyncio
from distutils import core
import types
from typing import Optional, List, Dict
from pyee import AsyncIOEventEmitter  # type: ignore
from wechaty_puppet.schemas.types import PayloadType  # type: ignore
from wechaty_puppet.schemas.event import EventScanPayload,ScanStatus
from wechaty_puppet import (  # type: ignore
    # EventReadyPayload,
    #
    # EventDongPayload,
    # EventRoomTopicPayload,
    # EventRoomLeavePayload,
    # EventRoomJoinPayload,
    # EventRoomInvitePayload,

    EventMessagePayload,
    EventLogoutPayload,
    EventLoginPayload,
    # EventFriendshipPayload,
    # EventHeartbeatPayload,
    # EventErrorPayload,
    FileBox, RoomMemberPayload, RoomPayload, RoomInvitationPayload,
    RoomQueryFilter, FriendshipPayload, ContactPayload, MessagePayload,
    MessageQueryFilter,

    ImageType,
    # EventType,
    MessageType,
    Puppet,
    PuppetOptions,
    MiniProgramPayload,
    UrlLinkPayload,
    watch_dog,
    get_logger
)

from wechaty_puppet.exceptions import (  # type: ignore
    # WechatyPuppetConfigurationError,
    # WechatyPuppetError,
    WechatyPuppetGrpcError,
    WechatyPuppetOperationError,
    # WechatyPuppetPayloadError
)
class PuppetUOS(Puppet):
    def __init__(self, options: PuppetOptions, name: str = 'puppet_UOS'):
        super().__init__(options,name)
    async def room_list(self) -> List[str]:
        """
        获取所有房间的列表
        """
    async def start(self) -> None:
        log.info("正在启动管线...")
        log.info("正在登录...")
        await lo
    async load_status()
    async def login():
        if not test_connect():
            logger.error("无法连接微信服务器，即将退出")
            #TODO:更优雅的退出
            sys.exit()
        