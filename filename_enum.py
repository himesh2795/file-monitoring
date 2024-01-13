from enum import Enum


class FileNameEnum(Enum):
    FILE1 = "random_string_1.txt"
    FILE2 = "random_string_2.txt"

    @classmethod
    def values(cls):
        """Returns a list of all the enum values."""
        return list(cls._value2member_map_.keys())
