from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

### functions ###

def login(id,pw) :
    id_box = driver.find_element_by_css_selector("input[name='id']")
    pw_box = driver.find_element_by_css_selector("input[name='pw']")
    id_box.send_keys(id)
    time.sleep(1)
    pw_box.send_keys(pw)
    time.sleep(1)

    pw_box.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)

    print("로그인 되었습니다.")

### functions ###

# 1 웹드라이버 켜기

driver = webdriver.Chrome("./chromedriver")

# 2 무신사 로그인 창 열기
raw = driver.get("https://my.musinsa.com/login/v1/login?referer=https%3A%2F%2Fstore.musinsa.com%2Fapp%2F/")
driver.implicitly_wait(5)

# 3 로그인 하기

login('enter your id','enter your pw')

# 4 마이 페이지로 이동하기
raw = driver.get("https://my.musinsa.com/member/v1/point")

# 5 현재 포인트 확인하기

points = driver.find_element_by_css_selector("strong#reminePoint").text
dates = driver.find_elements_by_css_selector("tr td:nth-of-type(3)")
date = dates[0].text

print("현재 포인트 : %s (%s 기준)" % (points,date) )

# 6 크롬 창 닫기
driver.close()