from common import main_category
from exception import illegal_argument_exception


class FileSearcher:

    def run(self):

        self.select_menu()
        pass

    def select_menu(self):
        while True:
            try:
                option = self.ask_option_choice()
                break
            except illegal_argument_exception.IllegalArgumentException as e:
                print(e)

    def ask_option_choice(self) -> str:
        print("[메인] 기능을 선택해 주세요.")
        for category in main_category.MainCategory:
            print(f"{category.method}: {category.description}")
        option = input()

        if option not in [item.method for item in main_category.MainCategory]:
            raise illegal_argument_exception.IllegalArgumentException("유효하지 않은 명령입니다.")
        return option