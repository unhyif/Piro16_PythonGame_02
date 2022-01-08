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
import time
import requests


# 전체 게임에서 공통으로 쓰는 속성들을 담는 클래스
class Game:
    def __init__(self, user, computer_num):
        self.user = user
        self.computer_num = computer_num
        self.computer_user_list = self.make_computer_user_list(self.computer_num)
        self.turn = user


    def next_turn(self):
        if self.turn == self.user:
            self.turn = self.computer_user_list[0]
        else:
            for i in range(len(self.computer_user_list)):
                if self.turn == self.computer_user_list[i] and i < len(self.computer_user_list) - 1:
                    self.turn = self.computer_user_list[i+1]
                    return
                else:
                    self.turn = self.user
                    return


    @staticmethod
    def make_computer_user_list(computer_num):
        random_computer_user_list = [User('c승아', 6), User('c지현',6), User('c혜영', 5), User('c찬영', 3), User('c세윤', 2)]
        index_list = []
        computer_user_list = []

        while True:
            if len(index_list) == computer_num:
                break
            random_index = random.randint(1, 4)
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
            user_drink = int(user_drink) * 2
            break
    return int(user_drink)


def input_computer_num():
    while True:
        computer_num = input('🍺  함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : ')
        if not computer_num.isdigit() or not (1 <= int(computer_num) <= 3):
            print_wrong_input_info()
        else:
            break
    return int(computer_num)


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
            print_others_start_info(alcohol_game)
            return alcohol_game
        elif start == 'n':
            print_game_end_info()
            return None
        else:
            print_wrong_input_info()


def input_menu(alcohol_game):
    if alcohol_game.turn != alcohol_game.user:
        user_input = input('🍺  술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 \'exit\'를, 계속하시려면 아무키나 입력해주세요! :')
        if user_input != 'exit':
            user_input = str(random.randint(1,5))
            # 발표 시연을 위한 코드 user_input = input('🍺  ' + alcohol_game.turn.name + '(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : ')
            print('🍺  ' + alcohol_game.turn.name + '(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : ' + user_input)
    else:
        print('🍺  술게임 진행중! 당신의 턴입니다. 그만하고 싶으면 \'exit\'를 입력해주세요!')
        user_input = input('🍺  ' + alcohol_game.turn.name + '(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : ')
    return user_input


def is_anyone_dead(alcohol_game):
    if alcohol_game.user.is_dead():
        print(f"{alcohol_game.user.name}(이)가 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
        return True
    for user in alcohol_game.computer_user_list:
        if user.is_dead():
            print(f"{user.name}(이)가 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
            return True
    return False


def alcohol_game_run():
    print_game_start_info()
    # alcohol_game: game object(current user, computer 유저의 수를 가지고 있음.)
    alcohol_game = game_setting()
    print_result_info(alcohol_game)
    if alcohol_game is None:
        return
    while True:
        if is_anyone_dead(alcohol_game):
            time.sleep(1)
            print_game_end_info()
            break
        # 게임 메뉴 출력
        print_game_menu()
        user_input = input_menu(alcohol_game)
        time.sleep(1)

        if user_input == "1":
            game1.chef_game_run(alcohol_game)
            alcohol_game.next_turn()

        elif user_input == "2":
            game2.death_game(alcohol_game)
            alcohol_game.next_turn()

        elif user_input == "3":
            game3.zero_game(alcohol_game)
            alcohol_game.next_turn()

        elif user_input == "4":
            game4.record_game(alcohol_game)
            alcohol_game.next_turn()

        elif user_input == "5":
            game5.apart_game(alcohol_game)
            alcohol_game.next_turn()

        elif user_input == "exit":
            print_game_end_info()
            break
        else:
            print_wrong_input_info()
            continue
        print_result_info(alcohol_game)


if __name__ == '__main__':
    alcohol_game_run()
