# app/schedule.py

from bs4 import BeautifulSoup
import bs4 # needed for element type identification
import requests
import pandas

url="https://www.stern.nyu.edu/registrar/shim2.cgi?studtype=PT2&tm=2020F"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "html.parser")

class_list = soup.find(id="schedules-content")

for each in class_list:
    print("-----start class-----") 
    if isinstance(each, bs4.element.Tag):

        #print(each) # remove this when finished

        if each.find('a') is None:
            category = each.get_text()
            print(category)
        else:
            print(each.find('a').get_text()) # course code e.g. ACCT-GB.3304
            print(each.find('a').next_sibling) # course name e.g. Modeling Financial Statements (3)

            # table parsing 
            # https://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/

            table = each.find_all('table')[0]

            table_cols = table.findAll('th')
            columns = []
            for col in table_cols:
                columns.append(col.get_text())            
            
            table_data = table.findAll('td')
            cells = []
            for cell in table_data:
                cells.append(cell.get_text())            

            print(columns)
            print(cells)
        
        
        





    #print(each.encode('utf-8'))
    print("-----end class-----")

