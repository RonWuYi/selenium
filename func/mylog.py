from datetime import datetime
import logging.config


def config_basic():
    logging.basicConfig(
        filename='log/app_{}.log'.format(str(datetime.today())[:19]),
        level=logging.WARNING,
        format='%(levelname)s:%(asctime)s:%(message)s')


def config_file():
    logging.config.fileConfig('/home/hdc/PycharmProjects/selenium/logconfig.ini')

# print()

