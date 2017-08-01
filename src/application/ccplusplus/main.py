#!/Anaconda3/python
# CC++

'''
This is an application for collecting and parsing CDS
'''

#-----------------------------------------------------------------------------------------------------#

from utils import create_file
from utils import create_workspace
from utils import prep_file
from utils import check_url
from utils import blaze_path
from utils import get_web_file


import PyPDF2
import requests
import os

#-----------------------------------------------------------------------------------------------------#


def main():
    project = "ccplusplus"
    path = create_workspace(project)
    root_url = "https://www.colgate.edu/docs/default-source/default-document-library/"
    file_name = "cds_2016-2017_updated_02142016.pdf"
    source_file_path = root_url + file_name
    get_web_file(source_file_path, path)
    archive_file_path = os.path.join(path, file_name)
    file_obj = open(archive_file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(file_obj)
    content = ""
    for i in range(17, 18):
        content += pdf_reader.getPage(i).extractText() + "\n"
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    print(content)


# ----------------------------------------------------------------------#

if __name__ == "__main__":
    main()