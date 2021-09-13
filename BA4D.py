"""
A solution to a Rosalind bioinformatics problem
Problem Title: Compute the Number of Peptides of Given Total Mass 
Rosalind ID: BA4D
URL: http://rosalind.info/problems/ba4d/
"""
def get_amino_acid_mass():
    mass = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }

    return mass

def get_all_combinations_worker(mass, aa_masses, counter):
    if mass in counter:
        return counter[mass]

    if mass < 0:
        return 0

    if mass == 0:
        return 1

    counter[mass] = 0
    for aa_mass in aa_masses:
        counter[mass] += get_all_combinations_worker(mass - aa_mass, aa_masses, counter)

    return counter[mass]


def get_all_combinations(mass):
    aa_masses = set(get_amino_acid_mass().values())
    counter = {}

    res = get_all_combinations_worker(mass, aa_masses, counter)

    # print({k: v for k,v in counter.items() if v!=0})

    return res

x=1024
result=get_all_combinations(x)
print(result)
