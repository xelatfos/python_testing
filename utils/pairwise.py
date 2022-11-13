from itertools import chain, combinations, product
import string

def pairwiseGen(*sequences):
    unseen = set(chain.from_iterable(product(*i) for i in combinations(sequences, 2)))
    for path in product(*sequences):
        common_pairs = set(combinations(path, 2)) & unseen
        if common_pairs:
            yield path
            unseen.difference_update(common_pairs)

if __name__ == '__main__':
    print("PAIRWISE:")

    parameters = [
        [ "Brand X", "Brand Y","Brand A","Brand B","Brand C","Brand D" ],
        [ "98", "NT", "2000", "XP"],
        [ "Internal", "Modem","A","B","C","D","E","F","G","H","I","J","K","L","M" ],
        [ "Salaried", "Hourly", "Part-Time", "Contr.","AA","BB","CC","DD","EE","FF","GG","HH","II" ],
        [ 6, 10, 15, 30, 60, 70, 80, 90, 100, 110, 120, 130, 140 ]
    ]

    letters = list(string.ascii_lowercase[:8])
    digits = range(1, 9)
    symbols = list(string.punctuation[:8])
    for (letter, digit,symbols) in product(letters, digits,symbols):
        print(letter+str(digit)+symbols, end=' ')

    pairs = list(pairwiseGen(*parameters)) #[t for t in [s1 for s1 in pairwiseGen(*parameters)]]
    st = ' '.join(str(s)+'\n' for s in pairs)
    print("pairs: ", st)