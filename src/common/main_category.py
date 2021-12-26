from enum import unique

from aenum import MultiValueEnum


@unique
class MainCategory(MultiValueEnum):
    SEARCH = "1", "파일 탐색"
    EXIT = "Q", "프로그램 종료"

    @property
    def method(self):
        return self.values[0]

    @property
    def description(self):
        return self.values[1]
