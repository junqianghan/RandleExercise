#!/usr/bin/python
#coding:utf-8

import logging
import sys


def main1():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")

def main():
    logging.basicConfig(filename='app.log',
                        filemode='w',
                        format='%(name)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to a file')


if __name__ == '__main__':
    main()
