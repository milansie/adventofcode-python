import inspect
import os
from abc import abstractmethod


class AdventDay:

    IN_TEST = False

    def __init__(self):

        self.year = None
        self.day = None
        self.log_lines = []

        module_path = inspect.getmodule(self).__file__
        path_parts = os.path.normpath(module_path).split(os.sep)
        for part in path_parts:
            if part.startswith('y'):
                self.year = part[1:]
            elif part.startswith('d'):
                self.day = part[1:].split('.')[0]

    def _log(self, str):
        self.log_lines.append(str)

    def debug(self, str):
        if self.IN_TEST:
            self._log(str)

    @abstractmethod
    def first(self, lines: list[str]) -> str:
        pass

    @abstractmethod
    def second(self, lines: list[str]) -> str:
        pass

    def run(self):
        self._log(f"Running {self.year}.{self.day}")

        lines = self._load_input("input.txt")

        # first with testing data
        self.IN_TEST = True
        self.first(lines)

        # first with production data
        self.IN_TEST = False
        self.first(lines)

        # second with testing data
        self.IN_TEST = True
        self.second(lines)

        # second with production data
        self.IN_TEST = False
        self.second(lines)

        print("---------------------------------------")
        print('\n'.join(self.log_lines))
        print("---------------------------------------")

    def _load_input(self, filename: str) -> list[str]:
        path = f"resources/y{self.year}/d{self.day}/{filename}"

        with open(path, "r") as f:
            return f.readlines()

