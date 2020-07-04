list1=[5,2,3,4,9,4,3,2,1,2,3,4,5,4,3,2,9]
"""for i in range(0,len(list1),4):
    for j in range(i,i+4,1):
        if (j <len(list1)):
            print (list1[j],end = '  ')
        else :
            print ("end")
            break
    print (" ")
"""
for i in range (0,len(list1),4):
    print ([ list1[x+i] for x in range (4) if x+i < len(list1) ])


#print(list4)