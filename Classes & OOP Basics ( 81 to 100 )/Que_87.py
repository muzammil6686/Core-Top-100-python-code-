class Tasbeeh_Counter:
    def __init__(self,tasbeeh):
        self.tasbeeh = tasbeeh
        
    def add_count(self,count):
        self.tasbeeh += count
        print(self.tasbeeh)

    def reset_count(self,count):
        if self.tasbeeh > count:
            self.tasbeeh -= count
            print(self.tasbeeh)