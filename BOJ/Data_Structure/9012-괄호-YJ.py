from sys import stdin

def vps(string):

    while len(string) != 0:

        if (string[0] == ')' or string[len(string)-1] == '('):
            print("NO")
            break

        else:
            if '(' and ')' in string:
                string.remove('(')
                string.remove(')')
            
            else:
                print('NO')
                break

    if len(string) == 0:
        print("YES")


N = int(stdin.readline())

for _ in range(N):
    string = list(stdin.readline().rstrip())
    vps(string)