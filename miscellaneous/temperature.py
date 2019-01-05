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

'''
(base) :~/Documents/PluralSight/PythonFundamentals/PracticeAgain$ python temperature.py

min =   2.0,            max =  13.0,            average =   9.0
min =   2.0,            max =  14.0,            average =  10.0
min =   3.0,            max =  15.0,            average =  10.7
min =   7.0,            max =  15.0,            average =  12.0
min =   9.0,            max =  17.0,            average =  14.0
min =  10.0,            max =  21.0,            average =  17.0
min =  11.0,            max =  22.0,            average =  18.0
min =  12.0,            max =  22.0,            average =  18.7
min =  10.0,            max =  23.0,            average =  18.3
min =   9.0,            max =  22.0,            average =  17.3
min =   8.0,            max =  20.0,            average =  15.7
min =   8.0,            max =  18.0,            average =  14.3

All days are above zero degree?
True

Any day above 28 degree?
False

'''  
    
