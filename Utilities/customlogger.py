import inspect
import logging
import allure


def customlogger():
    logName = inspect.stack()[1][3]
    logger = logging.getLogger(logName)
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("../Reports/log.log", mode='w')
    fileHandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger


def allurelogs(text):
    with allure.step(text):
        pass