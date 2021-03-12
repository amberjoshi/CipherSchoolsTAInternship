spaces=5
stars=1
i=1
while i<=5:
  while spaces!=1: 
    print(" ",end="")
    spaces-=1;
  while stars!=i+1: 
    print("*",end="")
    stars+=1;
  spaces=5-i
  stars=1
  i+=1
  print()

first="A"
next="A"
for i in range(0,6):
  for j in range(0,i):
    print(next,end="")
    next=chr(ord(next)+1)
    j+=1
  print()
  i+=1 

