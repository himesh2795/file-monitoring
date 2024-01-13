from monitor_system import MonitorSystem
from random_writer import RandomWriter


def __get_interval_time(input_msg):
    interval_time = False
    while not interval_time:
        try:
            interval_time = int(input(input_msg))
        except ValueError:
            print("Please provide appropriate number for interval")
    return interval_time


def main():
    try:
        random_writer_interval = __get_interval_time("Input Interval time(seconds) to generate strings : ")
        interval_time_for_monitoring = __get_interval_time("Input Monitoring Interval time(seconds): ")

        random_writer = RandomWriter(interval=random_writer_interval)
        random_writer.run_in_threading()

        MonitorSystem(interval_time_for_monitoring).run()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
