import re
import time

from filename_enum import FileNameEnum


class MonitorSystem:
    def __init__(self, interval: int):
        """
        :param interval: Regular interval time to monitor the files
        """
        self.interval = interval

    def run(self):
        """
        Run the system continuously to read and log generated file using __read_and_log_generated_files() method.
        - The loop is paused for the specified interval time between iterations.
        """
        while True:
            self.__read_and_log_generated_files()

            # pausing loop for the given interval time
            time.sleep(self.interval)

    @staticmethod
    def __read_and_log_generated_files():
        """
        - Iterate over file_names.
        - Read file and find "CDS" occurrences length.
        - Create a text to store in the search_results.log file
        - If CDS occurrences are found then append to the search_results.log.
        :return:
        """
        # Iterating over file names
        for file_name in FileNameEnum.values():
            # Open file in read mode
            with open(file_name) as f:
                # Read file
                file_content = f.read()

                # Using regex find the occurrence and length of "CDS" from the file
                pattern = re.compile(r'\bCDS\b')
                cds_occurrence = len(pattern.findall(file_content))

                # Create a text to append in the log
                text = f"{file_name} - {cds_occurrence}\n"
                print(text)

                if cds_occurrence:
                    # If CDS found then store to the log file with the given file name and the count
                    with open("search_results.log", 'a') as log:
                        log.write(text)


if __name__ == "__main__":
    MonitorSystem(5).run()
