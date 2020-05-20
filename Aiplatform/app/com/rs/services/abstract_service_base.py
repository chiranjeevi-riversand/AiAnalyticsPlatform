from abc import ABC, abstractmethod


class AbstractServiceBase(ABC):
    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def tune(self):
        pass

    @abstractmethod
    def score(self, payload):
        pass