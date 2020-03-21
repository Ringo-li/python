import os

def word_sum(word):
	sum = 0
	for letter in word:
		sum += ord(letter) - 96
	return sum
	
if os.path.exists('English-alphabet.txt'):		
	with open('English-alphabet.txt','r') as file:
		a = 0
		for word in file.readlines():	
			if a < 10:
				word = word.strip()
				if word_sum(word) == 100:		
					print(word,a)
					a += 1
else:
	print('file not exist')		
			

