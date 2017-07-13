#!/Anaconda3/python
# shakespeare

'''
This is a file for figuring stuff out
'''

#-----------------------------------------------------------------------------------------------------#

from bs4 import BeautifulSoup
import requests

def main():
    url = "http://shakespeare.mit.edu/twelfth_night/twelfth_night.4.3.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.get_text())




# ----------------------------------------------------------------------#

if __name__ == "__main__":
    main()