# %%
import urllib.request

# %%
nate_url = 'https://www.nate.com/'
html_obj = urllib.request.urlopen(nate_url)
html = html_obj.read()
print(html)

# %%
import bs4

bs_obj = bs4.BeautifulSoup(html, 'html.parser')
print(bs_obj)

# %%
webpage = open('html_01.html', 'rt', encoding='utf-8').read()
bs_obj = bs4.BeautifulSoup(webpage, 'html.parser')
print(bs_obj)

# %%
# div의 태그 내용 추출
divs = bs_obj.findAll('div')
print(divs)

# %%
# ul 태그 내용 추출
uls = bs_obj.findAll('ul')
print(uls)

# %%
webPage = open('html_02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'id':'myId1'})
print(tag)
print(tag.text)

tag = bsObject.find('div', {'class':'myClass1'})
print(tag)
print(tag.text)

tag = bsObject.findAll('div', {'class':'myClass1'})
print(tag)
# print(tag.text)

# %%
webPage = open('html_02.html', 'rt', encoding='utf-8').read()
bs_obj = bs4.BeautifulSoup(webPage, 'html.parser')

ul_value = bs_obj.find('ul', {'class':'myClass2'})
print(ul_value)
print()

li_value = bs_obj.findAll('li', {'class': 'myClass2'})
print(li_value)
print()

# %%
tag = bs_obj.findAll('a')
for t in tag:
    print(t['href'])

# %%
webPage = open('html_01.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag_li_all= bsObject.findAll('li')
for tag_li in tag_li_all :
    print(tag_li.text)
print()
for i in range(len(tag_li_all)) :
    print(tag_li_all[i].text)

# %%
nate_url = 'https://www.nate.com/'
html_obj = urllib.request.urlopen(nate_url)
wab_page = html_obj.read()
bs_obj = bs4.BeautifulSoup(wab_page, 'html.parser')

tag = bs_obj.find('div', {'id': 'NateBi'})
print(tag, '\n')

a_tag = tag.find('a')
print(a_tag, '\n')

href = a_tag['href']
print(href)

text = a_tag.text
print(text)

# %%
# tag = bs_obj.find('div', {'id': 'wrab_nav'})
# print(tag, '\n')

# lis = tag.findAll('li')
# for li in lis:
#     print(li.text, end=' ')

# %%
import csv
import time
import datetime

csvName = 'dataset/datetime.csv'
with open(csvName, 'w', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일', '시분초'])

count = 10
while count > 0 :
    count -= 1

    now = datetime.datetime.now() 
    yymmdd = now.strftime('%Y-%m-%d')
    hhmmss = now.strftime('%H:%M:%S')
    time_list = [yymmdd, hhmmss]
    print(time_list)

    with open(csvName, 'a', newline='') as csvFp:
        csvWriter = csv.writer(csvFp)
        csvWriter.writerow(time_list)

    time.sleep(3)

# %%
csv_name = 'dataset/sokcho_weather.csv'
with open(csv_name, 'w', newline='') as csv_fp:
    csv_writer = csv.writer(csv_fp)
    csv_writer.writerow(['연월일', '시분초', '온도', '습도', '강수량', '풍향'])

nate_url = 'https://news.nate.com/weather?areaCode=11D20401'

while True:
    html_obj = urllib.request.urlopen(nate_url)
    web_page = html_obj.read()
    bs_obj = bs4.BeautifulSoup(web_page, 'html.parser')
    tag = bs_obj.find('div', {'class': 'right_today'})
    temper = tag.find('p', {'class': 'celsius'}).text
    humi = tag.find('p', {'class': 'humidity'}).text
    rain = tag.find('p', {'class': 'rainfall'}).text
    wind = tag.find('p', {'class': 'wind'}).text

    now = datetime.datetime.now()
    yymmdd = now.strftime('%Y-%m-%d')
    hhmmss = now.strftime('%H:%M:%S')

    weather_list = [yymmdd, hhmmss, temper, humi, rain, wind]
    with open(csv_name, 'a', newline='') as csv_fp:
        csv_writer = csv.writer(csv_fp)
        csv_writer.writerow(weather_list)

    time.sleep(1)

# %%
