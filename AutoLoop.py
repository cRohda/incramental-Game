import Game as g
from time import sleep

while True:
    x = float(g.pps['text'])
    total_wealth = float(g.wealth['text'])
    g.wealth['text'] = f'{total_wealth + x}'
    print(g.wealth)
    sleep(1)
