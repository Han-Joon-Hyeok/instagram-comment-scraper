import selenium
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import time
import random as r
import getpass

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def set_chrome_driver():
    user_agent = UserAgent(verify_ssl=False).random
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# 1 Set Chrome Webdriver (Auto Download)
driver = set_chrome_driver()

# 2 Move to Instagram Login Page
def move_to_url(url):
    return driver.get(url)

login_url = "https://www.instagram.com/accounts/login/"
raw = move_to_url(login_url)
driver.implicitly_wait(5)

# 3 Login Instagram Account
def login_input_send_keys(username, password):
    try:
        types = {'username': username, 'password': password}
        for type in types:
            print(type)
            input_css_selector = f'input[name="{type}"]'
            inputBox = driver.find_element(By.CSS_SELECTOR, input_css_selector)
            inputBox.send_keys(types[type])
            time.sleep(1.5)

        inputBox.send_keys(Keys.RETURN)
    except ValueError:
        print("Write Correct ID or Password")

username = getpass.getpass("Input ID : ")       # User ID
password = getpass.getpass("Input Password : ") # User Password

login_input_send_keys(username, password)

# 4 Move to Target Post
# target_url = "https://www.instagram.com/p/B_6ThCKHP4I/"
# driver.get(target_url)


# 5 Load All Comments

## Click "comments load button" until comments have all loaded
# moreCommentLoadBtnCssSelector = "li button.wpO6b"
# moreCommentLoadBtn = raw.find_element("By.CSS_SELECTOR", moreCommentLoadBtnCssSelector)
# moreCommentLoadBtn.click()
# for i in range(999) :
#     try :
#         moreCommentLoadBtn = raw.find_element("By.CSS_SELECTOR", moreCommentLoadBtnCssSelector)
#         moreCommentLoadBtn.click()
#         driver.implicitly_wait(5)
#         print("Click Count : ", i + 1)
#     except :
#         print("Complete Loading All Comments")
#         break

# # 4 Load All Replies
# moreCommentLoadBtn = driver.find_elements("By.CSS_SELECTOR", "div.Igw0E > button.sqdOP.yWX7d,y3zJF")

# for i in range(999) :
#     try:
#         more_box = moreCommentLoadBtn[i].find_element("By.CSS_SELECTOR", "span.EizgU").text
#         count = int(more_box[-3])
#         if count >= 9 :
#             moreCommentLoadBtn[i].click()
#             time.sleep(0.15)
#             moreCommentLoadBtn[i].click()
#             time.sleep(0.15)
#             moreCommentLoadBtn[i].click()
#             time.sleep(0.15)
#         elif count >= 4 :
#             moreCommentLoadBtn[i].click()
#             time.sleep(0.15)
#             moreCommentLoadBtn[i].click()
#             time.sleep(0.15)
#         else :
#             moreCommentLoadBtn[i].click()
#             time.sleep(0.15)
#         print("Click Count", i + 1)
#     except:
#         print("Complete Loading All Replies")
#         break

# # 댓글 더 보기 : div.Igw0E.IwRSH.YBx95._4EzTm.MGdpg button.dCJp8.afkep (1번 누를 때마다 12개씩 추가됨)
# # 답글 보기 : div.Igw0E > button.sqdOP.yWX7d,y3zJF
#  ## 답글 갯수 : span.EizgU
# # 댓글 컨테이너 : ul.Mr508 div.C4VMK
#  ## 작성자 이름 : a.sqdOP
#  ## 댓글 내용 : span

# # 5 20학번 중 정답자 아이디 수집 (학번 없으면 수집X)
# driver.implicitly_wait(3)
# containers = driver.find_elements("By.CSS_SELECTOR", "ul.Mr508 div.C4VMK")
# comments = driver.find_elements("By.CSS_SELECTOR", "ul.Mr508 div.C4VMK span")
# award_dic = {}

# ##  댓글 반복 수집
# id_count = 0

# for i in containers :
#     comment = i.find_element("By.CSS_SELECTOR", "span")
#     try :
#         std_id = comment.text
#         if "6020" and ("8개" or "8새") in std_id :
#             account = i.find_element("By.CSS_SELECTOR", "a.sqdOP").text
#             print(account, "/ 학번 있음 / 정답 O /", std_id)
#             idx = std_id.index("6020")
#             id_num = std_id[idx:idx+8]
#             print("학번", id_num)
#             id_count += 1
#             award_dic[account] = id_num
#     except :
#         print("오류 발생")

# print("="*20)
# print("총 댓글 개수 : ", len(comments))
# print("정답 및 학번 포함 댓글 수 : ", id_count)
# print("오답 및 학번 없는 댓글 수 : ", len(comments)-id_count)
# print("="*20)
# print("정답자 아이디 명단")
# print(award_dic)
# print("정답자 : 총",len(award_dic),"명")
# print("="*20)

# # 7 당첨자 랜덤 추출
# award = []

# print("치킨 당첨자 : ")
# while len(award) != 3 :
#     pick = account, id_num = r.choice(list(award_dic.items()))
#     if ( pick not in award) :
#         award.append(pick)
#         print(account, id_num, sep="/")
# print("="*20)

# print("베라 당첨자 : ")
# while len(award) != 8 :
#     pick = account, id_num = r.choice(list(award_dic.items()))
#     if ( pick not in award) :
#         award.append(pick)
#         print(account, id_num, sep=" / ")
# print("="*20)

# print("스벅 당첨자 : ")
# while len(award) != 15 :
#     pick = account, id_num = r.choice(list(award_dic.items()))
#     if ( pick not in award) :
#         award.append(pick)
#         print(account, id_num, sep=" / ")

# print("="*20)
# print("명지내일 성년의 날 이벤트에 참여해주셔서 감사합니다. 다음에 더 좋은 이벤트로 찾아뵙겠습니다. ")

# # 8 크롬 창 닫기
# driver.close()