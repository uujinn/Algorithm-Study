cocktails = list(map(int, input().split(' ')))

taste = 1

for cocktail in cocktails:
    if cocktail % 2 != 0:
        taste *= cocktail

if ((cocktails[0] * cocktails[1] * cocktails[2]) % 2 != 0) or (cocktails[0] % 2 == 0 and cocktails[1] % 2 == 0 and cocktails[2] % 2 == 0):
    print(cocktails[0] * cocktails[1] * cocktails[2])
else:
    print(taste)
