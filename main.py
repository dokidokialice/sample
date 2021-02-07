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

import Player
import Dealer

ore = Player.Player()
omae = Dealer.Dealer()
add_draw_p = True
add_draw_d = True
while True:
    if add_draw_p: 
        text = input('hit or stay?\n')
        if text == 'hit':
            card = ore.deck.draw()
            ore.hand.add(card.suit, card.rank)
            print(ore.hand.count())
        else:
            add_draw_p = False
    if add_draw_d:
        add_draw_d = omae.play()
    if (not add_draw_p) and (not add_draw_d):
        break
    
print(ore.hand.count())
print(omae.hand.count())
ore_count = ore.hand.count()
omae_count = omae.hand.count()
win = (ore_count < 22)
if win:
    win = (omae_count - 21) > 0
    if not win:
        win = (ore_count - 21) > (omae_count - 21)
if win:
    print('You Win!')
else:
    print('You Lose...')

