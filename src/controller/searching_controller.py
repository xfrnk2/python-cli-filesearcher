import os

from exception import illegal_argument_exception


class SearchingController:

    def __init__(self):
        self.__root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.__unusable_name_values = ["/", "|", ":", "*", "?", "<", ">"]

    def run(self):
        while True:
            try:
                target_name = input("찾고자 하는 파일의 이름 또는 포함하는 문자를 입력하세요.")
                self.validate(target_name)
                result = self.search(self.__root_dir, target_name)

                break
            except illegal_argument_exception.IllegalArgumentException as e:
                print(e)

    def validate(self, value):
        if value == "":
            raise illegal_argument_exception.IllegalArgumentException("[ERROR] 빈 값을 입력할 수 없습니다.")
        for char in self.__unusable_name_values:
            if char in value:
                raise illegal_argument_exception.IllegalArgumentException(f"[ERROR] 사용이 불가능한 문자가 포함되어 있습니다. '{char}'")

    def search(self, dir, target_name) -> list:
        result = []
        queue = [(dir, os.listdir(dir))]
        while queue:
            path, files = queue.pop(0)
            for file in files:
                p = path + "\\" + file
                if os.path.isdir(p):
                    queue.append((p, os.listdir(p)))
                elif target_name in p:
                    result.append(p)
        return result
