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

import os


def main():
    project = "shakespeare"
    path = create_workspace(project)
    #plays = ['allswell']
    plays = ['allswell', 'asyoulikeit', 'comedy_errors', 'cymbeline', 'lll',
             'measure', 'merry_wives', 'merchant', 'midsummer', 'much_ado',
             'pericles', 'taming_shrew', 'tempest', 'troilus_cressida',
             'twelfth_night', 'two_gentlemen', 'winters_tale', '1henryiv',
             '2henryiv', 'henryv', '1henryvi', '2henryvi', '3henryvi', 'henryviii',
             'john', 'richardii', 'richardiii', 'cleopatra', 'coriolanus', 'hamlet',
             'julius_caesar', 'lear', 'macbeth', 'othello', 'romeo_juliet', 'timon',
             'titus']

    root_url = "http://shakespeare.mit.edu"

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





# ----------------------------------------------------------------------#

if __name__ == "__main__":
    main()