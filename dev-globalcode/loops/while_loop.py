#print 1 - 10
print ("print from 1 - 10")
i = 0

while(i < 10):
    i = i + 1
    print (i)


print ("printing from 7 -19")
#print from 7 - 19
a = 6

while(a < 19):
    a = a + 1
    print (a)
    

#print even numbers between 12 ans 20
print ("method 1")
j = 12
while j <20:
    print(j)
    j +=2

even_num = [x for x in range(13,20) if x % 2 == 0]
print (even_num)it