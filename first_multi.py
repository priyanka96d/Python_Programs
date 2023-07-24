
import time

start = time.perf_counter()
class makePizaa ():
    def run(self):
            print("Making Pizza")
            time.sleep(3)
            print("Pizza is ready")

class eatPizza():
    def run(self):
            print("Eating Pizza")
            time.sleep(1)
            print("Done eating")



t1 = makePizaa()
t2 = eatPizza()

t1.run()
t2.run()
finish = time.perf_counter()
print(f'finished in {round(finish-start,2)} seconds' )
