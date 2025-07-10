from shapely import reverse


str=["Able was I ere I saw Elba", "level", "madam", "rotor", "anna", "annaa"]

for ted in str:
    ted = ted.strip().lower().replace(" ", "")
    
    x = len(ted)
    y = x//2


    if x%2 == 0:
        temp1 = ted[0:y]
        temp2 = ted[y:][::-1]
        
        if temp1 == temp2:
            print("panlindrome")
        else:
            print("not panlindrome")
    else:
        temp1 = ted[0:y]
        temp2 = ted[y+1:x][::-1]

        if temp1 == temp2:
            print("panlindrome")
        else:
            print("not panlindrome")



ted = "00010"
print(ted[::-1])
tim = []
jane=list(map(int, (i for i in ted)))
print(jane)
for i in jane:
   tim.append(i) 

print(tim)