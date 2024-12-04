# %%
# %pip install bs4

# %%
from bs4 import BeautifulSoup
import urllib.request

# %%
html = '<h1 id="title">한빛출판네트워크</h1><div class="top"><ul class="menu"><li><a href=https://hanbit.co.kr/member/login.html class="login">로그인 </a></li></ul><ul class="brand"><li><a href=http://hanbit.co.kr/media/>한빛미디어<li><a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li></ul></div>'
soup = BeautifulSoup(html, 'html.parser')

# %%
print(soup.prettify())
print(soup.h1)
print(soup.div)
print(soup.a)

# %%
title = soup.find(id='title')
print(title)

select = soup.select('a')
print(select)

# %%
address = 'https://www.hollys.co.kr'
result = []

for page in range(1, 59):
    holly_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?page=NO=%d&sido=&gugun=&store=' % page
    print(holly_url)

    html = urllib.request.urlopen(holly_url)
    soup = BeautifulSoup(html, 'html.parser')
    tag_body = soup.find('tbody')

    for store in tag_body.find_all('tr'):
        if len(store) <= 3:
            break

        store_td = store.find_all('td')
        store_name = store_td[1].string
        store_sido = store_td[0].string
        store_address = store_td[2].string
        store_phone = store_td[3].string
        result.append([store_name] + [store_sido] + [store_address] + [store_phone])
        
# %%
len(result)
print(store_td)
print(store_td[1])
print(store_td[1].string)
# %%
