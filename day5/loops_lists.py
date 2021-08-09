import random
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """

    for num in nums:
        if num % 7 == 0 and num>0:
            return True
    if len(nums) < 1:
        return False
    else:
        return False

a = [1,2,3,7,2,14]
b = []
c = [1,2,4]
print(has_lucky_number(a))
print(has_lucky_number(b))
print(has_lucky_number(c))


def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is
    True if L[i] is greater than thresh, and False otherwise.

    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    results = []
    for element in L:
        if element > thresh:
            results.append(True)
        else:
            results.append(False)
    return results


def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    i = 0
    total = 0
    payout = random.gauss(-n_runs, n_runs)
    while i < n_runs:
        total *= payout
        i += 1
    return total
print(estimate_average_slot_payout(50))

meals=['Spam', 'Eggs', 'Spam', 'Spam', 'Bacon', 'Spam']
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for meal in meals:
        for item in meals:
            if meal == item and meals.index(meal) != meals.index(item):
                return True
    return False
print(menu_is_boring(meals))