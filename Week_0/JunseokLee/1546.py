N=int(input())
score = list(map(int, input().split()))
print(100*sum(score)/(N*max(score)))