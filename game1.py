import main
import random
import time


def chef_game(alcohol_game):
    chef_game_run(alcohol_game)

    
menu=['떡볶이','비빔밥','김치찌개','부대찌개','치킨']
menu_pick=random.choice(menu)

        

def chef_game_run(alcohol_game):
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                                     오늘은 내가 요리사!! 오늘은 내가 요리사!!")

    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    print("오늘은 무엇을 만드나요??\n")
    time.sleep(1)
    print('오늘은 >>>>>',menu_pick,'<<<<< 만들어요!!!\n')

    turn_list = [alcohol_game.user] + alcohol_game.computer_user_list # 사람 + 컴퓨터
    turn_list.remove(alcohol_game.turn) # 사람 + 컴퓨터 중 요리사게임 시작해야 되는 유저(starter) 제거
    turn_list = [alcohol_game.turn] + turn_list # starter + 나머지 플레이어 (starter가 사람인지 컴퓨터인지 모름)
    
    i = 0

    while 1: # 재료 X로 게임 끝날 때 까지 반복
        if i == len(turn_list):
            i = 0 # 총 플레이어 4명일 때, turn_list[4]는 존재하지 않으므로 turn_list[0]으로 순서 return
        current_starter = turn_list[i] # main에서 정해진 turn 유저부터 시작하기 위해 위에서 i=0으로 초기화 해놈

        rand=random.choice([True,False])    

        # if (유저가 인풋을 해서 재료를 선택해야 하는 경우 == 현재 턴이 유저인 경우)
        if current_starter == alcohol_game.user: # 사람 차례일 때

            time.sleep(1)
            ingredients=input('무슨 재료가 들어갈까요? ')
            time.sleep(1)

            if rand==True:
                time.sleep(0.5)
                print('있음!')
                i += 1 # current_starter가 turn_list[i] 이므로 다음 타자로 넘어가기 위해 1을 더해줌

            else:
                time.sleep(0.5)
                print('없음!')
                time.sleep(1)
                current_starter.drink(1)
                time.sleep(0.5)
                break               
    

        else: # 컴퓨터 차례일 때
            ingredients_list=["셰프님의 정성","셰프님의 사랑♥","셰프님의 미모"]
            random_ingredients = random.choice(ingredients_list)
            # rand_=random.choice([True,False]) 생략 가능
           
            print(current_starter.name,': ', random_ingredients)
            
            if rand ==True:
                time.sleep(0.5)
                print('있음!')
                i += 1 # 다음 차례로 넘기기 위해
                
            else:
                time.sleep(0.5)
                print('없음!')
                time.sleep(1)
                current_starter.drink(1)
                time.sleep(0.5)
                break