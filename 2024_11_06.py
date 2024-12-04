# %%
import urllib.request
import datetime
import json

# %%
client_id = ""
client_secret = ""
encText = urllib.parse.quote("미 대선")

# %%
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if rescode == 200:
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

# %%
def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_naver_search(node, src_txt, start_num, disp_num):
    base = "https://openapi.naver.com/v1/search"
    node = "/" + node + ".json"
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(src_txt), start_num, disp_num)

    url = base + node + parameters
    retData = get_request_url(url)

    if retData == None:
        return None
    else:
        return json.loads(retData)

def get_post_data(post, json_request, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    json_request.append({'cnt': cnt, 'title': title, 'description': description, 'org_link': org_link, 'link': link, 'pDate': pDate})
    return

# %%
def main():
    node = 'news'
    src_txt = '월드컵'
    cnt = 0
    json_request = []

    json_response = get_naver_search(node, src_txt, 1, 100)
    total = json_response['total']

    while ((json_response != None) and (json_response['display'] != 0)):
        for post in json_response['items']:
            cnt += 1
            get_post_data(post, json_request, cnt)

        start_num = json_response['start'] + json_response['display']
        if start_num > total:
            break

        json_response = get_naver_search(node, src_txt, start_num, 100)

    print('전체 검색 : %d 건' % total)

    with open('naver_%s.json' % (src_txt), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_request, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print('가져온 데이터 : %d 건' % cnt)
    print('파일 저장 완료')

# %%
# 테스트
main()        
# %%
