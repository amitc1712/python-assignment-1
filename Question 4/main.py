def question4():
    return list(map(lambda x: x**2, range(1, 21)))


if __name__ == "__main__":
    squares = question4()
    print("List of squares of numbers between 1 and 20 (both included): ", squares)
