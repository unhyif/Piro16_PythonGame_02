import main
import random
import time

def zero_game(alcohol_game):
    print_zero_game_info()
    zero_game_run(alcohol_game)


def print_zero_game_info():
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(
        "                                          0   제로~~~ 제로~~~~ 제로!!!  0                                              ")
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def zero_game_run(alcohol_game):
    max = (alcohol_game.computer_num+1)*2 #제로게임 최대

    while True:
        print(alcohol_game.turn.name, '님의 턴입니다')

        if(alcohol_game.turn == alcohol_game.user): # 사용자 턴
            sum = 0

            while True: #목표숫자 입력받기
                try:
                    print("0~",max,"까지 중 숫자를 골라주세요 : ", end = '')
                    g_n = int(input())
                    if(g_n > 0 and g_n <= max):
                        break
                    else:
                        print("범위에 알맞은 숫자를 고르세요!")
                except ValueError:
                    print('올바른 값을 입력해주세요!')
            while True:
                try:
                    f_n = int(input("0, 1, 2중에서 펼칠 손가락의 개수를 입력해주세요 : "))
                    if (f_n >= 0 and f_n < 3):
                        sum += f_n
                        break
                    else:
                        print("범위에 알맞은 숫자를 고르세요!")
                except ValueError:
                    print('올바른 값을 입력해주세요!')
                     
            print(g_n, '개의 손가락이 올라오면 게임이 끝납니다!')
            print(alcohol_game.user.name, '님은 손가락', f_n, '개를 들었습니다.')
            for i in range(alcohol_game.computer_num): #컴퓨터 플레이어들이 드는 손가락 합
                f_n = random.randint(0,2)
                print(alcohol_game.computer_user_list[i].name,'님은 손가락', f_n,'개를 들었습니다.')
                sum +=f_n

            print('총 합은 ', sum, '이였습니다!')

            if(sum == g_n): #목표 숫자랑 손가락 합이 같다면 이김
                print('축하드려요!!', alcohol_game.user.name, '님이 이겼습니다!')
                for i in range(len(alcohol_game.computer_user_list)):
                    alcohol_game.computer_user_list[i].drink(1) #컴퓨터 유저 마시기
                break #게임 끝

            else: # 다르다면 다음 턴
                print(alcohol_game.user.name,'님 아쉽게도 이기지 못했습니다ㅠㅠ 다음 턴을 기대해봐요!')
                print('-------------------------')
                alcohol_game.next_turn()
        
        else:
            sum=0
            g_n = random.randint(0,max) #목표 숫자 랜덤설정
            

            while True: #유저 손가락 드는 게수 입력 받기
                try:
                    f_n = int(input("0, 1, 2중에서 펼칠 손가락의 개수를 입력해주세요 : "))
                    if(f_n >= 0 and f_n < 3):
                        sum += f_n
                        break
                    else:
                        print("범위에 알맞은 숫자를 고르세요!")
                except ValueError:
                    print('올바른 값을 입력해주세요!')

            print(g_n, '개의 손가락이 올라오면 게임이 끝납니다!')
            print(alcohol_game.user.name, '님은 손가락', f_n, '개를 들었습니다.')
            for i in range(alcohol_game.computer_num): #컴퓨터 유저 손가락 들기
                f_n = random.randint(0,2)
                print(alcohol_game.computer_user_list[i].name,'님은 손가락', f_n,'개를 들었습니다.')
                sum +=f_n

            if(sum == g_n): #목표 숫자 같으면 이김
                print('축하드려요!!', alcohol_game.turn.name, '님이 이겼습니다!')


                alcohol_game.user.drink(1) #유저도 마심

                for i in range(len(alcohol_game.computer_user_list)):
                    if(alcohol_game.turn != alcohol_game.computer_user_list[i]): #이긴 컴터 유저 제외하고 마심
                        alcohol_game.computer_user_list[i].drink(1)
                break #게임 끝

            else: #틀렸으면 다음턴
                print(alcohol_game.turn.name,'님 아쉽게도 이기지 못했습니다ㅠㅠ 다음 턴을 기대해봐요!')
                print('-------------------------')
                alcohol_game.next_turn() 
                