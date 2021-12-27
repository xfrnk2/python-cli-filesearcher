from common import main_category
from controller import searching_controller
from exception import illegal_argument_exception


class FileSearcher:

    def __init__(self):
        self.__searching_controller = searching_controller.SearchingController()

    def run(self):

        self.select_menu()
        pass

    def select_menu(self):
        while True:
            try:
                option = self.ask_option_choice()
                self.perform_option(option)
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

    def perform_option(self, option: str) -> None:
        if option == main_category.MainCategory.SEARCH.method:
            self.__searching_controller.run()
