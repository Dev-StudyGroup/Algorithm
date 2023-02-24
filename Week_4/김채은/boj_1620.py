n, m = map(int, input().split())

pokemons_dict = dict()

for i in range(1, n+1):
    pokemon = input()
    index = str(i)
    pokemons_dict[index] = pokemon
    pokemons_dict[pokemon] = index

for _ in range(m):
    quiz = input()

    print(pokemons_dict[quiz])
    