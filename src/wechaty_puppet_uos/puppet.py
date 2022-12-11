from __future__ import annotations

import os
import sys

from wechaty_puppet_uos.utils import test_connect

if os.name == 'nt':
    sys.path.insert(0,f'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/wechaty_puppet_itchat')

sys.path.insert(0,f'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/wechaty_puppet_itchat')

from typing import List
from pyee import AsyncIOEventEmitter  # type: ignore
from wechaty_puppet.schemas.types import PayloadType  # type: ignore
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
log = get_logger('ItChatPuppet')


async def room_list(self) -> List[str]:
    """
    获取所有房间的列表
    """
async def start(self) -> None:
    log.info("正在启动管线...")
    log.info("正在登录...")
    # await log
async def load_status(self):pass
async def login(self):
    if not test_connect():
        log.error("无法连接微信服务器，即将退出")
        #TODO:更优雅的退出
        sys.exit()
