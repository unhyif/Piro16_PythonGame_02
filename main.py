"""
1) 게임이 끝날 때까지 게임이 멈추면 안된다 -> while True() -> break 조건을 걸어주자
2) game_setting()

"""

"""
본인 game.py를 import 해서 사용해주세요!
"""
from print_info import print_game_end_info, print_game_start_info, print_game_menu, print_wrong_input_info
import game1
import game2
import game3
import game4
import game5


# 전체 게임에서 공통으로 쓰는 속성들을 담는 클래스
class Game:
    def __init__(self, user, computer_num):
        self.user = user
        self.computer_num = computer_num

class User:
    def __init__(self, name, lethal_dose):
        self.name = name
        self.lethal_dose = lethal_dose
        self.amount = 0

    def drink(self, amount):
        self.amount += amount

    def is_dead(self):
        if self.lethal_dose > self.amount:
            return False
        return True


def game_setting():
    """
    1)
    2) 몇명이서 게임을 진행할지
    3) 주량은 얼마인지
    -> 전체 게임 하나 객체를 만들거에요!
    """
    start = input('🍺  게임을 진행할까요? (y/n) : ')
    if start == 'y':
        user_name = input('🍺  오늘 거하게 취해볼 당신의 이름은? : ')
        user_drink = input('🍺  당신의 치사량(주량)은 얼마만큼인가요? : ')
        computer_num = input('🍺  함께 취할 친구들은 얼마나 필요하신가요? : ')
        user_list = []
        alcohol_game = Game(user_list, computer_num)
        return alcohol_game
    elif start == 'n':
        print_game_end_info()
        return None
    else:
        print_wrong_input_info()


def alcohol_game_run():
    print_game_start_info()
    alcohol_game = game_setting()

    if alcohol_game is None:
        return
    while True:
        # 게임 메뉴 출력
        print_game_menu()
        user_input = input('🍺  어떤 게임을 진행할까요?(게임을 끝내시려면 \'exit\'를 입력해주세요) : ')
        if user_input == "1":
            # 자기 게임
            game1.br_game()
        elif user_input == "2":
            # 자기 게임
            game1.br_game()
        elif user_input == "3":
            # 자기 게임
            game1.br_game()
        elif user_input == "4":
            # 자기 게임
            game1.br_game()
        elif user_input == "5":
            # 자기 게임
            game1.br_game()
        elif user_input == "exit":
            print_game_end_info()
            break
        else:
            print_wrong_input_info()


if __name__ == '__main__':
    alcohol_game_run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
