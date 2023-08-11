from  colorama import Fore
from random import choice
from Menu import Menu


class TurnController:
    def __init__(self, players):
        self.players = players
        self.turn_deck = {}
        self.turn = 1

    @property
    def turn_count(self):
        return self.turn

    @turn_count.setter
    def turn_count(self, turn_count):
        self.turn = turn_count

    @property
    def deck(self):
        return self.turn_deck

    @deck.setter
    def deck(self, new_deck):
        self.turn_deck = new_deck

    @property
    def turn_deck_data(self):
        return {
            1: ['первый игрок']*3,
            2: ['первый игрок']*2 + ['второй игрок']*2,
            3: ['первый игрок', 'второй игрок', 'третий игрок', 'любой игрок'],
            4: ['первый игрок', 'второй игрок', 'третий игрок', 'четвертый игрок']
        }

    @property
    def color_card_data(self):
        return {
            'первый игрок': Fore.YELLOW,
            'второй игрок': Fore.BLUE,
            'третий игрок': Fore.MAGENTA,
            'четвертый игрок': Fore.GREEN,
            'НЕМЕЗИДА': Fore.RED
        }

    def create_turn_deck(self):
        deck = self.turn_deck_data[self.players]
        deck.extend(['НЕМЕЗИДА']*2)
        self.turn_deck = [self.color_card_data[c]+c+Fore.RESET for c in deck]
        self.turn_deck = dict(enumerate(self.turn_deck, 1))
        return self.turn_deck

    def mix_turn_deck(self):
        new_deck = []
        copy_turn_deck = self.turn_deck.copy()
        while copy_turn_deck:
            keys = list(copy_turn_deck.keys())
            el = copy_turn_deck.pop(choice(keys))
            new_deck.append(el)
        return new_deck

    def pull_a_card(self):
        card = self.deck.pop(0)
        return card


g = TurnController(2)
while True:
    gm = Menu(topic='***ход ' + str(g.turn_count) + '***',
              variants=('тянуть карту очередности хода', 'конец игры'))
    gm.print_a_topic()
    gm.print_variants()
    answ = gm.get_user_answer()
    if answ == 'конец игры':
        break
    else:
        g.create_turn_deck()
        g.deck = g.mix_turn_deck()
        #print(g.deck)
        while g.deck:
            card = g.pull_a_card()
            topic = f'***ход делает - {card}***\n'

            if len(g.deck) > 1:
                fm = Menu(topic, variants=('тянуть следующую карту', 'посмотреть следующую карту'))
            else:
                fm = Menu(topic, variants=('тянуть последнюю карту',))

            if not g.deck:
                fm.print_a_topic()
                print('***  раунд ' + str(g.turn_count) + ' окончен***\n')
                g.turn_count += 1
            else:
                fm.print_a_topic()
                fm.print_variants()
                answ2 = fm.get_user_answer()

                if answ2 == 'посмотреть следующую карту':
                    next_card = g.pull_a_card()

                    sm = Menu(topic=f'***следующим ходит - {next_card}***\n',
                               variants=('пусть ходит', 'В КОНЕЦ КОЛОДЫ!'))
                    sm.print_a_topic()
                    sm.print_variants()
                    answ3 = sm.get_user_answer()

                    if answ3 == 'В КОНЕЦ КОЛОДЫ!':
                        g.deck.append(next_card)
                        print(f'***{next_card} ходит последним***\n')
                    else:
                        g.deck.insert(0, next_card)
