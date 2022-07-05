# b1
# x,y,z,n = (int(input()) for _ in range (4))
# print ([[a,b,c] for a in range (0,x+1) for b in range (0,y+1) for c in range (0, z+1) if ((a+b+c) != n)] )

# b2 sorted
# n = int(input())
# arr = map(int, input().split())
#     # arr.append(n)
# print(sorted(list(set(arr)))[-2])

# B3 
# student = []
# for _ in range (int(input())):
#     name = input()
#     score = float(input())
#     student.append([name, score])
# score_sheet = sorted(set(score for name, score in student ))[1]
# print('\n'.join(sorted(name for name, score in student if score == score_sheet)))
