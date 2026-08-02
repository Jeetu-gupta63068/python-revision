class car:
    def __init__(self):
        self.accelelator = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.cluth = True
        self.accelator = True
        print("car started..")
        
car1=car()
car.start()