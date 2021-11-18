n = int(input())
s = ''
h = '0123456789ABCDEF' 
while n > 0:
    s = h[n % 16] + s
    n = n // 16
print(s)
