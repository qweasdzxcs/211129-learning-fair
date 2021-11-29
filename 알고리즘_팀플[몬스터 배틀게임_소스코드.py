import random
import time

class Player():
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.wins = 0

    def calculate_damage(self, damage_amount, attacker): #공격 선택시
        if (damage_amount > self.health):
            overkill = abs(self.health - damage_amount)
            self.health = 0
            if (overkill > 0):
                print("{0}는(은) {1}에게 치명타를 입혔고,  {2}로인해 즉사했다."
                      .format(self.name.capitalize(), attacker, overkill))
            else:
                print("{0}는(은) {1}에게 치명타를 입혔다!"
                      .format(self.name.capitalize(), attacker))
        else:
            self.health -= damage_amount
            print("{0}는(은) {2}로부터 {1}의 피해를 입었다!"
                  .format(self.name.capitalize(), damage_amount, attacker))

    def calculate_heal(self, heal_amount): #회복 선택시
        if (heal_amount + self.health > 100):
            self.health = 100
            print("{0}는(은) 피로를 전부 회복했다!"
                  .format(self.name.capitalize()))
        else:
            self.health += heal_amount
            print("{0}는(은) {1}만큼 회복했다!"
                  .format(self.name.capitalize(), heal_amount))


def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


def get_selection(): #번호 선택
    valid_input = False
    while (valid_input is False):
        print()
        choice = input("공격 방법을 고르시오: ")
        if (parse_int(choice) is True):
            return int(choice)
        else:
            print("잘못입력하셨습니다. 한번 더 입력해 주세요.")


def get_computer_selection(health):
    sleep_time = random.randrange(2, 5)
    print("....상대편 공격중 잠시만 기다려 주세요....")
    print()
    time.sleep(sleep_time)

    if (health <= 35):
        # <=35일때 컴퓨터는 50%까지 치유
        result = random.randint(1, 6)
        if (result % 2 == 0):
            return 3
        else:
            return random.randint(1, 2)
    elif (health == 100):
        return random.randint(1, 2)
    else:
        return random.randint(1, 3)
    
def play_round(computer, human):
    game_in_progress = True
    current_player = computer
    
    while game_in_progress: # 유저와 컴퓨터 공격 순서를 바꿔줌
        if (current_player == computer):
            current_player = human
        else:
            current_player = computer

        print()
        print(
            "you HP: {0}     "
            "computer HP: {1}"
            .format(human.health, computer.health))
        print()

        if (current_player == human):
            print("공격 혹은 회복을을 선택하시오.:")
            print("1) Electrocute - 적당한 데미지를 줍니다.")
            print("2) Wild Swing - 확률적으로 데미지가 높거나 낮은 공격을 합니다, "
                  "자신의 운을 믿어보세요!!")
            print("3) Recovery - 적당량의 피를 회복시켜줌니다.")
            print()
            move = get_selection()
        else:
            move = get_computer_selection(computer.health)

        if (move == 1): #1번 데미지 18~25 랜덤
            damage = random.randrange(18, 25)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 2): #2번 데미지 10~35 랜덤
            damage = random.randrange(10, 35)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else: #3번 회복 18~25 랜덤
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 3):
            heal = random.randrange(18, 25)
            current_player.calculate_heal(heal)
        else:
            print ("잘못입력하셨습니다. 한번 더 입력해 주세요.")

        if (human.health == 0):
            print("패 배")
            computer.wins += 1
            game_in_progress = False

        if (computer.health == 0):
            print("승 리")
            human.wins += 1
            game_in_progress = False


def start_game():
    print("몬스터 배틀게임")
    print()
    print("게임 방법")
    print()
    print("1. 플레이할 캐릭터를 선택해 주세요")
    print("2. 상대편 적은 컴퓨터로 대결합니다. ")
    print(" 2-1 적의 캐릭터는 랜덤으로 선택되며, 플레이어와 동일 할 수 있습니다.")
    print("3. 목숨치는 유저와 적 동일하게 100입니다.")
    print("4. 공격 & 회복 번호를 입력하여 먼저 목숨값이 사라지면 집니다.")
    print("5. 승리 & 패배 후 게임을 다시할 수 있으며 스코어가 저장됩니다.")
    print()
    
    computer = Player("Computer")

    print("-------------선택할 수 있는 캐릭터-------------")
    print("       * 플루트                * 트러스티     ")
    print()
    print("    ■          ■                            ")
    print("      ■      ■                              ")
    print("    ■■■■■■■                ■   ■     ")
    print("  ■■  ■■■  ■■        ■  ■■■■■  ■")
    print("■■■■■■■■■■■      ■■■  ■  ■■■")
    print("■  ■■■■■■■  ■        ■■■■■■■  ")
    print("■  ■          ■  ■        ■  ■  ■  ■  ")
    print("      ■■■■■            ■■          ■■")
    print()
    print()
    print("        * 아로                    * 자크      ")
    print()
    print("                                ■      ■    ")
    print("      ■■■■■                  ■  ■      ")
    print("    ■■■■■■■              ■■■■■    ")
    print("  ■■    ■    ■■          ■■  ■  ■■  ")
    print("  ■■  ■■  ■■■        ■■■■■■■■■")
    print("  ■■■■■■■■■        ■  ■■■■■  ■")
    print("  ■■■■■■■■■        ■  ■■■■■  ■")
    print("  ■  ■  ■  ■  ■              ■  ■      ")
    print("                                ■■  ■■    ")
    print()

    name = input("당신의 캐릭터를 입력하시오.: ")
    print()
    human = Player(name)

    com = ["플루트", "트러스티", "아로", "자크"] #적 캐릭터 랜덤 출력
    print("적의 캐릭터: ", random.sample(com, 1))
    print()
    print()

    keep_playing = True

    while (keep_playing is True): #이어서 한판 더 게임할 때 스코어 저장  
        print("점수:")
        print("You - {0}".format(human.wins))
        print("Computer - {0}".format(computer.wins))

        computer.health = 100
        human.health = 100
        play_round(computer, human)
        print()
        response = input("한판 더 하시겠습니까?(Y/N)")
        if (response.lower() == "n"):
            break

start_game()
