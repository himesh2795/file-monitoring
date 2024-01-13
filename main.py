from monitor_system import MonitorSystem
from random_writer import RandomWriter


def __get_interval_time(input_msg):
    """
    This function is to take valid interval time from the user.
    It asks user for interval_time until user doesn't provide appropriate integer as interval_time

    :param input_msg: The message to display as the input prompt.
    :return: The validated interval time as an integer.
    """
    interval_time = False
    while not interval_time:
        try:
            interval_time = int(input(input_msg))
        except ValueError:
            print("Please provide appropriate number for interval")
    return interval_time


def main():
    """
    Main function to execute the File Monitoring System.

    This function prompts the user to input the interval time for generating random strings
    and the interval time for monitoring files. It then initializes and runs the RandomWriter
    in a separate thread to generate random strings and the MonitorSystem to monitor the files.

    """
    try:
        # Take interval from suer to generate random string.
        random_writer_interval = __get_interval_time("Input Interval time(seconds) to generate strings : ")

        # Take interval time from user for monitoring files
        interval_time_for_monitoring = __get_interval_time("Input Monitoring Interval time(seconds): ")

        # Initialize and run the RandomWriter in a separate thread
        random_writer = RandomWriter(interval=random_writer_interval)
        random_writer.run_in_threading()

        # Initialize and run the MonitorSystem to monitor files
        MonitorSystem(interval_time_for_monitoring).run()
    except KeyboardInterrupt:
        print("Stopping the monitoring.")


if __name__ == "__main__":
    main()
