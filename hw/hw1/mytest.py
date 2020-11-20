from main import fibo, root_5, prime, seek_unique, find_names

for i in range(1,11):
    print(fibo(i))

for i in range(10):
    print(root_5(i))

for i in range(1,6):
    print(prime(i))

t = [1,1,1,3,3,2,5,6,4,8,8,5,9,9,9,5,10,46]
print(seek_unique(t))

s = ['aaa','bbb','ccc','abc']
n = 'alice'
print(find_names(s,n))