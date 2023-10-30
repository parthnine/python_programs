import re
	

input_str = "Hey, did you know that the summer break is coming? Amazing right !! It's only 5 more days"
text_lowercase = input_str.lower()
print(text_lowercase)

input_str1 = "There are 3 balls in this bag, and 12 in the other one."
remove_number = re.sub(r'\d+', '', input_str1)
print(remove_number)

