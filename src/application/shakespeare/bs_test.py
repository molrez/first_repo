from bs4 import BeautifulSoup

import ast
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
    root_url = "http://shakespeare.mit.edu"
    plays = ['allswell', 'asyoulikeit', 'comedy_errors', 'cymbeline', 'lll',
             'measure', 'merry_wives', 'merchant', 'midsummer', 'much_ado',
             'pericles', 'taming_shrew', 'tempest', 'troilus_cressida',
             'twelfth_night', 'two_gentlemen', 'winters_tale', '1henryiv',
             '2henryiv', 'henryv', '1henryvi', '2henryvi', '3henryvi', 'henryviii',
             'john', 'richardii', 'richardiii', 'cleopatra', 'coriolanus', 'hamlet',
             'julius_caesar', 'lear', 'macbeth', 'othello', 'romeo_juliet', 'timon',
             'titus']

    for play in plays:
        play_url = root_url + "/" + play + '/' + "full" + ".html"
        page = requests.get(play_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        play = dict()
        play_list = list()
        global_line_counter = 0
        speech_counter = 0
        play_name = soup.title.string[:-15]
        print(play_name)
        play['name'] = play_name
        play['content'] = list()
        current_act = {'name': '', 'num': 0, 'modified': False}
        current_scene = {'name': '', 'num': 0, 'location': '', 'modified': False}
        current_speaker = {'name': '', 'act': current_act['num'], 'scene': current_scene['num'], 'modified': False}

        for member in soup.find_all():

            if member.name == 'h3':

                if member.string[0] == 'A':
                    current_act['name'] = member.string
                    current_act['num'] += 1
                    current_act['modified'] = True
                    current_scene['num'] = 0
                    act_line_counter = 0
                    current_speaker['act'] = current_act['num']
                    if not current_speaker['modified']:
                        current_speaker['modified'] = True
                else:

                    scene_name = member.string.split('.')[0]
                    scene_location = member.string.split('.')[1][1:]
                    # print(scene_name)
                    # print(scene_location)
                    current_scene['name'] = scene_name
                    current_scene['num'] += 1
                    current_scene['location'] = scene_location
                    current_scene['modified'] = True
                    scene_line_counter = 0
                    current_speaker['scene'] = current_scene['num']
                    if not current_speaker['modified']:
                        current_speaker['modified'] = True

            if member.name == 'a':

                if "name" in member.attrs:
                    attrib = member["name"]
                    if attrib[0] == 's':
                        speech_counter += 1
                        local_line_counter = 0
                        current_speaker['name'] = member.string

                    else:
                        current_speech = member.string
                        global_line_counter += 1
                        act_line_counter += 1
                        scene_line_counter += 1
                        local_line_counter += 1
                        row_dict = dict()
                        row_dict['act'] = str(current_act['num'])
                        row_dict['scene'] = str(current_scene['num'])
                        row_dict['location'] = current_scene['location']
                        row_dict['speech_counter'] = str(speech_counter)
                        row_dict['line_counter'] = str(global_line_counter)
                        row_dict['act_line_counter'] = str(act_line_counter)
                        row_dict['scene_line_counter'] = str(scene_line_counter)
                        row_dict['speech_line_counter'] = str(local_line_counter)
                        row_dict['current_speaker'] = current_speaker['name']
                        row_dict['speech'] = current_speech
                        row_dict['direction'] = stage_direction
                        play['content'].append(row_dict)

            key = 'name'
            if member.name == 'i':

                try:
                    directions_current_speech = current_speech

                except UnboundLocalError:
                    directions_current_speech = None

                try:
                    directions_local_line_counter = local_line_counter

                except UnboundLocalError:
                    directions_local_line_counter = 0

                finally:
                    stage_direction = member.string
                    row_dict = dict()
                    row_dict['act'] = str(current_act['num'])
                    row_dict['scene'] = str(current_scene['num'])
                    row_dict['location'] = current_scene['location']
                    row_dict['speech_counter'] = str(speech_counter)
                    row_dict['line_counter'] = str(global_line_counter)
                    row_dict['act_line_counter'] = str(act_line_counter)
                    row_dict['scene_line_counter'] = str(scene_line_counter)
                    row_dict['speech_line_counter'] = str(directions_local_line_counter)
                    row_dict['speech'] = directions_current_speech
                    row_dict['direction'] = stage_direction
                    play['content'].append(row_dict)
                    stage_direction = None
        file_name = play_name + "_" + "output.txt"
        file_path = os.path.join(path, file_name)
        content = ""
        for row in play['content']:
            content += (str(row) + "\n")
        create_file(file_path, content)

        with open(file_path, 'r') as play:
            for line in play:
                try:
                    row_dict = ast.literal_eval(line)
                    # print(str(row_dict))
                    play_list.append(row_dict)
                except SyntaxError:
                    pass



    
    #for line in play_list:
        #if line['speech'] is not None:
            #if "love" in line['speech']:
                #if line['current_speaker'] == "LUCIANA":
                    #print(str(line))
            
if __name__ == "__main__":
    main()