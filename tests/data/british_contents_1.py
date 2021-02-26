
def acclimatise():
    """
    A function to print the word acclimatise.
    """
    print('acclimatise')


def variable_names():
    """

    :return:
    """
    agonise = 1
    labour = 2
    cypher = 3

    return agonise + labour + cypher


def argument_definitions(defence, epilogue, familiarise):
    """

    :param defence:
    :param epilogue:
    :param familiarise:
    :return:
    """

    print(familiarise, epilogue, defence)


def main():
    acclimatise()
    assert variable_names() == 6
    argument_definitions(
        defence='runs',
        epilogue='test ',
        familiarise='This ',
    )


if __name__ == '__main__':
    main()
