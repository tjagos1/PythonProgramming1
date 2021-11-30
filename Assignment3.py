
arr_2d =[['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in arr_2d:
    for j in i:
        print(j,end=" ")
    print()




n = int(input("Enter 1 for heads or 0 for tails :"))

import random
a=random.randint(0,1)

if n == a:
    print("Congratulations you won!")
else:
    print("The computer wins")