import re
#print('\tTab')
#print(r'\tTab')


#text_to_search="""
#abcdefghijklmnopqrstuvwxyz
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#1234567890"""

#MetaCharacters (needs to be escaped):
#.!@+$%^&*(){}[]

#coreyms.com


#pattern = re.compile(r'\.')
#matches = pattern.finditer(text_to_search)
#for match in matches:
#    print(match)

#xx= "hello world, is very fun"
#r1=re.findall(r"^\w+",xx)
#print(r1)


#print((re.split(r'\s',"hello world, is very fun")))


#abc='helloworld@google.com,www.google.com,www.facbook.com'
#emails = re.findall(r'[\w\.-]+@[\w\.-]+',abc)
#for email in emails:
#    print (email)


#a="welcome to hello world"
#x=re.findall("[a-e]",a)
#print(x)

#print((re.split(r's','splits words')))

list = ["hello world","hai kumar","ram raju","kiran kiran","kumar kumar"]
for element in list:
    z= re.match("(k\w+)\W(k\w+)" ,element)
    if z:
        print ((z.groups()))

