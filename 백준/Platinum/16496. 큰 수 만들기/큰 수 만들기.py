import sys
input = sys.stdin.readline

n = int(input())

l = input().split()
q = max(map(lambda x : len(x), l))

# l.sort(key= lambda x : int(x.ljust(q, '0')), reverse=True)
l.sort(key= lambda x : x.ljust(q, '0'), reverse=True)

ans = ""
for x in l:
    ans = max(x+ans,ans+x)
if int(ans) == 0:
    print(0)
else:
    print(ans)
