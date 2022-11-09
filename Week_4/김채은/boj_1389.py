from collections import deque

def game(user):

    dq = deque([user])
    count = [int(1e9) for _ in range(n+1)]
    count[user] = 0

    while dq:
        u = dq.popleft()

        for v in relations[u]:
            if count[v] > count[u] + 1:
                count[v] = count[u] + 1
                dq.append(v)
    
    return sum(count[1:])
   


if __name__ == "__main__":
    n, m = map(int, input().split())

    relations = [[] for _ in range(n+1)]

    for _ in range(m):
        user_a, user_b = map(int, input().split())

        relations[user_a].append(user_b)
        relations[user_b].append(user_a)

    kevin = []

    for user in range(1, n+1):
        kevin.append(game(user))
    
    print(kevin.index(min(kevin)) + 1)
