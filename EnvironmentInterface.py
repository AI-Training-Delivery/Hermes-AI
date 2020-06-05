import abc

class EnvironmentInterface(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def initialize(self):
        pass
    
    @abc.abstractmethod
    def giveData(self, data):
        pass

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def result(self):
        pass

    @abc.abstractmethod
    def checkID(self, id):
        pass
    