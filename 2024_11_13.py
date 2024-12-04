# %%
# 라이브러리 불러오기
import urllib.request
import datetime
import json
import pandas as pd

# %%
service_key = ''

# %%
def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s] Url Request Success' % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Error for URL: %s' % (datetime.datetime.now(), url))
        return None
    
# %%
def get_tourism_stats_item(yyyymm, national_code, ed_cd):
    service_url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    parameters = '?_type=json&serviceKey=' + service_key
    parameters += '&YM=' + yyyymm
    parameters += '&NAT_CD=' + national_code
    parameters += '&ED_CD=' + ed_cd

    url = service_url + parameters

    ret_data = get_request_url(url)

    if ret_data == None:
        return None
    else:
        return json.loads(ret_data)

# %%
def get_tourism_stats_service(nat_cd, ed_cd, n_start_year, n_end_year):
    json_result = []
    result = []
    nat_name = ''
    data_end = "{0}{1:0>2}".format(str(n_end_year), str(12))
    is_data_end = 0

    for year in range(n_start_year, n_end_year + 1):
        for month in range(1, 13):
            if is_data_end == 1: break

            yyyymm = "{0}{1:0>2}".format(str(year), str(month))            
            json_data = get_tourism_stats_item(yyyymm, nat_cd, ed_cd)

            if json_data['response']['header']['resultMsg'] == 'OK':
                if json_data['response']['body']['items'] == '':
                    is_data_end = 1
                    data_end = '{0}{1:0>2}'.format(str(year), str(month - 1))

                    print('데이터 없음. \n 제공되는 통계 데이터는 %s년 %s월 까지 입니다.' % (str(year), str(month - 1)))
                    break

            print(json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False))   

            nat_name = json_data['response']['body']['items']['item']['natKorNm']
            nat_name = nat_name.replace(' ', '')
            num = json_data['response']['body']['items']['item']['num']
            ed = json_data['response']['body']['items']['item']['ed']
            print('[%s_%s] %s : %s' % (yyyymm, nat_name, num, ed))
            print('-' * 50)

            json_result.append({'nat_name': nat_name, 'nat_cd': nat_cd, 'yyyymm': yyyymm, 'visit_cnt': num})
            result.append([nat_name, nat_cd, yyyymm, num])
    return json_result, result, nat_name, ed, data_end

# %%
def main():
    json_result = []
    result = []

    print('국내 입국한 외국인의 통계 데이터 수집.')
    nat_cd = input('국가 코드 입력: ')
    n_start_year = int(input('조회 시작 년도 입력(예: 2019): '))
    n_end_year = int(input('조회 종료 년도 입력(예: 2019): '))
    ed_cd = 'E' # e: 방한 외래 관광객, d: 해외 출국

    json_result, result, nat_name, ed, data_end = get_tourism_stats_service(nat_cd, ed_cd, n_start_year, n_end_year)

    if nat_name == '':
        print('데이터가 전달되지 않았습니다. 공공데이터포털의 서비스 상태를 확인하기 바랍니다.')
    else:
        with open('./%s_%s_%d_%s.json' % (nat_name, ed, n_start_year, data_end), 'w', encoding='utf8') as outfile:
            json_file = json.dumps(json_result, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(json_file)

        columns = ['입국자 국가', '국가 코드', '입국 연월', '입국자 수']
        result_df = pd.DataFrame(result, columns=columns)
        result_df.to_csv('./%s_%s_%d_%s.csv' % (nat_name, ed, n_start_year, data_end), index=False, encoding='cp949')

# %%
if __name__ == '__main__':
    main()

# %%
