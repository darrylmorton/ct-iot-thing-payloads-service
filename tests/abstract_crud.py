import abc

from models import ThingPayloadModel


class CrudInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self.session = None
        pass

    @abc.abstractmethod
    async def insert_thing_payload(self, thing_payload: ThingPayloadModel) -> None:
        pass

    async def insert_thing_payloads(
        self, thing_payloads: list[ThingPayloadModel]
    ) -> None:
        pass
