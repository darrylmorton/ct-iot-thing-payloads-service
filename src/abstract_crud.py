import abc

from schemas import ThingPayload


class CrudInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self.session = None
        pass

    @abc.abstractmethod
    def find_thing_payloads_by_timestamps(
        self, start_timestamp: int, end_timestamp: int
    ) -> list[ThingPayload]:
        pass
