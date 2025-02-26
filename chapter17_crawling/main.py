'''
pip : 파이썬 패키지 관리자, 파이썬 패키지를 ㄹ설치하는 데 사용

requests 라이브러리 : 파이썬에서 HTTP 요청을 보내기 위해 가장 널리 사용되는
라이브러리 중 하나로 사용하기 쉽고 직관적인 ATI(Application Interface) 를 제공하여
request 라이브러리응 사용하면 GET, POST, DELETE  등 다양한
HTTP 매서드를간편하게 사용 가능

터미널에서 pop install requests 라고 입력

  1. 웹 크롤링의 개념
     웹 클올ㄹ링이란 완성된 웹 페이지에서 필요한 정보를ㄹ 수집하고
      선별하여 조종하는 배경으로 웹 스크래핑이라 하기도 함

       1) HTML 의 개념
       Hyper Texy Marking Languege 의 약자로 ' 웹  페이지를 만드는 문법을 갖춘 언어'
       라고 변칙되어 가자의 역할이 정해진 태그들로 구상한 언어로
       페이지를 만드는데 각각의 태그를 붙여가며 사용함

       2) HTML 구조

<html>
   head
        meta
        title
    body
        hl
        div
</html>

      3) URL : 어떤 자원의 위치를 표기하는 방법을 의미함
        http://www.google.com 과 같은 인터넷 주소를 입력하는데
        이때 입력한 주소가 URL에 들어감

'''
from http.client import responses

import requests
#
# url = "http://www.naver.com"    #naver 메인 웹페이지 주소를 url이라는 변수에 저장
# responses = requests.get(url)   # requests 모듈의 get() 메서드를 호출하여
#                                 #response 라는 변수에 저장
# print(f"응답코드 : {responses.status_code}")
# print(responses.text)

'''
  2. 검색 결과 전부를 웹 페이지 가져오기
       네이버 에서 "파이썬" 을 검색했을 때 나오는 경과 화면을 가져오는 방법
       
https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=vkdlTjs&qdt=0&ie=utf8&query=파이썬

검색하는 것이 함수개념이라면 -> 결과값은 return애 해당될텐데 ->  검색어는  argument
search(" 파이썬") ->return 검색 결과창

입력한 검색어 "파이썬"  은 quary라는 매개변수로 전달됩니다.
search(quary= "파이썬")     #keyqord argument 와 같은 형태라고 볼 수 있습니다.

매개변수를 입력하지 않은 경우에는 default 값으로 적용되기 때문에 나머지는 지워도 무방합니다.

https://search.naver.com/search.naver?query=파이썬
'''
# url = "https://search.naver.com/search.naver"
# searching_word = input("검색어를 입력하세요 >>>")
# param = {
#     "quary" : searching_word,
#     "io": "utf8",
# }
# response = requests.get(url, params= param) #dictionary의 param을 params속성에 대입
# #일부만 keyword argument 를 사용한 예시입니다. / print("dhfaijdfi, end="")
#
# print(f"응답코드 :{response.status_code}")
# print(response.text)

'''
일부 감자 웹툰의 소개 페이지를 가져오는 프로그램을 작성하시오. 
'''
# url = "https://comic.naver.com/webtoon/list"
# param = {
#     "titleld": 822556,
# }
# response = requests.get(url, params= param)
# print(f"응답코드 : {response.status_code}")
# print(response.text)

'''
구글에서 파이썬을 검색한 결과를 가지고 오는 프로그램을 작성하시오.
'''
url = "https://www. google.com/search"
param = {
    "q" : "파이썬",
}
response = requests.get(url, params= param)
print(f"응답코드 : {response.status_code}")
print(response.text)