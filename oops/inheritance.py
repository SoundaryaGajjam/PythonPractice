class BMW:
    def __init__(self,mk,model,yr):
        self.make=mk
        self.model=model
        self.year=yr

    def start(self):
        print("starting the car")

    def stop(self):
        print("stoping the car")

class ThreeSeries(BMW):     #no extends keyword
    def __init__(self,cruiseControlEnabled,mk,model,yr):
        #BMW.__init__(self,mk,model,yr)  #calling base cls constructor
        super().__init__(mk,model,yr) #invoking parent cls constructor using super()
        self.cruiseControlEnabled = cruiseControlEnabled

#overriding
    def start(self):
        super().start() #invoking mthds of parent cls using super()
        print("button start")

    def display(self):
        print(self.cruiseControlEnabled)

class FiveSeries(BMW):     #no extends keyword
    def __init__(self,parkingAssistEnabled,mk,model,yr):
        BMW.__init__(self,mk,model,yr)  #calling base cls constructor
        self.parkingAssistEnabled=parkingAssistEnabled

threeSeries=ThreeSeries(True,"BMW",'328i',2018)
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make,threeSeries.model,threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()