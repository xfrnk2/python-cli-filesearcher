from common import main_category
from exception import illegal_argument_exception


class FileSearcher:

    def run(self):

        self.select_menu()
        pass

    def select_menu(self):
        print("[메인] 기능을 선택해 주세요.")
        for category in main_category.MainCategory:
            print(f"{category.method}: {category.description}")
