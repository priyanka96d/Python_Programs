from threading import Thread


class makePizza(Thread):
    def run(self):
        for i in range(5):
            print("Pizza is ready")

class eatPizza(Thread):
    def run(self):
        for i in range(5):
            print("Eating the Pizza")



t1 = makePizza()
t2 = eatPizza()

t1.start()
t2.start()


