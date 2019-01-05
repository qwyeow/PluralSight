from itertools import chain, islice
from generator import lucas

tuesday = [2,2,3,7,9,10,11,12,10,9,8,8]   
monday = [13,14,14,14,16,20,21,22,22,21,19,17]
sunday = [12,14,15,15,17,21,22,22,23,22,20,18]

for temps in zip(sunday,monday,tuesday):
    print(f"min = {min(temps):5.1f},\
            max = {max(temps):5.1f},\
            average = {(sum(temps)/len(temps)):5.1f}")


temperatures = chain(sunday,monday,tuesday)
print("All days are above zero degree?")
print(all( t>0 for t in temperatures))

print("Any day above 28 degree?")
print(any(t>28 for t in temperatures))


    