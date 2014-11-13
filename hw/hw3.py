#  Name: Kevin Hui
#  Email: kvnhui@berkeley.edu

# Q1.

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n > 3:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)
    else:
        return n

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <=3:
        return n
    counter = 3
    n1, n2, n3 = 3, 2, 1
    while counter < n:
        n1, n2, n3 = n1 + 2*n2 + 3*n3, n1, n2
        counter += 1
    return n1

# Q2.

def has_seven(k):
    """Has a has_seven
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k % 10 == 7:
        return True
    if k // 10 == 0:
        return False
    else:
        return has_seven(k//10)

# Q3.

"1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    def helper_pingpong(current, count, up):
        if count == n:
            return current
        else:
            if(count+1)%7 == 0 or has_seven(count+1):
                if up:
                    return helper_pingpong(current+1, count+1, False)
                else:
                    return helper_pingpong(current-1, count+1, True)
            else:
                if up:
                    return helper_pingpong(current+1, count+1, True)
                else:
                    return helper_pingpong(current-1, count+1, False)
    return helper_pingpong(0, 0, True)

# Q4.

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def helper_ten(x, y):
        if y == 0:
            return 0
        elif y%10 == (10-x):
            return 1 + helper_ten(x, y//10)
        else:
            return helper_ten(x, y//10)
    if n<10:
        return 0
    else:
        return helper_ten(n%10, n//10) + ten_pairs(n//10)

# Q5.

from math import log, sqrt, pow

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    coin = 1
    while coin < amount:
        coin *= 2
    coin = coin // 2

    def partition(amount, coin):
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        elif coin == 1:
            return 1
        else:
            return partition(amount - coin, coin) + partition(amount, coin//2)

    return partition(amount, coin)

# Q6.

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return YOUR_EXPRESSION_HERE

