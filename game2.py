from print_info import *
import random
import time

def death_game(alcohol_game):
    game = Death_game(alcohol_game) # 게임 객체
    game.print_death_intro()
    num = game.pick_num()
    choose_status = game.choose_someone()
    loser = game.find_loser(num, choose_status)
    for player in game.players:
        if player.name == loser:
            player.drink(1)


class Death_game:
    def __init__(self, alcohol_game):
        self.user = alcohol_game.user
        self.tagger = alcohol_game.turn
        self.players = [self.user] + alcohol_game.computer_user_list # User 객체들 리스트
        self.players_name = self.make_players_name()


    def make_players_name(self): # User 객체들의 이름 리스트를 생성하는 기능
        players_name = []
        for player in self.players:
            players_name.append(player.name)

        return players_name
    

    def print_death_intro(self):
        print(''' ________ __                         ______                                           ______    ______         _______                         __      __       
    /        /  |                       /      \                                         /      \  /      \       /       \                       /  |    /  |      
    $$$$$$$$/$$ |____    ______        /$$$$$$  | ______   _____  ____    ______        /$$$$$$  |/$$$$$$  |      $$$$$$$  |  ______    ______   _$$ |_   $$ |____  
    $$ |  $$      \  /      \       $$ | _$$/ /      \ /     \/    \  /      \       $$ |  $$ |$$ |_ $$/       $$ |  $$ | /      \  /      \ / $$   |  $$      \ 
    $$ |  $$$$$$$  |/$$$$$$  |      $$ |/    |$$$$$$  |$$$$$$ $$$$  |/$$$$$$  |      $$ |  $$ |$$   |          $$ |  $$ |/$$$$$$  | $$$$$$  |$$$$$$/   $$$$$$$  |
    $$ |  $$ |  $$ |$$    $$ |      $$ |$$$$ |/    $$ |$$ | $$ | $$ |$$    $$ |      $$ |  $$ |$$$$/           $$ |  $$ |$$    $$ | /    $$ |  $$ | __ $$ |  $$ |
    $$ |  $$ |  $$ |$$$$$$$$/       $$ \__$$ /$$$$$$$ |$$ | $$ | $$ |$$$$$$$$/       $$ \__$$ |$$ |            $$ |__$$ |$$$$$$$$/ /$$$$$$$ |  $$ |/  |$$ |  $$ |
    $$ |  $$ |  $$ |$$       |      $$    $$/$$    $$ |$$ | $$ | $$ |$$       |      $$    $$/ $$ |            $$    $$/ $$       |$$    $$ |  $$  $$/ $$ |  $$ |
    $$/   $$/   $$/  $$$$$$$/        $$$$$$/  $$$$$$$/ $$/  $$/  $$/  $$$$$$$/        $$$$$$/  $$/             $$$$$$$/   $$$$$$$/  $$$$$$$/    $$$$/  $$/   $$/ 
''')
        time.sleep(1)
        print(f'''{self.tagger.name}님이 술래! 🤗)
~~~~~ 아 신난다😙 아 재미난다😆 더 게임 오브 데 스! ~~~~~\n''')
        time.sleep(1)


    def pick_num(self): # 술래가 숫자 정하는 기능
        if self.tagger != self.user: # 컴퓨터가 술래일 때
            num = random.randint(2, 2*len(self.players))
            print(f"{self.tagger.name} : {num} ❗❗❗")
        else:
            while True:
                num = input(f"2 이상 {2*len(self.players)} 이하의 정수를 외쳐 주세요! ")

                if not (num.isdigit() and (2 <= int(num) <= 2*len(self.players))):
                    print_wrong_input_info()
                else:
                    num = int(num)
                    break

        print("")
        time.sleep(1)

        return num


    def choose_someone(self): # 각 player들이 지목할 상대를 결정하는 기능
        choose_status = {} # 누가 누굴 지목하는지 나타내 주는 딕셔너리

        for name in self.players_name:
            temp = self.players_name[::]
            temp.remove(name) # 생성한 임시 리스트에서 자신의 이름은 제외
            choose_status[name] = random.choice(temp) # 자신이 지목할 상대 결정
        for k, v in choose_status.items():
            print(f"{k} 👉 {v}")

        print("")
        time.sleep(1)

        return choose_status


    def find_loser(self, num, choose_status): # 게임 진행
        k = self.tagger.name # 지목 turn 이름, 술래로 초기화

        for n in range(1, num+2):
            if n == num+1: # 마지막으로 num으로 지목 당한 loser case
                print(f"{k} : 🤮")
                time.sleep(1)
                return k # loser 이름(string)

            print(f"{k} : {n}! 😎👉 {choose_status[k]}")
            k = choose_status[k] # 지목 당한 사람을 다음 지목 turn으로 변경
            time.sleep(0.5)