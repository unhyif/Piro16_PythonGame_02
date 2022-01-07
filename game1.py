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


    # 이 게임을 시작한 유저

    while 1:

        rand=random.choice([True,False])    
        # if (유저가 인풋을 해서 재료를 선택해야 하는 경우 == 현재 턴이 유저인 경우)
        if alcohol_game.turn == alcohol_game.user:

            time.sleep(1)
            ingredients=input('무슨 재료가 들어갈까요? ')
            time.sleep(1)

            if rand==True:
                time.sleep(0.5)
                print('있음!')
                alcohol_game.next_turn() 

            else:
                time.sleep(0.5)
                print('없음!')
                time.sleep(1)
                alcohol_game.user.drink(1)
                time.sleep(0.5)
                break               

    

        else:
            ingredients_list=["셰프님의 정성","셰프님의 사랑♥","셰프님의 미모"]
            random_ingredients = random.choice(ingredients_list)

            rand_=random.choice([True,False])

            for i in range(len(alcohol_game.computer_user_list)):
                print(alcohol_game.user.name,': ', random_ingredients)
                
                
                
                if rand==True:
                    time.sleep(0.5)
                    print('있음!')
                    alcohol_game.next_turn() 
                else:
                    time.sleep(0.5)
                    print('없음!')
                    time.sleep(1)
                    alcohol_game.turn.drink(1)
                    time.sleep(0.5)
                    break
               
                break         
                
                
            
        
        # else (현재 턴이 컴퓨터인 경우)
        
        # 리스트로 입력할 수 있는 재료들을 써놓고 그 안에서 랜덤으로 입력할 재료를 ingredients에 넣어주기
        # 랜덤으로 인덱스 뽑아서 재료 아무거나 입력


            
        
            ## while 문 한번 돌때마다 다음 유저한테 turn을 넘겨준다.
        
        break
    
    
