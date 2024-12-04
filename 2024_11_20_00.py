# %%
# %pip install selenium

# %%
from selenium import webdriver
from bs4 import BeautifulSoup

# %%
# wd = webdriver.Chrome()
# wd.get('http://www.hanbit.co.kr')

# %%
wd = webdriver.Chrome()
wd.get('https://www.coffeebeankorea.com/store/store.asp')
wd.execute_script('storePop2(3)')
wd.execute_script('storePop2(5)')

# %%
html = wd.page_source
soup = BeautifulSoup(html, 'html.parser')

# %%
store_name_h2 = soup.select('div.store_txt>h2')
print(store_name_h2)

# %%
store_name = store_name_h2[0].string
print(store_name)

# %%
store_info = soup.select('div.store_txt > table.store_table > tbody > tr > td')
print(store_info)

# %%
store_address_list = list(store_info[2])
print(store_address_list)

# %%
store_address = store_address_list[0]
print(store_address)

# %%
store_phone = store_info[3].string
print(store_phone)

# %%
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

# [CODE 1]
def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome()

    # 마지막 매장번호(최근 신규 매장번호) 까지 반복
    for i in range(1, 389):
        wd.get(CoffeeBean_URL)

        # 웹페이지 연결할 동안 1초 대기
        time.sleep(1)

        try:
            wd.execute_script("storePop2(%d)" %i)

            # 스크립트 실행할 동안 1초 대기
            time.sleep(1)

            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name = store_name_h2[0].string

            # 매장 이름 출력하기
            print(store_name)
            
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
            store_address_list = list(store_info[2])
            store_address = store_address_list[0]
            store_phone = store_info[3].string

            result.append([store_name]+[store_address]+[store_phone])
        except:
            continue
    return None

# [CODE 0]
def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result) #[CODE 1]

    CB_tbl = pd.DataFrame(result, columns = ('store', 'address', 'phone'))
    CB_tbl.to_csv('dataset/CoffeeBean.csv', encoding = 'cp949', mode = 'w', index = True)

if __name__ == '__main__':
    main()

# %%
