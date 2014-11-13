#  Name: Kevin Hui
#  Email: kvnhui@berkeley.edu


def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


# Q1.

def interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    def confusing(confused):
        if confused:
            return a
        else:
            return b
    return confusing


def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x(1)


def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x(0)

# Q2.

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    "*** YOUR CODE HERE ***"
    assert (lower_bound(y) <= 0 and upper_bound(y) <= 0) or(lower_bound(y) >= 0 and upper_bound(y) >= 0)
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Q3.

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    "*** YOUR CODE HERE ***"
    a = lower_bound(x) - upper_bound(y)
    b = upper_bound(x) - lower_bound(y)
    return interval(a, b)


# Q4.

def mul_interval_fast(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y, using as few multiplications as possible.

    >>> str_interval(mul_interval_fast(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(interval(-2, -1), interval(4, 8)))
    '-16 to -4'
    >>> str_interval(mul_interval_fast(interval(-1, 3), interval(-4, 8)))
    '-12 to 24'
    >>> str_interval(mul_interval_fast(interval(-1, 2), interval(-8, 4)))
    '-16 to 8'
    """
    "*** YOUR CODE HERE ***"
    if lower_bound(x) < 0:
        if upper_bound(x) < 0:
            if lower_bound(y) > 0:
                a = lower_bound(x)*upper_bound(y)
                b = upper_bound(x)*lower_bound(y)
            elif lower_bound(y) < 0 and upper_bound(y) > 0:
                a = lower_bound(x)*upper_bound(y)
                b = lower_bound(x)*lower_bound(y)
            else:
                a = upper_bound(x)*upper_bound(y)
                b = lower_bound(x)*lower_bound(y)
        else:
            if lower_bound(y) > 0:
                a = lower_bound(x)*upper_bound(y)
                b = upper_bound(x)*upper_bound(y)
            elif lower_bound(y) < 0 and upper_bound(y) > 0:
                a = min(lower_bound(x)*upper_bound(y), lower_bound(y)*upper_bound(x))
                b = max(lower_bound(x)*lower_bound(y), upper_bound(x)*upper_bound(y))
            else:
                a = upper_bound(x)*lower_bound(y)
                b = lower_bound(x)*upper_bound(y)
    else:
        if lower_bound(y) > 0:
            a = lower_bound(x)*lower_bound(y)
            b = upper_bound(x)*upper_bound(y)
        elif lower_bound(y) < 0 and upper_bound(y) > 0:
            a = upper_bound(x)*lower_bound(y)
            b = upper_bound(x)*upper_bound(y)
        else:
            a = upper_bound(x)*lower_bound(y)
            b = lower_bound(x)*upper_bound(y)
    return interval(a, b)



# Q5.

def make_center_width(c, w):
    """Construct an interval from center and width."""
    return interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2


def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.

    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    "*** YOUR CODE HERE ***"
    width = p/100 * c
    return make_center_width(c, width)

def percent(x):
    """Return the percentage tolerance of interval x.

    >>> percent(interval(1, 3))
    50.0
    """
    "*** YOUR CODE HERE ***"
    return width(x)/center(x) * 100

# Q6.

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


# These two intervals give different results for parallel resistors:
"*** YOUR CODE HERE ***"
r1 = interval(1,2)
r2 = interval(1,2)

# Q7.

def multiple_references_explanation():
  return """par2 is better because it references the intervals r1 and r2 fewer times than par1. Because par1 references it more, the interval (error) increases with each reference."""

# Q8.


def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    def quad1(t):
        return a*t*t + b*t + c

    extreme = -b/(2*a)
    list = []
    if extreme < upper_bound(x) and extreme > lower_bound(x):
        list.append(quad1(extreme))
    list.append(quad1(lower_bound(x)))
    list.append(quad1(upper_bound(x)))
    high = max(list)
    low = min(list)
    return interval(low, high)

def func(x, a, b, c):
    extreme = -b / (2*a)
    if extreme > upper_bound(x) or extreme < lower_bound(x):
        return interval(min((lower_bound(x)**2 * a + lower_bound(x) * b + c), (upper_bound(x)**2 * a + upper_bound(x) * b + c)), max((lower_bound(x)**2 * a + lower_bound(x) * b + c), (upper_bound(x)**2 * a + upper_bound(x) * b + c)))
    else:
        return interval(min((lower_bound(x)**2 * a + lower_bound(x) * b + c), (upper_bound(x)**2 * a + upper_bound(x) * b + c), (extreme**2 * a + extreme * b + c)), max((lower_bound(x)**2 * a + lower_bound(x) * b + c), (upper_bound(x)**2 * a + upper_bound(x) * b + c), (extreme**2 * a + extreme * b + c)))

# Q9.

def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (interval(-1, 2), make_center_width(-1, 2), make_center_percent(-1, 50))

zero = interval(0, 0)

def sum_nonzero_with_for(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using a for statement.

    >>> str_interval(sum_nonzero_with_for(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"
    sum = zero
    for inter in seq:
        if non_zero(inter):
            sum = add_interval(sum, square_interval(inter))
    return sum

from functools import reduce
def sum_nonzero_with_map_filter_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using map, filter, and reduce.

    >>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"
    filtered = filter(non_zero, seq)
    mapped = map(square_interval, filtered)
    reduced = reduce(add_interval, mapped)
    return reduced


def sum_nonzero_with_generator_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using reduce and a generator expression.

    >>> str_interval(sum_nonzero_with_generator_reduce(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"
    generator = [square_interval(x) for x in seq if non_zero(x)]
    return reduce(add_interval, generator)


# Q10.

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), (-1, 3, -2)))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), (1, -3, 2)))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), (10, 24, -6, -8, 3)))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"


