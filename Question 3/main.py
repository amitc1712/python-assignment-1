def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


if __name__ == "__main__":
    input_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    result_list = f7(input_list)
    print(result_list)
