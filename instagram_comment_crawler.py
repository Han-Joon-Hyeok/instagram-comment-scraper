import getpass

from driver import ChromeDriver
# from RandomPicker import RandomPicker

# 1 Auto Download Chrome Webdriver (Corresponding to Chrome Browser Installed)
driver = ChromeDriver()

# 2 Move to Instagram Login Page
driver.move_to_login_page()

# 3 Login Instagram Account
username = input(str("Input ID : "))            # User ID
password = getpass.getpass("Input Password : ") # User Password

driver.login_to_instagram(username, password)

# 4 Move to Target Post
target_url = "https://www.instagram.com/p/B_6ThCKHP4I/"
driver.get(target_url)

# 5 Load All Comments
# Click "comments load button" until all comments have loaded
driver.load_all_comments()

# 6 Load All Replies
driver.load_all_replies()

# 7 Collect All Comments Writers and Contents
driver.collect_comments()

# 8 Check answer and student ID which is eligible for participate in the event.
driver.filter_comments()

# 9 Pick Random Winners
# data = driver.answer_list


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