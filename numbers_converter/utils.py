J = ('', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć', 'dziesięć', 'jedenaście',
     'dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście', 'osiemnaście',
     'dziewiętnaście')
D = ('', 'dziesięć', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt',
     'osiemdziesiąt', 'dziewięćdziesiąt')
S = ('', 'sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset')
T = ('', 'tysiąc', 'tysiące', 'tysięcy')
NAMES = ('', '', 'y', 'ów')
M = ('', 'milion', 'miliony', 'milionów',)
Mi = ('', 'miliard', 'miliardy', 'miliardów',)
B = ('', 'bilion', 'biliony', 'bilionów',)
Bi = ('', 'biliard', 'biliardy', 'biliarów',)
Tr = ('', 'trylion', 'tryliony', 'trylionów',)
G = ('', T, M, Mi, B, Bi, Tr)


def cut_on_group(list_number):
    list_number = list_number[::-1]
    i = 0
    a = []
    while len(list_number[i:i + 3]) != 0:
        b = list_number[i:i + 3]
        a.append(b[::-1])
        i += 3
    return a[::-1]


def group_to_str(list_number):
    string_number = ''
    int_number = int("".join([str(x) for x in list_number[-2:]]))

    if len(list_number) == 3:
        string_number += '%s ' % S[list_number[0]]

    if int_number < 20:
        string_number += J[int_number]
    else:
        string_number += ' '.join((D[list_number[-2]], J[list_number[-1]]))

    return ' ' + string_number + ' '


def get_group_name(group, list_number):
    if group == 0:
        return ''

    j = list_number[-1]
    int_number = int("".join([str(x) for x in list_number[-3:]]))

    if int_number == 0:
        return ''

    if int_number == 1:
        return G[group][1]

    if 5 <= int_number <= 21:
        return G[group][3]

    if 2 <= j <= 4:
        return G[group][2]
    return G[group][3]
