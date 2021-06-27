def odd_generator(range_):
    """

    :param range:
    :return: generator
    """
    return (i for i in range(range_ + 1) if i % 2)


if __name__ == '__main__':

    odd_to_15 = odd_generator(15)
    for i in odd_to_15:
        print(i)
    print('*' * 50)
    odd_to_15 = odd_generator(5)
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))