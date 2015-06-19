
def sum_squares(n):
    """
    This function calculate the sum of the square of the first n natural numbers.
    """
    return sum(map(lambda x : x**2, range(1, n+1)))

def squares_sum(n):
    """
    This function calculate the square of the sum of the first n natural numbers.
    """
    return sum(range(1, n+1))**2

def get_diff(n):
    """
    This function calculate the difference between the sum of the squares of the first n
    natural numbers and the square of the sum.
    """
    return squares_sum(n) - sum_squares(n)
