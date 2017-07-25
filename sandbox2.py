
a= input ("number1")
b = input ("number2")
print a + b


a = input ( "your name is ")
print (a + " " + "is a pig")


a = ['aaa','c','dddd','rr']
b= len(a[0])




print b


a = ['aaa','c','dddd','rr']
sorted (a, key=len)

print a


def last(s):
    return s[-1]



s= "hello"
print s, last(s)


def first(s):
    return s[0:2]

print s + " - " + first(s)

help(sorted)

a = ['aaa','t','dddd','rr']
sorted(a)

print sorted(a), a




def newkey(s):
    return s[1]

a= [('a',100),('b',93),('c',55)]
#a.sort(a,key=newkey)

print(sorted(a, key=newkey))


def newkey(s):
    return s[1]

a= ['100','93', '55']
#a.sort(a,key=newkey)

print(sorted(a, key=newkey))

a= 100
print(str(a)[1])

print (50 - 5*6) / 4


i = 256*256
print('The value of i is ', i, 10, 78, "di")

a, b = 1,1
while b <10:
    print(b, end=' ')
    a, b = a, b+a

print()
print (50 - 5*6) / 4




i=1
while i<5:
    print i,
    i = i + 1
print()

"""
words = ['zat', 'aindow', 'fefenestrate']



for a in words[:]:
    if len(a) < 8:
        words.insert(0,a)

print words
print sorted( words)

def newkey(s):
    return s [1]

print sorted(words, key=newkey)

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print i, a[i]
print

print 'ab\nm'

def one():
    return 'hey'

def two() :
    print 'heyp'

print 'hello'+ one()
two()



'''
'''
def bigger(a, b):
    if a > b:
        return a
    elif a <b:
        return b
    else:
        return a


print bigger(1,3)


def bigger(a, b):
    if a > b:
        return a
    elif a <b:
        print b
    else:
        print a


bigger(1,3)


def ret(n):
    if n > 9:
         temp = "two digits"
         return temp     #Line 4
    else :
         temp = "one digit"
         return temp     #Line 8
    return     #Line 9
    print ("return statement")
print ret(10)


''

a= ['blue','hey','you']
print a.join(' ')
