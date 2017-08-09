import PyPDF2
import requests
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
	

def crawler(college, path):
	
    url_path = "https://" + college['domain_name'] + "/" + college['cds_doc_path']
    file_name = college['file_name_prepend'] + college['file_name_root'] + college['file_name_append'] + college['file_name_postpend'] + college['file_ext']
    url_file_path = url_path +  "/" + file_name
    print(url_file_path)
    get_web_file(url_file_path, path)
    archive_file_path = os.path.join(path, file_name)
    file_obj = open(archive_file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(file_obj)
    content = ""
    for i in range(17, 18):
        content += pdf_reader.getPage(i).extractText() + "\n"
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    #print(content)
	
    return content

#short_name	domain_name	cds_doc_path	file_name_root	file_name_prepend  file_name_append file_name_postpend file_ex	

def initialize_rowdict(row):
    
	return{
	'long_name': row[0],
	'short_name': row[1],
	'domain_name': row[2],
	'cds_doc_path': row[3],
	'file_name_root': row[4],
	'file_name_prepend': row[5],
	'file_name_append': row[6],
	'file_name_postpend': row[7],
	'file_ext': row[8]
	}
	

		
def main():
    project = "ccplusplus"
    path = create_workspace(project)
    contents = []
    college_master_list = [
	["Connecticut College", "conncoll", "www.conncoll.edu", "media/new-media/ir-office", "CDS_", "Connecticut-College-", "2016-2017", "", ".pdf"],
	["New York University", "nyu", "www.nyu.edu", "content/dam/nyu/institutionalResearch/documents", "CDS_", "",  "2016-2017", "", ".pdf"],
	["Colgate University", "colgate", "www.colgate.edu", "docs/default-source/default-document-library", "cds_", "", "2016-2017", "_updated_02142016", ".pdf"]
	]
	
    for college_row in college_master_list:
        college_hook = initialize_rowdict(college_row)
        content = crawler(college_hook, path)
        contents.append(content)
		
    print(len(contents))
	
#----------------------------------------------------------------------#

if __name__ == "__main__":
    main()