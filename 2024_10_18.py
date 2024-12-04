# %%
import csv
import pandas as pd
# %%
with open('test.csv', encoding='utf-8') as file:
    f = csv.reader(file)

    max_wind = 0.0
    min_wind = 11.4
    next(f)
    
    for row in f:
        try:
            wind = float(row[3]) if row[3] != '' else 0
        except ValueError:
            continue

        # 최대 풍속
        if max_wind < wind:
            max_wind = wind
        
        # 최소 풍속
        if min_wind > wind:
            min_wind = wind

    print('지난 10 년간 최대 풍속은', max_wind, 'm/s 입니다.')
    print('지난 10 년간 최소 풍속은', min_wind, 'm/s 입니다.')
# %%
