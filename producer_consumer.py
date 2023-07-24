import time, random
from threading import Thread,  currentThread, Condition
from queue import Queue

class SharedCell():
    """Shared data that sequences writing before reading."""
    
    def __init__(self):
        """Can produce but not consume at startup."""
        self.tasks = Queue(5)
        self.writeable = True
        self.condition = Condition()

    def setData(self, data):
        """Second caller must wait until someone has
        consumed the data before resetting it."""
        self.condition.acquire()
        while not self.writeable:
            self.condition.wait()
        print("%s setting data to %d" % \
              (currentThread().getName(), data))
        self.tasks.put(data)
        self.writeable = False
        self.condition.notify()
        self.condition.release()

    def getData(self):
        """Caller must wait until someone has produced
        the data before accessing it."""
        self.condition.acquire()
        while self.writeable:
            self.condition.wait()
        value = self.tasks.get()
        print("%s accessing data %d" % \
              (currentThread().getName(), value))
        self.writeable = True
        self.condition.notify()
        self.condition.release()
        return value

class Producer(Thread):
    """A producer of data in a shared cell."""

    def __init__(self, cell, accessCount, sleepInterval):
        Thread.__init__(self, name = "Producer")
        self.accessCount = accessCount
        self.cell = cell
        self.sleepInterval = sleepInterval

    def run(self):
        """Resets the data in the cell and goes to sleep,
        the given number of times."""
        print("%s starting up" % self.getName())
        for count in range(self.accessCount):
            time.sleep(random.randint(1, self.sleepInterval))
            self.cell.setData(count + 1)
        print("%s is done producing\n" % self.getName())

class Consumer(Thread):
    """A consumer of data in a shared cell."""

    def __init__(self, cell, accessCount, sleepInterval):
        Thread.__init__(self, name = "Consumer")
        self.accessCount = accessCount
        self.cell = cell
        self.sleepInterval = sleepInterval

    def run(self):
        """Accesses the data in the cell and goes to sleep,
        the given number of times."""
        print("%s starting up\n" % self.getName())
        for count in range(self.accessCount):
            time.sleep(random.randint(1, self.sleepInterval))
            value = self.cell.getData()
        print("%s is done consuming\n" % self.getName())

def main():
    accessCount = int(input("Enter the number of accesses: "))
    cell = SharedCell()
    p = Producer(cell, accessCount, 4)
    c = Consumer(cell, accessCount, 4)
    print("Starting the threads")
    p.start()
    c.start()

if __name__ == "__main__":
    main()