#!/usr/bin/python3
"""
logger.py - logger for privacy-protecting IRC stats
author: mutantmonkey <mutantmonkey@mutantmonkey.in>
"""

import os
import datetime
import pdb
def setup(self):
    pass;
def textlogger(phenny, input):
    
    directory = input.sender
    textlogger.logger_folder = os.path.join(os.path.expanduser('~/.phenny'), directory)
    if not os.path.exists(textlogger.logger_folder):
        os.makedirs(textlogger.logger_folder)

    logger_file = os.path.join(textlogger.logger_folder ,datetime.date.today().__str__()+".txt")
    pdb.set_trace()
    message= {
        'channel': input.sender,
        'nick': input.nick,
        'msg': input.group(1),
        'chars': len(input.group(1)),
        }

    # format action messages
    if message['msg'][:8] == '\x01ACTION ':
        message['msg'] = '* {0} {1}'.format(message['nick'], message['msg'][8:-1])
    with open(logger_file , 'a+') as f:
        f.write("<"+ str(message['nick']) +">: "+ str(message['msg'])+"\n")



textlogger.priority = 'low'
textlogger.rule = r'(.*)'
textlogger.thread = False

if __name__ == '__main__':
    print(__doc__.strip())
