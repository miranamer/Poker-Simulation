import CheckHands

import random as rd
import matplotlib.pyplot as plt
import math

def main():
    def simulatePokerHands(n):

        Results = {'Royal Flush': 0, 'Straight Flush': 0, 'Four Of A Kind': 0, 'Full House': 0, 'Flush': 0, 'Straight': 0, 'Three Of A Kind': 0, 'Two Pairs': 0, 'One Pair': 0, 'High Card': 0}


        for _ in range(n):
            hand = [] # [[8, 's'], [8, 'c']]
            cc = [] # [[14, 'h'], [12, 's'], [12, 'h'], [14, 'c'], [4, 'd']]

            possible_suits = ['c', 's', 'd', 'h']


            for i in range(7):
                if len(hand) != 2:
                    random_suit_index = rd.randint(0, len(possible_suits) - 1)
                    random_suit = possible_suits[random_suit_index]
                    random_num = rd.randint(1, 14)

                    hand.append([random_num, random_suit])
                else:
                    random_suit_index = rd.randint(0, len(possible_suits) - 1)
                    random_suit = possible_suits[random_suit_index]
                    random_num = rd.randint(1, 14)

                    cc.append([random_num, random_suit])

            #print('Hand -> ', hand)
            #print('CC -> ', cc)

            ranks = {0: 'Royal Flush', 1: 'Straight Flush', 2: 'Four Of A Kind', 3: 'Full House', 4: 'Flush', 5: 'Straight', 6: 'Three Of A Kind', 7: 'Two Pairs', 8: 'One Pair'}

            hand_ranks = [CheckHands.checkRoyalFlush(hand, cc), CheckHands.checkStraightFlush(hand, cc), CheckHands.checkFourOfAKind(hand, cc), CheckHands.checkFullHouse(hand, cc), CheckHands.checkFlush(hand, cc), CheckHands.checkStraight(hand, cc), CheckHands.checkThreeOfAKind(hand, cc), CheckHands.checkTwoPairs(hand, cc), CheckHands.checkPair(hand, cc)] # get index of first True for best 5 card hand

            best_hand = ''

            rank_ptr = 0

            while rank_ptr < len(hand_ranks):
                if hand_ranks[rank_ptr]:
                    best_hand = ranks[rank_ptr]
                    break
                rank_ptr += 1

            if best_hand == '':
                best_hand = 'High Card'

            Results[best_hand] += 1

            if best_hand == 'Royal Flush':
                print('Royal Flush ------> ', hand, cc)

        return Results


    n = int(input('Enter Number Of Simulation Runs: '))

    pokerSim = simulatePokerHands(n)

    plt.bar(range(len(pokerSim)), list(pokerSim.values()), align='center')
    plt.xticks(range(len(pokerSim)), list(pokerSim.keys()), rotation=90, fontsize = 'medium')

    counter = 0
    for i in pokerSim:
        plt.text(counter, pokerSim[i], f'{round((pokerSim[i] / n) * 100, 2)}%', ha = 'center', bbox = dict(facecolor = 'red', alpha =.8))
        counter += 1
    plt.show()

if __name__ == '__main__':
    main()