#reiksmiu_sukeitimas.py
active_player = '1'
passive_player = 'ABC'
active_player, passive_player = passive_player, active_player
active_player = passive_player
passive_player = active_player
print(active_player)