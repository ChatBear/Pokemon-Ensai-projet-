from abc import ABC, abstractmethod


class AbstractView(ABC):
    def __init__(self, session):
        self._session = session

    def display_info(self):
        with open('assets/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    @abstractmethod
    def make_choice(self):
        pass
