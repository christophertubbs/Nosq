import typing
import abc


class Backend(abc.ABC):
    @abc.abstractmethod
    def query(self, key: str) -> 