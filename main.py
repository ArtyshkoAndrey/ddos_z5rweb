import logging
import time
import os
from configparser import ConfigParser

from workers import Z5rweb
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    config = ConfigParser()
    config.read(os.path.join(os.getcwd(), 'config.ini'))
    host = config.get('skud', 'host')
    serials = config.get('skud', 'sn').split(',') if config.has_option('skud', 'sn') else list()

    for i in serials:
        logging.debug(f"Serial: {i}")
        th = Z5rweb(link=host, sn=int(i))
        # Что бы в 1 секунду не летели Запросики
        time.sleep(1.71)
        th.start()

    while True:
        time.sleep(10)
        continue
