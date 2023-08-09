import colorama
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
    def turn_deck_data(self):
        return {
            1: ['первый игрок']*3,
            2: ['первый игрок']*2 + ['второй игрок']*2,
            3: ['первый игрок', 'второй игрок', 'третий игрок', 'любой игрок'],
            4: ['первый игрок', 'второй игрок', 'третий игрок', 'четвертый игрок']
        }

    def create_turn_deck(self):
        deck = self.turn_deck_data[self.players]
        deck.extend(['НЕМЕЗИДА']*2)
        self.turn_deck = dict(enumerate(deck, 1))
        return self.turn_deck

    def mix_turn_deck(self):
        new_deck = []
        copy_turn_deck = self.turn_deck.copy()
        while copy_turn_deck:
            keys = list(copy_turn_deck.keys())
            el = copy_turn_deck.pop(choice(keys))
            new_deck.append(el)
        return new_deck


g = TurnController(2)
g.create_turn_deck()
print(g.turn_deck)
while True:
    gm = Menu(topic='***ход ' + str(g.turn_count) + '***',
              variants=('тянуть карту очередности хода', 'конец игры'))
    gm.print_a_topic()
    gm.print_variants()
    answ = gm.get_user_answer()
    if answ == 'конец игры':
        break
    else:
        deck = g.mix_turn_deck()
        while deck:
            #print(deck)
            card_index = 0
            card = deck.pop(card_index)
            topic = f'***ход делает - {card}***\n'

            if len(deck) > 1:
                fm = Menu(topic, variants=('тянуть следующую карту', 'посмотреть следующую карту'))
            else:
                fm = Menu(topic, variants=('тянуть последнюю карту',))

            if not deck:
                fm.print_a_topic()
                print('***turn ' + str(g.turn_count) + ' finished***\n')
                g.turn_count += 1
            else:
                fm.print_a_topic()
                fm.print_variants()
                answ2 = fm.get_user_answer()

                if answ2 == 'посмотреть следующую карту':
                    next_index = card_index + 1
                    next_card = deck[next_index]

                    sm = Menu(topic=f'***следующим ходит - {next_card}***\n',
                              variants=('пусть ходит', 'В КОНЕЦ КОЛОДЫ!'))
                    sm.print_a_topic()
                    sm.print_variants()
                    answ3 = sm.get_user_answer()

                    if answ3 == 'В КОНЕЦ КОЛОДЫ!':
                        next_card_to_end_of_deck = deck.pop(next_index)
                        deck.append(next_card_to_end_of_deck)
                        print(f'***{next_card_to_end_of_deck} ходит последним***\n')
                    else:
                        continue

                card_index += 1
