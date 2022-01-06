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





def apart_game_run():
    while True:
        floor = input('몇층?(1~20까지만 받아요~) : ')
        if floor.isdigit() and (1 <= int(floor) <= 20):
            print_apart_floor(int(floor))
        else:
            print("동구밖 과수원샷~! 투샷~! 쓰리샷~! 치키치키 예! 마셔!")