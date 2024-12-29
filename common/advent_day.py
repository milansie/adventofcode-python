import inspect
import os
import time
from abc import abstractmethod
from pathlib import Path


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

        input_test_1 = self._load_input("1_input.txt")
        result_test_1 = "\n".join(self._load_input("1_result.txt"))

        # first with testing data
        self.IN_TEST = True
        start_time = time.perf_counter()
        first_test_result = self.first(input_test_1)

        consumed_time = int((time.perf_counter() - start_time) * 1000)
        if first_test_result != result_test_1:
            self._log(f"ERROR First test failed: expected '{result_test_1}', but was '{first_test_result}' in {consumed_time} ms")
        else:
            self._log(f"First test passed: expected '{result_test_1}', was '{first_test_result}' in {consumed_time} ms")

        # first with production data
        self.IN_TEST = False
        input_data = self._load_input("input.txt")
        start_time = time.perf_counter()
        first_result = self.first(input_data)
        consumed_time = int((time.perf_counter() - start_time) * 1000)
        self._log(f"First result: {first_result} in {consumed_time} ms")

        # second with testing data
        self.IN_TEST = True
        input_test_2 = self._load_input("2_input.txt")
        result_test_2 = "\n".join(self._load_input("2_result.txt"))

        start_time = time.perf_counter()
        second_test_result = self.second(input_test_2)
        consumed_time = int((time.perf_counter() - start_time) * 1000)
        if second_test_result != result_test_2:
            self._log(f"ERROR Second test failed: expected '{result_test_2}', but was '{second_test_result}' in {consumed_time} ms")
        else:
            self._log(f"Second test passed: expected '{result_test_2}', was '{second_test_result}' in {consumed_time} ms")

        # second with production data
        self.IN_TEST = False
        start_time = time.perf_counter()
        second_result = self.second(input_data)
        self._log(f"Second result: {second_result} in {int((time.perf_counter() - start_time) * 1000)} ms")

        print("---------------------------------------")
        print('\n'.join(self.log_lines))
        print("---------------------------------------")

    def _load_input(self, filename: str) -> list[str]:
        current_file = Path(inspect.getmodule(self).__file__)
        root_dir = current_file.parent.parent.parent
        path = root_dir / "resources" / f"y{self.year}" / f"d{self.day}" / filename


        with open(path, "r") as f:
            return f.readlines()

