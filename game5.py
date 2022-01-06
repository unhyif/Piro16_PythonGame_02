from main import User, Game


def apart_game(alcohol_game):
    print_apart_game_info()
    apart_game_run()


def print_apart_game_info():
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(
        "                                          🏢   아~파트 아파트! 아~파트 아파트! 몇층?  🏢                                              ")
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



def print_apart_floor(floor):
    for i in floor:
        print(" ______________ ")
        print(" |  ㅁ  ㅁ  ㅁ  | ")
    print(" ______________ ")

    print(f"{floor}층에는")




def apart_game_run():
    while True:
        floor = input('몇층?(1~20까지만 받아요~) : ')
        if floor.isdigit() and (1 <= int(floor) <= 20):
            print_apart_floor(int(floor))
        else:
            print("마셔!(입력이 잘못 되어도 마셔야죠?)")