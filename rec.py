print("Enter array elements")
arr=list(map(int,input().split()))
result=[]
def looping_arr(k):
	if k>0:
		n=k+looping_arr(k-1)
	else:
		n=0
	return n
	
for x in range(len(arr)) : 
	sum=0
	sum=looping_arr(arr[x])
	result.append(sum)
print(result,sep=",")

	
