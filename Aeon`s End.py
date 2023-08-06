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
            1: ['first']*3,
            2: ['first']*2 + ['second']*2,
            3: ['first', 'second', 'third', 'wild'],
            4: ['first', 'second', 'third', 'forth']
        }

    def create_turn_deck(self):
        deck = self.turn_deck_data[self.players]
        deck.extend(['nemesis']*2)
        self.turn_deck = dict(enumerate(deck, 1))
        return self.turn_deck

    def mix_turn_deck(self):
        new_deck = []
        copy_turn_deck = self.turn_deck.copy()
        while copy_turn_deck:
            keys = list(copy_turn_deck.keys())
            el = copy_turn_deck.pop(choice(keys))
            new_deck.append(el)
        new_deck = dict(enumerate(new_deck, 1))
        print(new_deck)
        return new_deck


g = TurnController(2)
g.create_turn_deck()
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
        for card_index in deck:

            print(deck[card_index])

            if len(deck)-1 >= card_index:
                fm = Menu(variants=('тянуть следующую карту', 'посмотреть следующую карту'))
            else:
                fm = Menu(variants=('тянуть следующую карту'))

            fm.print_variants()
            answ2 = fm.get_user_answer()

            if answ2 == 'посмотреть следующую карту':
                next_index = card_index+1
                print(deck[next_index])

                sm = Menu(variants=('оставить вытянутой', 'убрать в низ колоды'))
                sm.print_variants()
                answ3 = sm.get_user_answer()

                if answ3 == 'убрать в низ колоды':
                    ### здесь замуть со словарем. нодобно подумать!
                    next_card_to_end_of_deck = deck.pop(next_index)
                    deck[]
                    print(f'***{next_card_to_end_of_deck}*** идет на низ колоды\n')
                else:
                    continue

    print('***turn ' + str(g.turn_count) + ' finished***\n')
    g.turn_count += 1

