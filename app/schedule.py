# app/schedule.py

from bs4 import BeautifulSoup
import requests

url="https://ais.stern.nyu.edu/aismw/get_course_schedule/1206/PT2"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "html.parser")

class_list = soup.find(id="schedules-content")

for x in class_list:
    print(x)
    print(type(x))
    print("-------next class-------")
