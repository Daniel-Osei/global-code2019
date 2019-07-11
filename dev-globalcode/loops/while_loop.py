#first trial
print ("printing from 1 - 10 with while")

i = 0
while(i < 10):
    i = i + 1
    print (i)

input("press enter to continue")
#try printing numbers from 7 - 19
print ("print from 7 - 19")

j = 6
while(j < 19):
    j = j + 1
    print (j)

input("press enter to continue")

#print even numbers between 12 and 20
print ("print even numbers between 12 and 20 ")

k = 12
while(k < 18):
    k = k + 2
    print (k)

input("press enter to continue")

#take two numbers from user and give even numbers between them


def even():
    start = int(input("Enter the lower limit: "))
    end = int(input("Enter the upper limit: "))
    for num in range(start, end + 1):
        if num % 2 == 0:
            print (num)

even()

def reverse_even():
    start = int(input("Enter the lower limit: "))
    end = int(input("Enter the upper limit: "))
    for num in range(end, start - 1, -1):
        if num % 2 == 0:
            print (num)

reverse_even()
