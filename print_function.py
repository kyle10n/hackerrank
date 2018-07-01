if __name__ == '__main__':
    n = int(input())

    empty_list = []

    counter = 0
    while counter < n:
        empty_list.append(counter)
        counter = counter + 1

    empty_list.append(n)

    new_string = map(str,empty_list)

    new_string = ''.join(new_string)

    new_number = int(new_string)

    print(new_number)