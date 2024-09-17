#Store sates and capital in respective arrays
#'Goa Panjim' 'Andhra Amarvati' 'Kerala Tiruvanantapuram' 'Himachal Shimla'

import sys

states = []
capitals = []
input = sys.argv[1:]
for i in range (0,len(input)):
    parts = input[i].split()
    states.append(parts[0])
    capitals.append(parts[1])
print(states)
print(capitals)