string=input("Enter the string :")
freq={}
for x in string:
  if x in freq:
    freq[x]=freq[x]+1
  else :
    freq[x]=1
print(freq)
