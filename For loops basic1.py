
for i in range(0, 150):
    print(i)
for i in range(0, 1000, 5):
    print(i)
for i in range(0, 1000, 5):
    print(i)
    
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(0, 1000, 1):
    if(i%10==0):
        print("Coding Dojo")
    elif(i%5==0):
        print("Dojo")
    else:
        print(i)
        
sum =0 
for i in range(0,500000):
    if(i%2==1):
        sum+=i

print("Sum: ",sum)

#
for i in range(2018,0,-4):
    print(i)
    
def flexiblecounter(l,h,inc):
    for i in range(l,h,inc):
        print(i)
        
flexiblecounter(-42,75,2)

flexiblecounter(732,-9,-11)