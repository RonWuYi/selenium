import os
import time
import logging

from func.mylog import config_basic


class Test:
    def __init__(self):
        config_basic()
        logging.error("error happed")

    def main(self):
        pass


if __name__ == '__main__':
    my_test = Test()
