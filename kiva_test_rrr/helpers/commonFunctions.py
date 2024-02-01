import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] > %(message)s')
logger = logging.getLogger(__name__)

def log(app,method,level,message):
    # 1-debug, 2-info, 3,warning, 4-error, 5-critical
    if(level == 1):
        logger.debug(f'[{app}][{method}] {message}')
    
    if(level == 2):
        logger.info(f'[{app}][{method}] {message}')
    
    if(level == 3):
        logger.warning(f'[{app}][{method}] {message}')
    
    if(level == 4):
        logger.error(f'[{app}][{method}] {message}')

    if(level == 5):
        logger.critical(f'[{app}][{method}] {message}')




