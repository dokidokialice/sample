""" Copyright 2019 Takashi Nagai

This file is part of BlackJack.

    BlackJack is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    BlackJack is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with BlackJack.  If not, see <http://www.gnu.org/licenses/>.
 """    
 
import random

class Card:
    suit = ''
    rank = 0

    def __init__(self, set_suit, set_rank):
        self.suit = set_suit
        self.rank = set_rank

class CardDeck:
    ACE = 1
    PIPCARD_MAX = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    SUIT_LIST = ['spade', 'heart', 'club', 'diamond']
    
    def __init__(self, BlackJack_ON = False):
        self.deck = {}
        for suit in self.SUIT_LIST:
            rank_list = []
            for count in range(self.ACE, (self.PIPCARD_MAX + 1)):
                rank_list.append(count)
            #ブラックジャックの場合、11～13を10にする
            if BlackJack_ON:
                rank_list.append(self.PIPCARD_MAX)
                rank_list.append(self.PIPCARD_MAX)
                rank_list.append(self.PIPCARD_MAX)
            else:
                rank_list.append(self.JACK)
                rank_list.append(self.QUEEN)
                rank_list.append(self.KING)
            self.deck[suit] = rank_list
    
    def draw(self):
        suit = random.choice(list(self.deck.keys()))
        rank = random.sample(self.deck[suit], 1)[0]
        card_info = Card(suit, rank)
        self.deck[suit].remove(rank)
        return card_info
            


