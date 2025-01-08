from abc import ABC, abstractmethod

class Block(ABC):
    @abstractmethod
    def computeHash(self):
        pass