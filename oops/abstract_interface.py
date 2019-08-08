from abc import abstractmethod, ABC


class BMW(ABC):
    def __init__(self,mk,model,yr):
        self.make=mk
        self.model=model
        self.year=yr

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):     #no extends keyword
    def __init__(self,cruiseControlEnabled,mk,model,yr):
        #BMW.__init__(self,mk,model,yr)  #calling base cls constructor
        super().__init__(mk,model,yr) #invoking parent cls constructor using super()
        self.cruiseControlEnabled = cruiseControlEnabled

    def start(self):
        super().start() #invoking mthds of parent cls using super()
        print("button start")

    def stop(self):
        super().stop() #invoking mthds of parent cls using super()
        print("button stop")

    def display(self):
        print(self.cruiseControlEnabled)

    def drive(self):
        print("Three series being driven")

class FiveSeries(BMW):     #no extends keyword
    def __init__(self,parkingAssistEnabled,mk,model,yr):
        BMW.__init__(self,mk,model,yr)  #calling base cls constructor
        self.parkingAssistEnabled=parkingAssistEnabled

    def drive(self):
        print("Five series being driven")

threeSeries=ThreeSeries(True,"BMW",'328i',2018)
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make,threeSeries.model,threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()
threeSeries.drive()