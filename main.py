from sensor.exception import SensorException
# from sensor import sensor
import sys
import os
from sensor.logger import logging



def test_exception():
    try:
        logging.info("Starting Test Exception")
        a = 1/0
    except Exception as e:
        raise SensorException(e, sys)
        # raise e







if __name__ == "__main__":

    try:
        test_exception()
    except Exception as e:
        print(e)        