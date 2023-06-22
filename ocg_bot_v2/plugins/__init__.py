import copy
import json
import logging
import os.path

import requests
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Message, Event, Bot, MessageSegment, GroupRequestEvent, GroupMessageEvent
from nonebot import  logger, get_driver
import re

from ocg_bot_v2.libraries.forbideGet import forbiddenGet
from ocg_bot_v2.libraries.image import *
from ocg_bot_v2.libraries.raiseCard import draw_card_text
from ocg_bot_v2.libraries.staticvar import nick_name_0, nick_name_1, forbidden

async def nickNameInit():
    nick_path = static_path + "nickname.json"
    try:
        # 尝试读取
        with open(nick_path, 'r', encoding='utf-8') as f:
            nick_json = json.loads(f.read())['RECORDS']
            for js in nick_json:
                if js['NK_type'] == 0:
                    nick_name_0.append(js)
                if js['NK_type'] == 1:
                    nick_name_1.append(js)
    except Exception as e:
        # 读取失败
        logger.warning(f'nickname.json 读取失败')


async def forbideInit():
    forbide_path = static_path + "forbidden.json"
    try:
        # 尝试读取
        with open(forbide_path, 'r', encoding='utf-8') as f:
            forbidden_json = json.loads(f.read())
            for js in forbidden_json:
                forbidden.append(js)
    except Exception as e:
        # 读取失败
        logger.warning(f'forbidden.json 读取失败,正在获取禁卡表')
        forbiddenGet()


async def init():
    logger.info("开始初始化")
    if not os.path.exists(static_path+"pics"):
        logger.info("未发现图片文件夹，已经创建")
        os.mkdir(static_path+"pics")
    await nickNameInit()
    await forbideInit()

driver = get_driver()
driver.on_startup(init)
