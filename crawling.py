from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
import datetime
from datetime import timedelta

def yanolja_crawl(url):
    global df # 전역 변수를 지역 범위에서 적용
    driver.get(url)

    hotel = driver.find_element_by_css_selector('section.PlaceDetailTitle_titleContainer__3sGdf h1').text
    hotel = hotel.replace("[★숙박대전] ", "")

    # 리뷰 페이지 클릭 (Click review page)
    driver.find_element_by_css_selector('section.PlaceDetailTitle_titleContainer__3sGdf > a').click()

    import time
    time.sleep(1)

    SCROLL_PAUSE_TIME = 1.5

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 아래쪽으로 스크롤
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
        time.sleep(SCROLL_PAUSE_TIME)

        # 스크롤 위치 계산
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

    # 스크롤 끝나고 페이지 elements 가져오기
    raw = driver.page_source # 페이지의 elements 모두 가져오기
    html = BeautifulSoup(raw, "html.parser")

    # 리뷰 텍스트 선택자: div.item-wrap
    reviews = html.select("div.item-wrap")

    columns = ['hotel', 'star', 'review', 'date']

    for r in reviews:
        review = r.select_one("p")
        date = r.select_one('time')

        stars = r.select('.container.score')
        for s in stars:
            star_count = 5 - len(s.select(".ico.gray"))

        df = df.append(pd.DataFrame([[hotel, star_count, review.text, date.text]], columns = columns),
                       ignore_index=True)
    
def change_date(x):
    now = datetime.datetime.today()
    today = now.strftime("%Y. %m. %d")
    yesterday = (now - timedelta(days=1)).strftime("%Y. %m. %d")
    _2days_ago = (now - timedelta(days = 2)).strftime("%Y. %m. %d")
    _3days_ago = (now - timedelta(days = 3)).strftime("%Y. %m. %d")
    hour = int(datetime.datetime.today().strftime("%H"))
    if "시간 전" in x:
        x = int(x.replace("시간 전", ""))
        if hour - x > 0: return today
        else: return yesterday
    elif "일 전" in x:
        if "1" in x: return yesterday
        elif "2" in x: return _2days_ago
        else: return _3days_ago
    else: return x

url_list = [ "https://www.yanolja.com/hotel/10041653", # 서울 신라호텔
            # "https://www.yanolja.com/hotel/3018226", # 인천 파라다이스 시티
            # "https://www.yanolja.com/hotel/3002096", # 인천 네스트
            # "https://www.yanolja.com/hotel/3000605" # 서울 라마다 동대문
            # "https://www.yanolja.com/hotel/3015391" # 용산 노보텔 엠배서더
            # "https://www.yanolja.com/hotel/3001542" # 서울 신라스테이 광화문
            # "https://www.yanolja.com/hotel/3012800" # 서울 글래드 마포
            # "https://www.yanolja.com/hotel/3001564" # 서울신라스테이 구로
            # "https://www.yanolja.com/hotel/3000998" # 송도 센트럴 파크
            # "https://www.yanolja.com/hotel/3000622" # 송도 오라카이
            # "https://www.yanolja.com/hotel/1000110435" # 서울 그랜드 하얏트
           ]

columns = ['hotel', 'star', 'review', 'date']
df = pd.DataFrame(columns = columns) # 데이터프레임 생성

driver = webdriver.Chrome('./chromedriver')
for url in url_list:
    yanolja_crawl(url)

driver.close()

df['real_date'] = df['date'].apply(change_date)

df["length"] = df["review"].map(lambda x: len(x))

df.to_csv("신라.csv")

# 그랜드하얏트 = pd.read_csv('그랜드하얏트.csv')
# 글래드 = pd.read_csv('글래드.csv')
# 네스트 = pd.read_csv('네스트.csv')
# 노보텔 = pd.read_csv('노보텔.csv')
# 라마다 = pd.read_csv('라마다.csv')
# 센트럴 = pd.read_csv('센트럴.csv')
# 신라 = pd.read_csv('신라.csv')
# 신라스테이 = pd.read_csv('신라스테이.csv')
# 신라구로 = pd.read_csv('신라스테이구로.csv')
# 오라카이 = pd.read_csv('오라카이.csv')
# 파라다이스 = pd.read_csv('파라다이스.csv')


# df = pd.concat([그랜드하얏트, 글래드, 네스트, 노보텔, 라마다, 센트럴, 신라, 신라스테이, 신라구로, 오라카이, 파라다이스])

# df.to_csv("datacsv.csv", encoding="utf-8-sig")
    

