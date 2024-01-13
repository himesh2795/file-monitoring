import random
import string
import threading
import time

from filename_enum import FileNameEnum


class RandomWriter:
    def __init__(self, interval: int, random_string_length: int = None):
        self.interval = interval
        self.random_string_length = random_string_length if random_string_length else random.randint(5, 10)

    def run_in_threading(self):
        threading.Thread(target=self._run).start()

    def _run(self):
        counter = 0
        while True:
            counter += 1
            print(f"Writing Randomly : {counter}")
            self.__write_file()
            time.sleep(self.interval)

    def __write_file(self):
        for file_name in FileNameEnum.values():
            # TODO: Doubt -> Do we need to check if the CDS string picked at least once as we have 50% probability
            random_string = self.__generate_string()

            # TODO: Assuming that we have to append everytime
            with open(file_name, 'a') as f:
                f.write(random_string + "\n")

    def __generate_string(self) -> str:
        """
        This will help us to generate random strings or return "CDS" with 50% of probability
        """
        if random.randint(0, 1):
            return "CDS"
        else:
            return ''.join(random.choice(string.ascii_letters) for _ in range(self.random_string_length))


if __name__ == "__main__":
    inter = int(input("Input Interval time(seconds) to generate strings : "))
    RandomWriter(interval=inter)._run()
    # RandomWriter(interval=inter).run_in_threading()
