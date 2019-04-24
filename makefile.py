#!/bin/usr/env python3


#Make counter file.
with open('counter.txt', 'w', encoding='utf-8') as fcounter:
	counter_data = 1000
	counter_data = str(counter_data)
	fcounter.write(counter_data)

#Make op database.
with open('OP_database.txt', 'w', encoding='utf-8') as fop:
	op_data = "questionNo,OP_name,correct_ans1,correct_ans2,correct_ans3,correct_ans4,correct_ans5,correct_ans6,correct_ans7,correct_ans8,correct_ans9,correct_ans10"
	fop.write(op_data)

#Make user database.
with open('user_answers.txt', 'w', encoding='utf-8') as fuser:
	user_data = "questionNo,answerNo,user_name,user_score,usr_ans1,usr_ans2,usr_ans3,usr_ans4,usr_ans5,usr_ans6,usr_ans7,usr_ans8,usr_ans9,usr_ans10"
	fuser.write(user_data)

print("Files created successfully!")

