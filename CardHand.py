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

class CardHand:

    def __init__(self):
        self.hand = {}
        self.hand['spade'] = []
        self.hand['heart'] = []
        self.hand['club'] = []
        self.hand['diamond'] = []

    def add(self, suit: str, rank: int):
        self.hand[suit].append(rank)
    
    def remove(self, suit: str, rank: int):
        self.hand[suit].remove(rank)

    def count(self):
        count = 0
        for suit in self.hand:
            for rank in self.hand[suit]:
                count += rank
        return count
