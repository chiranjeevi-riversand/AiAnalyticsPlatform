from abc import ABC, abstractmethod


class AbstractServiceBase(ABC):

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def tune(self):
        pass

    @abstractmethod
    def predict(self, payload):
        pass

    @abstractmethod
    def pre_process(self, payload):
        pass

    @abstractmethod
    def post_process(self, payload):
        pass