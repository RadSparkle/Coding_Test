n,x = map(int,input().split())
num_list = list(map(int,input().split(' ')))
result = []

for i in num_list :
   if x > i :
      result.append(i)

for k in result :
   print(k,end=' ')