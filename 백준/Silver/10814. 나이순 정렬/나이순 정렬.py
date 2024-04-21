T = int(input())
people = []
for _ in range(T):
    age, name = input().split()
    people.append((int(age), name))

result = sorted(people, key=lambda x : x[0])

for i in range(T):
    print(result[i][0], result[i][1])