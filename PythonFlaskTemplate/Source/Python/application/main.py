class PythonFlaskTemplateApp:
    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    def __init__(self, *, name: str, description: str) -> None:
        self._name = name
        self._description = description
