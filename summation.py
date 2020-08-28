"""
Sum a list of things
"""


def mysum(*numbers, start=0):
    """
    Sum a list of things
    """
    output = start
    for num in numbers:
        output += num
    return output


def myavg(*numbers):
    """
    Average numbers
    """
    return mysum(*numbers)/len(list(numbers))


def wordstats(*words):
    """
    Stats of words
    """
    wordlens = sorted(len(word) for word in words)
    return wordlens[-1], wordlens[-1], myavg(*wordlens)


if __name__ == "__main__":
    print(mysum(*range(101)))
