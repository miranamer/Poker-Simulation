def checkRoyalFlush(hand, cc):
    combined = hand+cc
    combined = sorted(combined, key=lambda x: x[0])

    suits = {'c': 0, 's': 0, 'h': 0, 'd': 0}
   
    for i in combined:
        suits[i[1]] += 1
   
    suits = sorted(suits.items(), key=lambda item: item[1], reverse=True)

   
    majority_suit = suits[0][0]
   
    if suits[0][1] < 5: # need at least 5 same suit for flush
        return False
   
    only_possible = [i[0] for i in combined if i[1] == majority_suit]

    return list(set(only_possible)) == [10, 11, 12, 13, 14]
   


def checkStraightFlush(hand, cc):
    
    if not checkStraight(hand,cc):
        return False

    combined = hand+cc
    combined = sorted(combined, key=lambda x: x[0])

    suits = {'c': 0, 's': 0, 'h': 0, 'd': 0}
   
    for i in combined:
        suits[i[1]] += 1
   
    suits = sorted(suits.items(), key=lambda item: item[1], reverse=True)

    majority_suit = suits[0][0]
   
    if suits[0][1] < 5: # need at least 5 same suit for flush
        return False

    only_possible = [i for i in combined if i[1] == majority_suit] # all same suit

    ptr = 0

    while ptr < len(only_possible):
        if only_possible.count(only_possible[ptr]) > 1:
            del only_possible[only_possible.index(only_possible[ptr])]
        else:
            ptr += 1

    num_only = [i[0] for i in only_possible]

    start_ind, end_ind = 0, 4

    straight_flag = False

    for _ in range(len(num_only) - 4):
        five_seq = num_only[start_ind:end_ind+1]
       
        gauss_sum = int((5 / 2) * (five_seq[0] + (five_seq[0] + 4)))

        if gauss_sum == sum(five_seq):
            straight_flag = True
            break
       
        start_ind += 1
        end_ind += 1

    return straight_flag



def checkFourOfAKind(hand, cc):
    combined = [i[0] for i in hand+cc]
   
    for i in combined:
        if combined.count(i) == 4:
            return True
    return False

def checkFullHouse(hand, cc):
    combined = [i[0] for i in hand+cc]
    count = {}
   
    for i in combined:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
   
    checks = [3, 2]
   
    for i in count:
        if count[i] in checks:
            del checks[checks.index(count[i])]
   
    if len(checks) == 0:
        return True
    return False
           
   

def checkFlush(hand, cc):
    combined = hand+cc

    count = {}

    for i in combined:
        if i[1] in count:
            count[i[1]] += 1
        else:
            count[i[1]] = 1

    for i in count:
        if count[i] >= 5:
            return True

    return False

def checkStraight(hand, cc):
    sorted_set = sorted(hand+cc, key=lambda x: x[0])
    num_only = list(set([i[0] for i in sorted_set]))

    if len(num_only) < 5:
        return False

    start_ind, end_ind = 0, 4

    straight_flag = False

    for _ in range(3):
        five_seq = num_only[start_ind:end_ind+1]

        gauss_sum = int((5 / 2) * (five_seq[0] + (five_seq[0] + 4)))

        #print(five_seq, gauss_sum)
        if gauss_sum == sum(five_seq):
            #print('TRUE', five_seq, gauss_sum)
            straight_flag = True
            break
       
        start_ind += 1
        end_ind += 1
   
    return straight_flag

def checkThreeOfAKind(hand, cc):
    combined = [i[0] for i in hand+cc]
   
    for i in combined:
        if combined.count(i) == 3:
            return True
    return False

def checkTwoPairs(hand, cc):
    combined = [i[0] for i in hand+cc]
   
    count = {}

    for i in combined:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    counter = 0

    for i in count:
        if count[i] == 2:
            counter += 1
    
    if counter >= 2: # 2 or more than 2 pairs
        return True
    return False

def checkPair(hand, cc):
    combined = [i[0] for i in hand+cc]
   
    count = {}

    for i in combined:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    counter = 0

    for i in count:
        if count[i] == 2:
            counter += 1
    
    if counter >= 1:
        return True
    return False