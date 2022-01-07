import requests
from bs4 import BeautifulSoup as bs
import re
import random
import time

def record_game(alcohol_game):
    print_record_game_info() # 출력
    record_game_run(alcohol_game) # 게임 실행

def print_record_game_info():
    print()
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(
        "                                 🎵 레코드 레코드 이이이~!  레코드 레코드 이이이~! 🎵                              ")
    print(

        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("※ 게임 주의사항! 노래 제목과 가사는 >>> 정확하게 <<< 입력해주세요~ 5글자 이하로  입력한 가사는 인정되지 않아요~ ")
    print()
    time.sleep(1)

def record_game_run(alcohol_game):

    # 노래 선곡
    if alcohol_game.turn.name == alcohol_game.user.name:
        title = input("♬ 노래 제목을 !정확하게! 입력해주세요◎_◎ ▷ ")
    else:
        title_list = ["잔소리", "예뻤어", "신호등", "Next level", "라일락", "살짝 설렜어", "밤편지", "봄날", "아무노래", "아로하", "오랜 날 오랜 밤", "가시", "작은 것들을 위한 시", "Psycho"]
        title = random.choice(title_list)


    # 크롤링 - 실패 시 발제자 샷
    try:
        url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={}+가사&oquery={}&tqi=hONOUdprvxZssLNoeOsssssssER-390973".format(title, title)
        response = requests.get(url)
        soup = bs(response.text, "html.parser")
        lyric_html = soup.select_one("._cm_content_area_song_lyric p")
        lyric = str(lyric_html)
        lyric = re.sub(r'<p class=".*">', '\n', lyric)
        lyric = re.sub(r'<br>', '\n', lyric)
        lyric = re.sub(r'<br/>', '\n', lyric)
        lyric = re.sub(r'<.*>', '\n', lyric)

        lyric_text = lyric_html.text.strip()  # 전체 가사가 연결된 문자열
        lyric_text = re.sub(r'[^0-9a-zA-Z가-힣]', '', lyric_text)  # 띄어쓰기, 문장 부호 없애는 전처리
        lyric_list = []  # 문장 단위로 가사가 구분된 리스트
        for sentence in lyric.split("\n"):
          if sentence.strip() != '' and sentence.strip() not in lyric_list:
            lyric_list.append(sentence.strip())

        print()
        print("♩ {} 님이 >>> {} <<< 노래를 골랐습니다!".format(alcohol_game.turn.name, title))
        print()
        print("♪ {} 가사 대기 시작 ~! ".format(title))

    except:
        print()
        print()
        print()
        print("  Σ( ˙꒳˙  )!?Σ( ˙꒳˙  )!?  해당 제목의 노래가 없어요!   Σ( ˙꒳˙  )!?Σ( ˙꒳˙  )!?   ")
        print("                                                                           ")
        print("            (งᐖ)ว  발! 제! 자!  샷 ~!   발! 제! 자!  샷 ~!  (งᐖ)ว")
        print()
        print(f"{alcohol_game.turn.name}(이)가 한 잔")
        print()
        alcohol_game.turn.drink(1)
        time.sleep(1)
        return  # 게임 종료


    # 게임 진행
    player_list = [alcohol_game.user]
    player_list.extend(alcohol_game.computer_user_list)
    current_player = alcohol_game.turn
    input_history = []

    while True:
        
        # 현재 순서
        if player_list.index(current_player) == len(player_list) - 1:
            current_player = player_list[0]
        else:
            current_player = player_list[player_list.index(current_player) + 1]


        # 노래 가사 대기
        if current_player == alcohol_game.user:
            print()
            input_lyric = input(f"♬ 당신의 차례입니다! {title} 노래 가사 한 소절을 적어주세요 >_< ▷ ")
            print()
            print("▶▶▶ {} : ♬♪ {} ♪♬".format(current_player.name, input_lyric))
        else:
            computer_success = random.randint(1, 100)  # 80% 확률로 성공 (성공하더라도 중복 가사를 말할 수도 있음)
            if computer_success >= 20:
                input_lyric = random.choice(lyric_list)
                print()
                print("▶▶▶ {} : ♬♪ {} ♪♬".format(current_player.name, input_lyric))
            else:
                input_lyric = random.choice(["음........................ㅜㅜㅜㅜㅜ", "나 이 노래 몰라 ㅠㅠㅠㅠㅠㅠ", "....그냥 마시겠습니다~", ".....???? 이게 무슨 노래야", ".......................ㅎㅎㅎㅎㅎㅎㅎㅎ"])
                print()
                print("▶▶▶ {} : {}".format(current_player.name, input_lyric))
        
        time.sleep(1)


        # 노래 가사 검사
        input_lyric = re.sub(r'[^0-9a-zA-Z가-힣]', '', input_lyric)  # 띄어쓰기, 문장 부호 없애는 전처리
        valid = False
        short = False

        for start in range(len(lyric_text) - len(input_lyric) + 1):
            if input_lyric == lyric_text[start:start+len(input_lyric)]:
                valid = True  # 가사에 있는 가사
            
        for past_input in input_history:
            for start in range(len(past_input) - len(input_lyric) + 1):
                if input_lyric == past_input[start:start+len(input_lyric)]:
                    valid = False  # 이미 나온 가사

        input_history.append(input_lyric)

        if len(input_lyric) <= 5:
            valid = False
            short = True

        # 확인
        if valid == True:
            new_lyric_text = ""
            for sub_lyric in lyric_text.split(input_lyric):
                new_lyric_text += sub_lyric
            lyric_text = new_lyric_text  # 이미 나온 가사 지우기
        else:
            print()
            print()
            print()
            if short == True:
                print("  Σ( ˙꒳˙  )!?Σ( ˙꒳˙  )!?  에이 너무 짧잖아~~~   Σ( ˙꒳˙  )!?Σ( ˙꒳˙  )!?   ")
            else:
                print("  Σ( ˙꒳˙  )!?Σ( ˙꒳˙  )!?  그런 가사는  없어요!   Σ( ˙꒳˙  )!?Σ( ˙꒳˙  )!?   ")
            print("                                                                           ")
            print(f"            (งᐖ)ว  아 누가 술을 마셔 ~ {current_player.name}(이)가 술을 마셔 ~  (งᐖ)ว")
            for i in range(len(current_player.name)):
                print()
                print(f"                  {current_player.name[i]}  (짝) (짝) ! (짝) (짝) !             ")
            print()
            print("                       아 원~~~ 샷~~~!                       ")
            print()
            current_player.drink(1)
            break
            
    
