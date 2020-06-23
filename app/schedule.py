# app/schedule.py

from bs4 import BeautifulSoup
import bs4 # needed for element type identification
import requests
import pandas as pd

url="https://www.stern.nyu.edu/registrar/shim2.cgi?studtype=PT2&tm=2020F"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "html.parser")

class_list = soup.find(id="schedules-content")

columns = [] # list for table column headings
cells = [] # list for table rows data

for each in class_list:

    print("-----start class-----") 

    if isinstance(each, bs4.element.Tag):

        #print(each) # remove this when finished

        if each.find('a') is None:
            category = each.get_text() # course category e.g. Core Courses
            print(category)

        else:
            row_data = []
            
            course_code = each.find('a').get_text() # course code e.g. ACCT-GB.3304
            course_name = each.find('a').next_sibling # course name e.g. Modeling Financial Statements (3)

            row_data.append(category) # adding category to row
            row_data.append(each.find('a').get_text()) # adding course code to row
            row_data.append(each.find('a').next_sibling) # adding course name to row

            try: # need to use Try because some courses do not have specializations
                specs = each.find("div", {"id": course_code+"_spec"}).get_text() # getting list of specializations
            except:
                specs = ""
            
         
            # table parsing 
            # https://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/

            table = each.find_all('table')[0]

            table_cols = table.findAll('th')
            #columns = []
            for col in table_cols:
                columns.append(col.get_text())          
            
            table_rows = table.findAll('tr')
            print(table_rows)
            #cells = []
            for row in table_rows[1:]: # for loop, skips the first row (the headers) of the HTML table 
                starting_row_count= len(row_data)
                table_data = row.findAll('td')
                
                for cell in table_data:
                    row_data.append(cell.get_text().strip())

                for line in specs.splitlines()[2:]: # adding each specialization as a separate element to the row data list
                    row_data.append(line.strip())

                cells.append(row_data)
                row_data = row_data[0:starting_row_count] # resets the row list back to include only category, name, and code


    #print(each.encode('utf-8'))
    print("-----end class-----")

print(columns)
print(cells)        
        
df = pd.DataFrame(cells) # https://kite.com/python/answers/how-to-convert-a-list-of-lists-into-a-pandas-dataframe-in-python
print(df)
df.to_csv('file_name.csv')