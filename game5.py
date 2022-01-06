import time
import random

def apart_game(alcohol_game):
    print_apart_game_info()
    apart_game_run(alcohol_game)


def print_apart_game_info():
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(
        "                                          🏢   아~파트 아파트! 아~파트 아파트! 몇층?  🏢                                              ")
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def print_wrong_input_floor(alcohol_game):
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(
        f"                Σ( ˙꒳˙  )!?Σ( ˙꒳˙  )!?     {alcohol_game.turn.name}~~~? 입력 실수~~~~?     Σ( ˙꒳˙  )!?Σ( ˙꒳˙  )!?               ")
    print(
        "                                    (งᐖ)ว  동구밖 과수원샷~! 투샷~! 쓰리샷~! 치키치키 예!  (งᐖ)ว                                       ")
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    print(f"[SYSTEM] {alcohol_game.turn.name}이 한잔 마십니다. 아파트 게임이 종료되었습니다.")


def set_stack_user_order(alcohol_game):
    user_list = alcohol_game.computer_user_list.copy()
    user_list.append(alcohol_game.user)
    user_floor_dict = {}
    user_order = []
    cnt = 0

    while True:
        if cnt == len(user_list):
            break
        index = random.randint(0, len(user_list)-1)
        if user_list[index].name in user_floor_dict.keys():
            if user_floor_dict[user_list[index].name] == 2:
                cnt += 1
                continue
            else:
                user_floor_dict[user_list[index].name] = 2
                user_order.append(user_list[index].name)
        else:
            user_floor_dict[user_list[index].name] = 1
            user_order.append(user_list[index].name)

    return user_order


def print_apart_floor(user_order, floor):
    print(
        "                                          🏢   모든 플레이어가 아파트에 층을 올렸습니다!  🏢                                              ")
    for i in range(floor):
        order = i % len(user_order)
        print(f"🏢  {i+1}층은  {user_order[order]}이 쌓았습니다.")
        if i == floor-1:
            return user_order[order]


def print_drink_user_info(user):
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(
        f"       Σ( ˙꒳˙  )!?Σ( ˙꒳˙  )!?     누가 술을 마셔? {user}(이)가 술을 마셔!     Σ( ˙꒳˙  )!?Σ( ˙꒳˙  )!?              ")
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    print(f"[SYSTEM] {user}이 한잔 마십니다. 아파트 게임이 종료되었습니다.")


def apart_game_run(alcohol_game):
    floor = 0
    if alcohol_game.turn == alcohol_game.user:
        floor = input('몇층까지 쌓아 올릴까요? (1~20까지만 쌓아 올릴 수 있습니다) : ')

        if not floor.isdigit() or not (1 <= int(floor) <= 20):
            print_wrong_input_floor(alcohol_game)
            alcohol_game.turn.drink(1)
            return

        floor = int(floor)

    else:
        floor = random.randint(1, 20)
        print('몇층까지 쌓아 올릴까요? (1~20까지만 쌓아 올릴 수 있습니다) : ' + str(floor))

    user_order = set_stack_user_order(alcohol_game)
    drink_user_name = print_apart_floor(user_order, floor)
    print_drink_user_info(drink_user_name)
    for user in alcohol_game.computer_user_list:
        if user.name == drink_user_name:
            user.drink(1)
            return
    if drink_user_name == alcohol_game.user.name:
        alcohol_game.user.drink(1)
