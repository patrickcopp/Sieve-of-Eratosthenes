#initialize list
high=1000
values=list(range(high))

#sieve
for i in range (2,high):
    if values[i]==0:
        continue
    else:
        counter=2
        while counter*i<high:
            values[counter*i]=0
            counter+=1
print(sum(values)-1)
            
