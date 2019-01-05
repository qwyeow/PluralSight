"""
Build a context manager that will execute close() no matter if exception is raised

"""


import sys
from contextlib import closing 

class Fridge:
    
    def open(self):
        print("Opening fridge door")

    def raid(self, food):
        print(f"preparing to raid {food}")
        if food == "pizza":
            raise RuntimeError("This is unhealthy! Raid Denied.")
        print(f"Take {food} out of fridge")

    def close(self):
            print("Closing fridge door")


def main(food):
    f = Fridge()
    with closing(f) as r:  # context manager makes sure close() executed no matter what
        r.open()
        r.raid(food)                    

if __name__ == "__main__":
    main(sys.argv[1])


"""
$ python3 fridge.py apple
Opening fridge door
preparing to raid apple
Take apple out of fridge
Closing fridge door

$ python3 fridge.py milk
Opening fridge door
preparing to raid milk
Take milk out of fridge
Closing fridge door

$ python3 fridge.py pizza
Opening fridge door
preparing to raid pizza
Closing fridge door
Traceback (most recent call last):
  File "fridge.py", line 26, in <module>
    main(sys.argv[1])
  File "fridge.py", line 23, in main
    r.raid(food)
  File "fridge.py", line 12, in raid
    raise RuntimeError("This is unhealthy! Raid Denied.")
RuntimeError: This is unhealthy! Raid Denied.


"""
