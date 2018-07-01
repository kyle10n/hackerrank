def mutate_string(string, position, character):
    """Take a given string, at an index position,
    replace with character"""

    if position == 0:
        new_string = character + string[1:]

    elif position < len(string):
        new_string = string[0:position] + character + string[position + 1:]

    else:
        new_string = string[0:position - 1] + character

    return new_string


def mutate_string2(string, position, character):
    list2=list(string)
    list2[position]=character
    return ''.join(list2)


print(mutate_string('abracadabra',5,'k'))

print(mutate_string2('abracadabra',5,'k'))
