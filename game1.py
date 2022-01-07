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
    
    while 1:
        time.sleep(1)
        ingredients=input('무슨 재료가 들어갈까요? ')
        time.sleep(1)
        
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

        
    
    
    
