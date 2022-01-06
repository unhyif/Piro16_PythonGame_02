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



def apart_game_run(alcohole_game):
    while True:
        floor = input('몇층까지 쌓아 올릴까요? (1~20까지만 쌓아 올릴 수 있습니다) : ')
        if floor.isdigit() and (1 <= int(floor) <= 20):
            print_apart_floor(int(floor))
        else:
            print("    Σ( ˙꒳˙  )!?Σ( ˙꒳˙  )!?     입력 실수~~~~?     Σ( ˙꒳˙  )!?Σ( ˙꒳˙  )!?    ")
            print("                                                                           ")
            print("            (งᐖ)ว  동구밖 과수원샷~! 투샷~! 쓰리샷~! 치키치키 예!  (งᐖ)ว")
            print(f"{alcohole_game.turn.name}(이)가 한 잔")
            break