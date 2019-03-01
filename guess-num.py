import random
r =random.randint(1, 10)

while True:
	g = input('1～10 猜一個數字：')
	g = int(g)
	if g == r:
		print('恭喜猜對數字了')
		break
	elif g > r:
		print('比答案大')
	elif g < r:
		print('比答案小')