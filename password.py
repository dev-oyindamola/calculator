import random as ra

num = "0123456789"


all_pass =list(num)

def genarate_password():
	ra.shuffle(all_pass)
	password = []

	for i in range(7):
		password.append(ra.choice(all_pass))
		# rand_pass_len = len(rand_pass)
		# rand_word = ra.randint(0, rand_pass_len-1)

		# password += rand_pass[ra.randint(0, rand_word)]
	ra.shuffle(password)

	return "".join(password)

# print(genarate_password())	