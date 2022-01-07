import main
import random
import time

def chef_game(alcohol_game):
    chef_game(alcohol_game)
    
menu=['떡볶이','비빔밥','김치찌개','부대찌개','치킨']
menu_pick=random.choice(menu)

def chef_game(alcohol_game):
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                                     오늘은 내가 요리사!! 오늘은 내가 요리사!!")

    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    print("오늘은 무엇을 만드나요??\n")
    time.sleep(1)
    print('오늘은 >>>>>',menu_pick,'<<<<< 만들어요!!!\n')

    computer_user_list = alcohol_game_computer_user_list
    # 이 게임을 시작한 유저
    turn = alcohol_game.turn

    while 1:
        # if (유저가 인풋을 해서 재료를 선택해야 하는 경우 == 현재 턴이 유저인 경우)
        if turn == alcohol_game.user:
            time.sleep(1)
            ingredients=input('무슨 재료가 들어갈까요? ')
            time.sleep(1)

        # else (현재 턴이 컴퓨터인 경우)
        else:
        # 리스트로 입력할 수 있는 재료들을 써놓고 그 안에서 랜덤으로 입력할 재료를 ingredients에 넣어주기
        # 랜덤으로 인덱스 뽑아서 재료 아무거나 입력

        rand=random.choice([True,False])
        if rand==True:
            time.sleep(0.5)
            print('있음!')
        else:
            time.sleep(0.5)
            print('없음!')
            time.sleep(1)
            alcohol_game.user.drink(1)
            break

        ## while 문 한번 돌때마다 다음 유저한테 turn을 넘겨준다.
        
    
    
    
