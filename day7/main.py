
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for j in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        elif racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} racer = {}".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts


def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    total_hand_1 = 0
    total_hand_2 = 0
    for i in hand_1:
        if i == "A":
            if total_hand_1 <= 10:
                total_hand_1 += 11
            else:
                total_hand_1 += 1
        elif i == "K" or i == "J" or i == "Q":
            total_hand_1 += 10
        else:
            total_hand_1 += int(i)
    for i in hand_2:
        if i == "A" :
            if total_hand_2 <= 10:
                total_hand_2 += 11
            else:
                total_hand_2 += 1
        elif i == "K" or i == "J" or i == "Q":
            total_hand_2 += 10
        else:
            total_hand_2 += int(i)
    if total_hand_1 > total_hand_2 and total_hand_1 <= 21:
        return True
    else:
        return False
print(blackjack_hand_greater_than(['K'], ['3', '4']))
print(blackjack_hand_greater_than(['K'], ['10']))
print(blackjack_hand_greater_than(['9'], ['9', 'Q', '8', 'A']))