# Hotel_Review_Sentiment_Analysis(koBERT)

## ✔️ 프로젝트 주제  
<div align="center">
<img src="https://user-images.githubusercontent.com/90162819/158767907-6ef1ca4c-c13c-411e-b70f-f98bd8891e29.png" width="500"></div>

</br> 

- 코로나 이후 여행장소 측면에서 소비자들의 관심이 가장 크게 높아진 곳은 호텔(호캉스)이며, 이는 대표적인 언택트(비대면)  
여행 장소로 각광받고 있는 추세입니다.  
- '언택트'와 '휴식'에 초점을 맞춘 여행 트렌드는 앞으로도 지속될것으로 보이며, 최근 2년간('20~'21년) 고객들의 실제 리뷰와  
 평점을 바탕으로 긍정/부정 리뷰를 분류하고 예약시에 도움이 되는 서비스를 제공합니다. 

 </br> 

## ✔️ Pipeline 


**1. 데이터 수집**  

<img src="https://user-images.githubusercontent.com/90162819/158769734-1d1b4721-0a50-4c9b-b5dc-7addcb005a7d.png">

- 호텔예약플랫폼 이용률 1위 '야놀자' 활용 서울,인천송도의 주요 호텔 11곳에 대한 리뷰데이터(22921개) Crawling 진행  
- 호텔명, 평점, 리뷰텍스트, 리뷰작성일 추출  

**2. 데이터 전처리** 

- 정규표현식 적용(특수문자, 한글자 자모음, 개행문자, 이모티콘 제거)

<div align="center"><img src="https://user-images.githubusercontent.com/90162819/159422915-0b1c5dd4-1c0b-42a7-9683-40488b16727e.png" width="600"></div>
