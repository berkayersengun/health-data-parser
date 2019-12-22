from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(open('resources/printable_diary'), 'html.parser')

# alldays = soup.find_all('td',class_='first',text='TOTAL:')
# print(alldays[2])
# print(soup.find('td',class_='first',text='TOTAL:'))
# test = soup.find_all('td',class_='first',text='TOTAL:')

# for child in test:
#     print(child.next_sibling.next_sibling)

# for child in soup.find('a').children:
#     print(child)
# for day in alldays:
#     print(day.contents)


dates = soup.find_all('h2', id="date")
# print(dates[1].next_sibling.next_sibling)
data = {}
for child in dates:
    date = child.get_text()
    # print(date, end=': ')
    daily_cal = child.next_sibling.next_sibling.find('td', class_='first',
                                                     text='TOTAL:').next_sibling.next_sibling.get_text()
    # print(daily_cal)
    data[date] = daily_cal

json_data = json.dumps(data)
print(json_data)

with open('data.json', 'w') as f:  # writing JSON object
    f.write(json_data)
