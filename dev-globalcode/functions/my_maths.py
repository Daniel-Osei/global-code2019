def calculate( str, num1, num2 ):
	str = input("what do you want to do ? ")
	num1 = eval(input("the first number: "))
	num2 = eval(input("the second number: "))
	
	if op == add:
		sum = num1 + num2
		print ("the sum is : ", sum)


calculate(str, num1, num2)
