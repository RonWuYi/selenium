import logging
import os
# import pathlib
from pathlib import Path
from datetime import datetime


class Mylog:
    current_path = Path.cwd()

    def __init__(self, hostname, item, filename, mode):

        # pass
        self.current_path = Path.cwd()


    @classmethod
    def main(cls):
        # logging.basicConfig(
        #     filename=os.path.join(current_path, )
        #     filename='app-{}.log'.format(datetime.today()),
        #     level=logging.ERROR,
        #     format='%(levelname)s:%(asctime)s:%(message)s'
        # )
        pass
