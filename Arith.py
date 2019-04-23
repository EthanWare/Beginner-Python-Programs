class Arith(object):

    def __init__(self): pass

    @staticmethod
    def add(x, y):
        """
        :param x: first number
        :param y: second number
        :return: returns the product of x and y

        >>> Arith.add(1,1)
        2
        """
        return x + y

    @staticmethod
    def sub(x, y):
        """
        :param x: first number
        :param y: second number
        :return: returns the difference of x and y

        >>> Arith.sub(2,1)
        1
        """
        return x - y

if __name__ == "__main__":
    import doctest
    doctest.testmod()
