import random
import string
import threading
import time

from filename_enum import FileNameEnum


class RandomWriter:
    def __init__(self, interval: int, random_string_length: int = None):
        """
        :param interval: Regular interval time to generate and save randomly generated strings
        :param random_string_length: Randomly generated string length
        """
        self.interval = interval  # given interval

        # if random_string_length is not provided then random number between 5 and 10 is taken as a length
        self.random_string_length = random_string_length if random_string_length else random.randint(5, 10)

    def run_in_threading(self):
        """
        To run the writer in threading
        """
        threading.Thread(target=self._run).start()

    def _run(self):
        """
        Run the writer to continuously generate and write random strings to files.

        This method runs in an infinite loop. Calls the private method __write_file() to write the generated strings
        to files. The loop is paused for the specified interval time between iterations.
        """
        # counter to see the progress and validate if the program is running or not
        counter = 0
        while True:
            counter += 1
            print(f"Writing Randomly : {counter}")

            # calling method to generate and write string to the files.
            self.__write_file()

            # pausing loop for the given interval time
            time.sleep(self.interval)

    def __write_file(self):
        """
        To append randomly generated or CDS strings to the text files.

        - Iterate over file_names.
        - Generates random strings for the file_name using __generate_string() method.
        - Write the strings to the given file_name.
        """
        # Iterating over file names
        for file_name in FileNameEnum.values():
            # TODO: Doubt -> Do we need to check if the CDS string picked at least once as we have 50% probability
            # Calling __generate_string() method to get random string or "CDS"
            random_string = self.__generate_string()

            # TODO: Assuming that we have to append everytime
            # Appending the random string to the file
            with open(file_name, 'a') as f:
                f.write(random_string + "\n")

    def __generate_string(self) -> str:
        """
        To generate random strings or return "CDS" with 50% of probability

        :return: "CDS" or randomly generated string
        """
        if random.randint(0, 1):
            return "CDS"
        else:
            return ''.join(random.choice(string.ascii_letters) for _ in range(self.random_string_length))


if __name__ == "__main__":
    inter = int(input("Input Interval time(seconds) to generate strings : "))
    RandomWriter(interval=inter)._run()
    # RandomWriter(interval=inter).run_in_threading()
