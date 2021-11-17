import sys

from selenium import webdriver
import time
import random as r

# 1 웹드라이버 켜기
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")

# 2 인스타그램 열기
raw = driver.get("https://www.instagram.com/p/B_6ThCKHP4I/")
driver.implicitly_wait(5)

# 3 댓글 전체 불러오기

## 댓글 불러오는 버튼 반복 클릭
for i in range(999) :
    try :
        comment_more = driver.find_element_by_css_selector("div.Igw0E.IwRSH.YBx95._4EzTm.MGdpg button.dCJp8.afkep")
        comment_more.click()
        driver.implicitly_wait(5)
        print("클릭을", i + 1, "번 했습니다.")
    except :
        print("댓글 전체 불러오기 완료.")
        break

# 4 답글 전체 불러오기
comment_more = driver.find_elements_by_css_selector("div.Igw0E > button.sqdOP.yWX7d,y3zJF")

for i in range(999) :
    try:
        more_box = comment_more[i].find_element_by_css_selector("span.EizgU").text
        count = int(more_box[-3])
        if count >= 9 :
            comment_more[i].click()
            time.sleep(0.15)
            comment_more[i].click()
            time.sleep(0.15)
            comment_more[i].click()
            time.sleep(0.15)
        elif count >= 4 :
            comment_more[i].click()
            time.sleep(0.15)
            comment_more[i].click()
            time.sleep(0.15)
        else :
            comment_more[i].click()
            time.sleep(0.15)
        print("클릭을", i + 1, "번 했습니다.")
    except:
        print("답글 불러오기 완료")
        break

# 댓글 더 보기 : div.Igw0E.IwRSH.YBx95._4EzTm.MGdpg button.dCJp8.afkep (1번 누를 때마다 12개씩 추가됨)
# 답글 보기 : div.Igw0E > button.sqdOP.yWX7d,y3zJF
 ## 답글 갯수 : span.EizgU
# 댓글 컨테이너 : ul.Mr508 div.C4VMK
 ## 작성자 이름 : a.sqdOP
 ## 댓글 내용 : span

# 5 20학번 중 정답자 아이디 수집 (학번 없으면 수집X)
driver.implicitly_wait(3)
containers = driver.find_elements_by_css_selector("ul.Mr508 div.C4VMK")
comments = driver.find_elements_by_css_selector("ul.Mr508 div.C4VMK span")
award_dic = {}

##  댓글 반복 수집
id_count = 0

for i in containers :
    comment = i.find_element_by_css_selector("span")
    try :
        std_id = comment.text
        if "6020" and ("8개" or "8새") in std_id :
            account = i.find_element_by_css_selector("a.sqdOP").text
            print(account, "/ 학번 있음 / 정답 O /", std_id)
            idx = std_id.index("6020")
            id_num = std_id[idx:idx+8]
            print("학번", id_num)
            id_count += 1
            award_dic[account] = id_num
    except :
        print("오류 발생")

print("="*20)
print("총 댓글 개수 : ", len(comments))
print("정답 및 학번 포함 댓글 수 : ", id_count)
print("오답 및 학번 없는 댓글 수 : ", len(comments)-id_count)
print("="*20)
print("정답자 아이디 명단")
print(award_dic)
print("정답자 : 총",len(award_dic),"명")
print("="*20)

# 7 당첨자 랜덤 추출
award = []

print("치킨 당첨자 : ")
while len(award) != 3 :
    pick = account, id_num = r.choice(list(award_dic.items()))
    if ( pick not in award) :
        award.append(pick)
        print(account, id_num, sep=" / ")
print("="*20)

print("베라 당첨자 : ")
while len(award) != 8 :
    pick = account, id_num = r.choice(list(award_dic.items()))
    if ( pick not in award) :
        award.append(pick)
        print(account, id_num, sep=" / ")
print("="*20)

print("스벅 당첨자 : ")
while len(award) != 15 :
    pick = account, id_num = r.choice(list(award_dic.items()))
    if ( pick not in award) :
        award.append(pick)
        print(account, id_num, sep=" / ")

print("="*20)
print("명지내일 성년의 날 이벤트에 참여해주셔서 감사합니다. 다음에 더 좋은 이벤트로 찾아뵙겠습니다. ")

# 8 크롬 창 닫기
driver.close()