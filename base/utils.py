from typing import List


# список преобразуется в строку
class Utils:

    @staticmethod
    def join_strings(str_list: List[str]) -> str:
        return ",".join(str_list)
