import random
import string
import threading
import time


class RandomWriter:
    def __init__(self, interval: int, random_string_length: int = None):
        self.interval = interval
        self.random_string_length = random_string_length if random_string_length else random.randint(5, 10)

    def run(self):
        # TODO: Doubt about regular interval of time. Is it ongoing or is the interval between two files?
        counter = 0
        while True:
            counter += 1
            print(counter)
            self.write_file()
            time.sleep(self.interval)

    def run_in_threading(self):
        # If ongoing then in threading
        threading.Thread(target=self.run).start()

    def write_file(self):
        for file_name in ["random_string_1.txt", "random_string_2.txt"]:
            # TODO: Doubt -> Do we need to check if the CDS string picked at least once as we have 50% probability
            random_string = self.generate_string()

            # TODO: Assuming that we have to append everytime
            with open(file_name, 'a') as f:
                f.write(random_string + "\n")

    def generate_string(self) -> str:
        """
        This will help us to generate random strings or return "CDS" with 50% of probability
        """
        if random.randint(0, 1):
            return "CDS"
        else:
            return ''.join(random.choice(string.ascii_letters) for _ in range(self.random_string_length))


if __name__ == "__main__":
    inter = int(input("Input Interval time(seconds) to generate strings : "))
    RandomWriter(interval=inter).run()
    # RandomWriter(interval=inter).run_in_threading()
