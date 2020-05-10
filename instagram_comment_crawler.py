from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup

# 1 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")

# 2 인스타그램 열기
raw = driver.get("https://www.instagram.com/p/B_6ThCKHP4I/")
# html = BeautifulSoup(raw.text, 'html.parser')

# 3 댓글 더보기
driver.implicitly_wait(5)
# comment_more = driver.find_element_by_css_selector("div.Igw0E.IwRSH.YBx95._4EzTm.MGdpg button.dCJp8.afkep")

def element_check():
    try:
        driver.find_element_by_css_selector("div.Igw0E.IwRSH.YBx95._4EzTm.MGdpg button.dCJp8.afkep")
        return True
    except NoSuchElementException:
        return False

# print(element_check())
for i in range(3) :
    comment_more = driver.find_element_by_css_selector("div.Igw0E.IwRSH.YBx95._4EzTm.MGdpg button.dCJp8.afkep")
    comment_more.click()
    driver.implicitly_wait(5)
    print("클릭을", i+1, "번 했습니다.")

    # if element_check() == True :
    #     continue
    # else :
    #     print("댓글 불러오기 완료.")
    #     break


## 댓글 더 보기 : div.Igw0E.IwRSH.YBx95._4EzTm.MGdpg button.dCJp8.afkep (1번 누를 때마다 12개씩 추가됨)
## 답글 보기 : div.Igw0E > button.sqdOP.yWX7d,y3zJF
## 댓글 컨테이너 : ul.Mr508 div.C4VMK
 ## 작성자 이름 : a.sqdOP
 ## 댓글 내용 : span


# 4 게시물 12개 저장
# posts = driver.find_elements_by_css_selector("div.v1Nh3")
# posts = posts[:12]

# 5 게시물 반복 수집
# for p in posts :
#     p.click()
#     driver.implicitly_wait(3)
#     try :
#         words_box = driver.find_element_by_css_selector("div.C4VMK span").text
#     except :
#         words_box = "본문 내용 없음."
#     print(words_box)
#     print("="*50)
#         ## 위에서 사용한 button_close를 다시 재사용.
#     button_close = driver.find_element_by_css_selector("button.ckWGn").click()
#
# driver.close()

# for n in range(1, 6):
#     # 컨테이너 : div.section-result-content
#     cafes = driver.find_elements_by_css_selector("div.section-result-content")
#
#     for c in cafes:
#         # 이름 h3 > span
#         # 평점 span.cards-rating-score
#         # 주소 span.section-result-location
#
#         name = c.find_element_by_css_selector("h3 > span").text
#         try :
#             score = c.find_element_by_css_selector("span.cards-rating-score").text
#         except :
#             score = "평점 없음"
#         address = c.find_element_by_css_selector("span.section-result-location").text
#
#         print(name + " / " + score + " / " + address)
#
#     page_bar = driver.find_elements_by_css_selector("div.n7lv7yjyC35__right > *")
#
#     if n != 5 :
#         page_bar[1].click()
#     else :
#         print("수집완료")
#         break
# driver.close()