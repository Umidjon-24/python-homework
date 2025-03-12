from bs4 import BeautifulSoup
from bs4 import MarkupResemblesLocatorWarning
import warnings

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)


with open ('weather.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, "html.parser")
    tag = soup.table
    print(tag.text)

def highest_temp():
    highest=0
    rows = soup.find('table').find('tbody').find_all('tr')
    for row in rows:    
        temp = int(row.find_all('td')[1].text.replace("°C",""))
        if highest<temp:
            highest=temp
            day = row.find_all('td')[0].text
    return f"{day} has the highest temperature with {highest}°C"
def sunny():
    sunny_days = list()
    rows = soup.find('table').find('tbody').find_all('tr')
    for row in rows:
        condition = row.find_all('td')[2].text
        if condition == 'Sunny':
            day = row.find_all('td')[0].text
            sunny_days.append(day)
    return sunny_days
print(highest_temp())
print(sunny())
