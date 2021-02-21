'''
abracadabra
5 k
The first line contains a string, .
The next line contains an integer , denoting the index location and a character
 separated by a space.

'''


def mutate_string(string, position, character):
    listed = list(string)

    listed[int(position)] = character
    string = ''.join(listed)
    return string


mutate_string('abracadabra', '5', 'k')
