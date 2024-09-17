#Pefect square

import math
n = int(input("Enter a number: "))
if (math.sqrt(n)) * (math.sqrt(n)) == n:
    print("Perfect square")
else:
    print("Not perfect")
