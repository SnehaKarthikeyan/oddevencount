Coding:
  
x=int(input())
count=0
count1=0
i=0
for j in range(1,x+1):
    if j%2==0:
      count=count+1
    else:
      count1=count1+1
print(count1,end=" ")   
print(count) 
