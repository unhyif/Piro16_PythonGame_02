import random
import time

def death_game(alcohol_game):
    players = [alcohol_game.user] + alcohol_game.computer_user_list # User 객체들 리스트
    
    game = Death_game(alcohol_game)
    game.print_death_intro(players)

    num = random.randint(2, 2*len(players)+1) # 술래가 외칠 숫자
    print(f"{game.origin.turn.name} : {num} ❗❗❗\n")
    choose_status = game.choose_someone(players) # 딕셔너리
    loser = game.find_loser(choose_status, game.origin.turn.name, num) # 진 사람 이름(string)
    
    for player in players:
        if player.name == loser:
            return player # 진 User 객체


class Death_game:

    def __init__(self, alcohol_game):
        self.origin = alcohol_game

    def choose_someone(self, players): # 각 player들이 상대를 지목하는 기능
        choose_status = {} # 누가 누굴 지목하는지 나타내 주는 딕셔너리

        players_name = self.make_name_list(self.origin, players) # 이름 리스트
        for name in players_name:
            temp = players_name[::]
            temp.remove(name) # 생성한 임시 리스트에서 자신의 이름은 제외
            choose_status[name] = random.choice(temp) # 자신이 지목할 상대 결정
        for k, v in choose_status.items():
            print(f"{k} 👉 {v}")

        return choose_status


    def find_loser(self, choose_status, tagger, num): # 게임 진행
        print("")
        k = tagger # 지목 turn인 사람, 술래부터 시작

        for n in range(1, num+2):
            if n == num+1:
                print(f"{k} : 🤮")
                return k # 진 사람 이름(string)

            print(f"{k} : {n}! 😎👉 {choose_status[k]}")
            k = choose_status[k] # 지목 당한 사람을 다음 지목 turn으로 변경




    @staticmethod
    def make_name_list(main_game, players): # 술래인 사람의 이름이 맨 앞에 오도록, User 객체들의 이름 리스트를 생성하는 기능
        players_name = []
        for player in players:
            if player.name == main_game.turn.name:
                pass;
            else:
                players_name.append(player.name)

        random.shuffle(players_name)
        players_name = [main_game.turn.name] + players_name

        return players_name


    def print_death_intro(self, players):
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
        print(f'''이번엔 {self.origin.turn.name}님부터 시작합니다! 2부터 {2*len(players)} 사이의 수를 부르시면 됩니다!
~~~ 아 신난다😙 아 재미난다😆 더 게임 오브 데 스! ~~~
''')
        time.sleep(1)

