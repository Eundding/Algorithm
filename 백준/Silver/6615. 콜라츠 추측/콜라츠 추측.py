import sys
input = sys.stdin.readline
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    A = a
    B = b
    Sa, Sb = [A], [B]
    while True:
        if Sa[-1] in Sb:
            print("%d needs %d steps, %d needs %d steps, they meet at %d" %(a, len(Sa)-1, b, Sb.index(Sa[-1]), Sa[-1]))
            break
        if Sb[-1] in Sa:
            print("%d needs %d steps, %d needs %d steps, they meet at %d" % (a, Sa.index(Sb[-1]), b, len(Sb)-1, Sb[-1]))
            break
        if A != 1:
            if A % 2 == 0:
                A //= 2
                Sa.append(A)
            elif A % 2 == 1:
                A = A*3+1
                Sa.append(A)
        if B != 1:
            if B % 2 == 0:
                B //= 2
                Sb.append(B)
            elif B % 2 == 1:
                B = 3*B + 1
                Sb.append(B)


