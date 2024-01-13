import re
import time

from filename_enum import FileNameEnum


class MonitorSystem:
    def __init__(self, interval):
        self.interval = interval

    def run(self):
        while True:
            self.__read_and_log_generated_files()
            time.sleep(self.interval)

    @staticmethod
    def __read_and_log_generated_files():
        for file_name in FileNameEnum.values():
            with open(file_name) as f:
                file_content = f.read()
                pattern = re.compile(r'\bCDS\b')
                cds_occurrence = len(pattern.findall(file_content))
                text = f"{file_name} - {cds_occurrence}\n"
                print(text)
                if cds_occurrence:
                    with open("search_results.log", 'a') as log:
                        log.write(text)


if __name__ == "__main__":
    MonitorSystem(5).run()
