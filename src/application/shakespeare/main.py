#!/Anaconda3/python
# shakespeare

'''
This is an application for digital Shakespeare
'''

#-----------------------------------------------------------------------------------------------------#

from utils import create_file
from utils import create_workspace
from utils import prep_file
from utils import check_url
from utils import blaze_path
from utils import get_web_file
from bs4 import BeautifulSoup

import os


def semantic_output(file_name, table, semantic):
    if semantic == "word_count":
        with open(file_name, 'w') as f:
            for word, count in table:
                f.write("{\"text\":\"%s\",\"count\":%s}," % (word, count))



def count_words(word_list):
    word_dict = dict()
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
        count = word_list.count(word)
        word_dict[word] = count
        if ' ' in word_dict:
            del word_dict[' ']
    return sorted(word_dict.items(), key=lambda item: item[1], reverse=True)



def get_words(file_name):
    word_list = list()
    with open(file_name, 'r') as f:
        raw_text = f.read()
        text = str.lower(raw_text)
        for ch in '\'`!"#$%&()*+,-./:;<=>?@[\\]^_{|}~0123456789\t\n':
            text = str.replace(text, ch, ' ')
        for word in text.split(' '):
            word_list.append(word)
    return word_list


def semantics(file_name, play):
    word_list = get_words(file_name)
    word_count = count_words(word_list)
    log_file = "c:/shakespeare/" + play + "_logfile.txt"
    semantic = "word_count"
    semantic_output(log_file, word_count, semantic)


def crawler(plays, path, root_url):
    for play in plays:
        print(play)
        file_name = "full.html"
        play_root = root_url + "/" + play
        url_full_play = play_root + "/" + file_name
        if check_url(url_full_play):
            destination_path = os.path.join(path, play)
            blaze_path(destination_path)
            file_name = play + ".html"
            destination = os.path.join(destination_path, file_name)
            get_web_file(url_full_play, destination)

            more_acts = True
            act = 1
            stride = 1
            more_play = True

            while more_play:
                while more_acts:
                    more_scenes = True
                    scene = 1
                    while more_scenes:
                        act_str = str(act)
                        scene_str = str(scene)
                        print(act_str + ", " + scene_str)
                        scene_file_name = play + "." + act_str + "." \
                                          + scene_str + ".html"
                        scene_url = play_root + "/" + scene_file_name
                        if check_url(scene_url):
                            act_path = os.path.join(destination_path, act_str)
                            blaze_path(act_path)
                            destination = os.path.join(act_path, scene_file_name)
                            get_web_file(scene_url, destination)
                            scene += stride
                        elif not check_url and scene == 1:
                            more_acts = False
                            more_play = False
                        else:
                            more_scenes = False
                            if scene != 1:
                                act += stride
                            else:
                                more_acts = False
                                more_play = False


        else:
            print(url_full_play + " not found!")


def main():
    project = "shakespeare"
    path = create_workspace(project)
    #plays = ['twelfth_night']
    plays = ['allswell', 'asyoulikeit', 'comedy_errors', 'cymbeline', 'lll',
             'measure', 'merry_wives', 'merchant', 'midsummer', 'much_ado',
             'pericles', 'taming_shrew', 'tempest', 'troilus_cressida',
             'twelfth_night', 'two_gentlemen', 'winters_tale', '1henryiv',
             '2henryiv', 'henryv', '1henryvi', '2henryvi', '3henryvi', 'henryviii',
             'john', 'richardii', 'richardiii', 'cleopatra', 'coriolanus', 'hamlet',
             'julius_caesar', 'lear', 'macbeth', 'othello', 'romeo_juliet', 'timon',
             'titus']

    root_url = "http://shakespeare.mit.edu"

    crawler(plays, path, root_url)

    for play in plays:
        print(play)
        source = 'c:/shakespeare/' + play + "/" + play + ".html"
        semantics(source, play)



# ----------------------------------------------------------------------#

if __name__ == "__main__":
    main()