"""
1) 게임이 끝날 때까지 게임이 멈추면 안된다 -> while True() -> break 조건을 걸어주자
2) game_setting()

"""

"""
본인 game.py를 import 해서 사용해주세요!
"""
from print_info import *
import game1
import game2
import game3
import game4
import game5
import random


# 전체 게임에서 공통으로 쓰는 속성들을 담는 클래스
class Game:
    def __init__(self, user, computer_num):
        self.user = user
        self.computer_num = computer_num
        self.computer_user_list = self.make_computer_user_list()

    @staticmethod
    def make_computer_user_list(computer_num):
        random_computer_user_list = [User('c승아', 6), User('c지현',4), User('c혜영', 5), User('c찬영', 3), User('c세윤', 2)]
        index_list = []
        computer_user_list = []

        while True:
            random_index = random.randint(0, 4)
            if random_index in index_list:
                continue
            else:
                index_list.append(random_index)

        for i in index_list:
            computer_user_list.append(random_computer_user_list[i])
        return computer_user_list


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


def input_user_drink():
    print_drink_info()
    while True:
        user_drink = input('🍺  당신의 치사량(주량)은 얼마만큼인가요?(1~5을 선택해주세요) : ')
        if not user_drink.isdigit() or not (1 <= int(user_drink) <= 5):
            print_wrong_input_info()
        else:
            break
    return user_drink


def input_computer_num():
    while True:
        computer_num = input('🍺  함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : ')
        if not computer_num.isdigit() or not (1 <= int(computer_num) <= 5):
            print_wrong_input_info()
        else:
            break
    return computer_num


def game_setting():
    """
    1)
    2) 몇명이서 게임을 진행할지
    3) 주량은 얼마인지
    -> 전체 게임 하나 객체를 만들거에요!
    """
    while True:
        start = input('🍺  게임을 진행할까요? (y/n) : ')
        if start == 'y':
            user_name = input('🍺  오늘 거하게 취해볼 당신의 이름은? : ')
            lethal_dose = input_user_drink()
            computer_num = input_computer_num()
            user = User(user_name, lethal_dose)
            alcohol_game = Game(user, computer_num)
            return alcohol_game
        elif start == 'n':
            print_game_end_info()
            return None
        else:
            print_wrong_input_info()


def alcohol_game_run():
    print_game_start_info()
    # alcohol_game: game object(current user, computer 유저의 수를 가지고 있음.)
    alcohol_game = game_setting()

    if alcohol_game is None:
        return
    while True:
        # 게임 메뉴 출력
        print_game_menu()
        user_input = input('🍺  ' + alcohol_game.user.name + '(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : ')
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
            # 아파트~아파트~
            game5.apart_game(alcohol_game)
        elif user_input == "exit":
            print_game_end_info()
            break
        else:
            print_wrong_input_info()


if __name__ == '__main__':
    alcohol_game_run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
