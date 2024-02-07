############ LOOPS ###############

########### IF-Else ##############
a=int(input("Enter a number: "))
if(a<18):
    print("You're not elligible to vote.")
elif(a==18):
    print("Yes you can vote.")
else:
    print("You're eligible to vote.")

################# WHILE LOOP ###############
n=10
i=1
while(i<n):
    print(i)
    i=i+1
else:
    print("It's executed")

############## BREAK #####################
n=10
i=1
while(i<n):
    print(i)
    i=i+1
    if(i==2):
        print("Yes it's there.")
        break
else:
    print("It's executed.")

########### CONTINUE #########
n=10
i=1
while(i<n):
    print(i)
    i=i+1
    if(i==2):
        print("Yes it's there.")
        continue
    print(i)
else:
    print("It's executed.")

########### FOR LOOP #############
a="Shally_Nagfase"
for i in a:
    print(i)

l=["shally",2,3,4,6+9j,3.4,True]
for i in l:
    print(i)
    if(i==6+9j):
        print(i)
        break
else:
    print("Executed")


######################
for i in range(0,10):
    print(i)

