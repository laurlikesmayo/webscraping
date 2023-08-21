from bs4 import BeautifulSoup
import requests;

url = "https://www.mountainproject.com/area/classics"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

grades = doc.find_all(class_="rateYDS")
searchtext = input('What grade are you looking for?: ')
for grade in grades:
    if searchtext in grade.text:
        parent = grade.parent.parent
        hi = parent.find(class_ = "text-truncate")
        if hi is not None:
            hello =hi.text.strip().replace("●", "")
            print(hello.strip())
            


