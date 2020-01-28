num=input("enter a number")
a=" ".join(num)
if '.' in a:
    print("enter integers only")
else:
    n=a.split(" ")
    sum=0
    for i in n:
      i=int(i)
      sum=sum+(i*i*i)
    if(sum==int(num)):
       print("Amstrong number")
    else:
       print("not an amstrong number")