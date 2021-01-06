#我的方法
def suma():
	a = int(input('please input your want num:'))
	sum = 0
	for i in range(a+1):
		if i <= a:
			sum = sum + i
		i += 1
	print(sum)		
		
suma()


#习题集方法:		
def get_sum(num):
	if num >= 1:
		res = num + get_sum(num-1)
#		dulbsum = get_sum(num-1) + 1
	else:
		res = 0
#		dulbsum = 0
	return res
#	return dulbsum

dulres = get_sum(5)	
print(dulres)


#网路方法:
def sum_numbers(num):
	if num == 1:
		return 1
	temp = sum_numbers(num - 1)
	print('temp',temp)
	return temp + num
	
print(sum_numbers(5))
		