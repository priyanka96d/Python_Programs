#sleep without join

from threading import Thread
import time

start = time.perf_counter()

class makePizza(Thread):
    def run(self):
        print("Making Pizza")
        time.sleep(3)
        print("Pizza is ready")

class eatPizza(Thread):
    def run(self):
        print("Eating Pizza")
        time.sleep(3)
        print("Done eating")



t1 = makePizza()
t2 = eatPizza()

t1.start()
t2.start()

finish = time.perf_counter()
print(f'finished in {round(finish-start,2)} seconds' )

