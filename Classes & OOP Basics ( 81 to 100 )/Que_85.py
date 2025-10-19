def add(self, count):
    self.namazi += count
    print(self.namazi)

def reset(self,count):
    if count > self.namazi:
        print("Namazi count cannot be negative")
    self.namazi -= count
    print(self.namazi)


    