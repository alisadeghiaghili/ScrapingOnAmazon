searchText = input().replace(' ', '+')

url = 'https://www.amazon.com/s?k=' + searchText
headers = {'User-Agent': 'test-0.1.1',
           'Accept-Language': 'en-US, en, q=.5'}
import requests
res = requests.get(url, headers = headers)

from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text)
cssSelector_title = '.a-color-base.a-text-normal'
cssSelector_link = '.s-line-clamp-2'
titles = soup.select(cssSelector_title)
links = soup.select(cssSelector_link)

import xlsxwriter
wb = xlsxwriter.Workbook(r'DestPath\test.xlsx')
ws = wb.add_worksheet('new')
ws.write('A1', 'BookName')
ws.write('B1', 'URL')

rowNum = 2
for title, link in zip(titles, links):
    # print(title.get_text())
    # print('https://www.amazon.com' + link.a['href'])
    
    ws.write('A'+str(rowNum), title.get_text())
    ws.write('B'+str(rowNum), 'https://www.amazon.com' + link.a['href'])
    rowNum += 1

wb.close()
