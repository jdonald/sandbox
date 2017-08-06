
a= ['blue','hey','you']
#print "\n".join(a)


def printlist(a):
    for i in range(len(a)):
        print a[i],




a=[12,23,3,4]
printlist(a)


x = [4, 5, 9]
y = "Hello"
print(type(x), type(y))
#help(type)

class a(object):
    pass
x = a()
print(type(x))


a = ['hello','hey','sun']
b = ' '.join(a)
print b

for i in range(len(a)):
    print a[i],


print

class enployment():
    def __init__(self,first,last,payrole):
        self.firstname=first
        self.lastname=last
        self.email=first+"."+last+'@gmail.com'
        self.pay=payrole
        print last +'test'

    def fullname(self):
        print self.firstname + ' ' +self.lastname

    def payraise(self,raiseamount):
        self.raiseamount = raiseamount
        self.pay = self.pay* raiseamount

a = enployment('james','donald',6000)

print  a.email

print a.lastname
print a.fullname()
print
enployment.fullname(a)
a.fullname()
print
print a.lastname
print
print a.pay

enployment.raiseamount = 1.1
a.raiseamount = 1.2
print a.pay
a.payraise(2)
print a.pay

print '***************************'

#def square(a):
#    return a*a
#
#
# f = square(2)
# #print square()
# print square
