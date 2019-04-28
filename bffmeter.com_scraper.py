#!/bin/usr/env python3
import requests
from bs4 import BeautifulSoup

url = "https://bestbuddymeter.com/bff/quiz/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

with open('OP_database.txt', 'r', encoding='utf-8') as f:
    for lines in f:
        questionNo = lines.strip().split(",")[0]

print("Scraping resuming from quiz no: {}".format(questionNo))

#Program runs inside this infinite loop.
x=1
while x<2:

	question_url = url + str(questionNo)	
	response = requests.get(question_url, headers = headers)
	soup = BeautifulSoup(response.text, 'lxml')

	# Check whether the page loads correctly.
	if response.status_code == 200 and str(soup.title).startswith("Best Friend Meter with", 7):
		op_name = str(soup.title)[30:-8]
		#In some pages, OP hasn't selected any answers. This skips those pages.
		op_ans_counter = 0
		#Parsing the answers OP chose (correct answers)
		for i, correct_ans in enumerate(soup.find_all('td', class_="answer center correct")):
			i += 1
			op_ans_counter += 1 #T skipp possible errors.
			if i == 1:
				ans1 = correct_ans.text.strip()
			elif i == 2:
				ans2 = correct_ans.text.strip()
			elif i == 3:
				ans3 = correct_ans.text.strip()
			elif i == 4:
				ans4 = correct_ans.text.strip()
			elif i == 5:
				ans5 = correct_ans.text.strip()
			elif i == 6:
				ans6 = correct_ans.text.strip()
			elif i == 7:
				ans7 = correct_ans.text.strip()
			elif i == 8:
				ans8 = correct_ans.text.strip()
			elif i == 9:
				ans9 = correct_ans.text.strip()
			elif i == 10:
				ans10 = correct_ans.text.strip()

		if op_ans_counter == 10:
			#Writing the data to the file
			with open('OP_database.txt', 'a', encoding='utf-8') as OP_database:
				op_data = "{},{},{},{},{},{},{},{},{},{},{},{}\n".format(questionNo, op_name, ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10)
				OP_database.write(op_data)

			#Find the user scoreboard.
			tbody = soup.find('tbody')

			#Check whether someone has answered the quiz.
			if tbody.tr.td.text !="":

				for users, score, link in zip(tbody.find_all('td', class_="center"), tbody.find_all('td', class_="score"), tbody.find_all('a', href=True)):
					answer_url = "https://bestbuddymeter.com/bff/quiz_ans/{}".format(link['href'].split("/")[2])
					answer_response = requests.get(answer_url, headers=headers)
					answers_soup = BeautifulSoup(answer_response.text, 'lxml')
					
					usr_ans1=""
					usr_ans2=""
					usr_ans3=""
					usr_ans4=""
					usr_ans5=""
					usr_ans6=""
					usr_ans7=""
					usr_ans8=""
					usr_ans9=""
					usr_ans10=""

					for i, user_ans in enumerate(answers_soup.find_all('tr')):
						i += 1
						if i%2 == 0:
							if i == 2:
								usr_ans1 = user_ans.text.strip()
							elif i == 4:
								usr_ans2 = user_ans.text.strip()
							elif i == 6:
								usr_ans3 = user_ans.text.strip()
							elif i == 8:
								usr_ans4 = user_ans.text.strip()
							elif i == 10:
								usr_ans5 = user_ans.text.strip()
							elif i == 12:
								usr_ans6 = user_ans.text.strip()
							elif i == 14:
								usr_ans7 = user_ans.text.strip()
							elif i == 16:
								usr_ans8 = user_ans.text.strip()
							elif i == 18:
								usr_ans9 = user_ans.text.strip()
							elif i == 20:
								usr_ans10 = user_ans.text.strip()

					
					with open('user_answers.txt', 'a', encoding='utf-8') as user_append:
						user_data = "{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(questionNo,link['href'].split("/")[2],users.text.strip(),score.text.strip(),usr_ans1,usr_ans2,usr_ans3,usr_ans4,usr_ans5,usr_ans6,usr_ans7,usr_ans8,usr_ans9,usr_ans10)
						user_append.write(user_data)
			else:
				user_data_null = "{}".format(questionNo) + ",nil"*13 +"\n"
				with open('user_answers.txt', 'a',encoding='utf-8') as user_append:
					user_append.write(user_data_null)
		else:
			continue

		#Increment the quiz counter.
		questionNo = int(questionNo) + 1

	elif response.status_code == 200 and not str(soup.title).startswith("Best Friend Meter with", 7):
		print("No more pages left to scrape. \n Last scraped question mumber: {}".format(questionNo))
		break

	elif response.status_code != 200:
		print(" Something went horribly wrong! \n Error code: {}".format(response.status_code))
		break