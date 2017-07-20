#!/Anaconda3/python
# shakespeare

'''
This is a file for figuring stuff out
'''

#-----------------------------------------------------------------------------------------------------#

from bs4 import BeautifulSoup

import os
import requests


def blaze_path(path):
    if not os.path.exists(path):
        os.mkdir(path)


def create_workspace(project):
    path = os.path.join("c:/", project)
    blaze_path(path)

    return path


def create_file(file_path, content):
    with open(file_path, 'w') as f:
        print(content, file=f, flush=True)
        print("Creating: " + file_path + content[0:36])


def main():
    project = "shakespeare"
    path = create_workspace(project)
    url = "http://shakespeare.mit.edu/comedy_errors/full.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #scene_numeral, scene_location
    #print(soup.h3.string)

    tags = ['b', 'blockquote', 'h3']
    stage_directions_list = list()
    character_list = list()
    speech_list = list()
    scene_list = list()

    for tag in tags:
        string = True
        if tag == 'blockquote':
            string = False
        for member in soup.find_all(tag):
            if string:
                member_str = member.string
                if tag == 'b':
                    character_list.append(member_str)
                else:
                    scene_list.append(member_str)

               # print(member_str)
            else:
                if member.i is not None:
                    stage_directions_list.append(member.i.string)
                    #print(member.i.string)
                else:
                    for line in member.find_all('a'):
                        line_str = line.string
                        speech_list.append(line_str)
                        print(line_str)

    logs = [(stage_directions_list, 'stage_directions'),
                 (character_list, 'characters'),
                 (speech_list, 'speeches'),
                 (scene_list, 'scenes')]
    for log, log_name in logs:
        file_name = log_name + '.txt'
        file_path = os.path.join(path, file_name)
        content = ""
        delim = "\n"
        for line in log:
            line_str = line + delim
            content += line_str

        create_file(file_path, content)





# ----------------------------------------------------------------------#

if __name__ == "__main__":
    main()