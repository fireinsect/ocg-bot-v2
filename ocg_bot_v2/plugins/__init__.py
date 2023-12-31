import json
import os.path
from nonebot import  logger, get_driver


from ocg_bot_v2.libraries.forbideGet import forbiddenGet
from ocg_bot_v2.libraries.globalMessage import json_path, static_path
from ocg_bot_v2.libraries.image import *

from ocg_bot_v2.libraries.staticvar import nick_name_0, nick_name_1, forbidden, daily_card


async def nickNameInit():
    nick_path = json_path + "nickname.json"
    try:
        # 尝试读取
        with open(nick_path, 'r', encoding='utf-8') as f:
            nick_json = json.loads(f.read())['RECORDS']
            logger.info(f'nickname.json 读取成功')
            for js in nick_json:
                if js['NK_type'] == 0:
                    nick_name_0.append(js)
                if js['NK_type'] == 1:
                    nick_name_1.append(js)
    except Exception as e:
        # 读取失败
        logger.warning(f'nickname.json 读取失败')


async def forbideInit():
    forbide_path = json_path + "forbidden.json"
    try:
        # 尝试读取
        with open(forbide_path, 'r', encoding='utf-8') as f:
            forbidden_json = json.loads(f.read())
            logger.info(f'forbidden.json 读取成功')
            for js in forbidden_json:
                forbidden.append(js)
    except Exception as e:
        # 读取失败
        logger.warning(f'forbidden.json 读取失败,正在获取禁卡表')
        forbiddenGet()

async def dailyInit():
    nick_path = json_path + "daily_card.json"
    try:
        # 尝试读取
        with open(nick_path, 'r', encoding='utf-8') as f:
            daily_json = json.loads(f.read())
            logger.info(f'daily_card.json 读取成功')
            for daily in daily_json:
                daily_card.append(daily)
    except Exception as e:
        # 读取失败
        logger.warning(f'daily_card.json 读取失败')


async def init():
    logger.info("开始初始化")
    if not os.path.exists(static_path+"pics"):
        logger.info("未发现图片文件夹，已经创建")
        os.mkdir(static_path+"pics")
    await nickNameInit()
    await forbideInit()
    await dailyInit()

driver = get_driver()
driver.on_startup(init)
