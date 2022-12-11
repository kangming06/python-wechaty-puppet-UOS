logger = logging.getLogger('itchat')
def test_connect(retryTime=5):
    for i in range(retryTime):
        try:
            r = requests.get(config.BASE_URL)
            return True
        except:
            logger.warning(f"连接微信服务器失败，尝试重连{i+1}/{retryTime}")
    logger.error(traceback.format_exc())
    return False