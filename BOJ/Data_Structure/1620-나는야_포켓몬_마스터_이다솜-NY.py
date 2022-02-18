from sys import stdin
N, M = map(int, stdin.readline().split())
pokemons = {}
for i in range(N):
    new_pokemon = str(stdin.readline().rstrip())
    pokemons[new_pokemon] = i+1
    pokemons[str(i+1)] = new_pokemon

for _ in range(M):
    searching = str(stdin.readline().rstrip())
    print(pokemons[searching])