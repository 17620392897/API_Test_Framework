
from nb_log import LogManager


logger = LogManager('newdream').get_logger_and_add_handlers(is_add_stream_handler=True,log_filename='ha.log')
print('hello')
logger.info('你好！')
logger.warning('警告！！')
logger.error('这是错误日志')


