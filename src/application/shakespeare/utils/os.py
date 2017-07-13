#!/Anaconda3/python
# compadre-toolkit

'''
we're handling basic "operating system" functions here
'''

#-----------------------------------------------------------------------------------------------------#

import os
import datetime
import wget
import urllib
from urllib.request import urlopen
from random import randint
from time import sleep


#-----------------------------------------------------------------------------------------------------#
'''create a workspace'''


def create_workspace(project):
    path = os.path.join("c:/", project)
    blaze_path(path)

    return path


#-----------------------------------------------------------------------------------------------------#
'''make a directory'''


def blaze_path(path):
    if not os.path.exists(path):
        os.mkdir(path)


#-----------------------------------------------------------------------------------------------------#
'''produce a useful timestamp'''


def stop_watch():
    d = datetime.datetime.now()
    now = d.strftime("%Y/%m/%d %H:%M:%S")

    return now


#-----------------------------------------------------------------------------------------------------#
'''create a file'''


def create_file(file_path, content):
    with open(file_path, 'w') as f:
        print(content, file=f, flush=True)
        print("Creating: " + file_path + content[0:36])


#-----------------------------------------------------------------------------------------------------#
'''append a file'''


def append_file(file_path, content):
    with open(file_path, 'a') as f:
        print(content, file=f, flush=True)
        print("Appending: " + file_path + content[0:36])


#-----------------------------------------------------------------------------------------------------#
'''prepare/create or append, and return a file name'''


def prep_file(path, page, action='create'):
    file_name, content = page
    file_path = os.path.join(path, file_name)
    if action == 'create':
        create_file(file_path, content)
    elif action == 'append':
        append_file(file_path, content)

    return file_path


#-----------------------------------------------------------------------------------------------------#
'''check a url'''


def check_url(url):
    try:
        with urllib.request.urlopen(url):
            sleep(randint(0, 1))
            return True
    except:
        pass


# -----------------------------------------------------------------------------------------------------#
'''get a web file'''


def get_web_file(url, destination):
    sleep(randint(0, 1))
    now = stop_watch()
    #print("\n" + now + " downloading file " + url)
    try:
        os.remove(destination)
    except OSError:
        pass
    wget.download(url, destination)
    now = stop_watch()
    #print("\n" + now + " completed file " + destination)