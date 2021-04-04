from typing import Set

from domain.cards import Card


class PythonFlaskTemplateApp:
    _name: str
    _description: str
    _cards: Set[Card]

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def cards(self) -> Set[Card]:
        return self._cards

    def __init__(self, *, name: str, description: str) -> None:
        self._name = name
        self._description = description
        self._cards = {
            Card(suite="hearts", value="10"),
            Card(suite="hearts", value="jack"),
            Card(suite="hearts", value="queen"),
            Card(suite="hearts", value="king"),
            Card(suite="hearts", value="ace"),
        }
