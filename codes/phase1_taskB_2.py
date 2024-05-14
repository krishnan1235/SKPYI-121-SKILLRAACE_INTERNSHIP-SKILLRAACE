name1=input("Enter the name1:").lower().replace(" ","")
name2=input("Enter the name2:").lower().replace(" ","")
l1=list(name1)
l2=list(name2)
f=['Friend','Love','Affection','Marriage','Enemy','Siblings']
k=l1+l2
for i in k:
    if i in l1 and i in l2:
        l1.remove(i)
        l2.remove(i)
n=len(l1)+len(l2)
while len(f)>1:
    index=(n% len(f))-1
    if index>=0:
        f=f[index + 1:] + f[:index]
    else:
        f=f[:len(f) - 1]
print("The relation between the name1 and name2 is:",f[0])
