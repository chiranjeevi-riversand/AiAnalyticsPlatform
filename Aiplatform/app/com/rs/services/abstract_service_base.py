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

    @abstractmethod
    def load_model(self, payload):
        pass

    @abstractmethod
    def pre_process_data(self, payload):
        pass

    @abstractmethod
    def post_process_data(self, payload):
        pass