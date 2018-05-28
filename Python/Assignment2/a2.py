def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    dna_length = len(dna)
    return dna_length


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    if len(dna1) > len(dna2):
        return True
    else:
        return False
    

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna1.count(dna2):
        return True
    else:
        return False


def is_valid_sequence(dna_seq):
    """ (str) -> bool

    Return True iff DNA sequence dna_seq is valid (that is, it contians no
    characters other than A T C G or contains lowercase letters.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGCXS')
    False
    >>> is_valid_sequence('ATCgT')
    False
    
    """

    valid = True
    for nucl in dna_seq:
        if nucl not in 'ATCG': #valid string
            valid = False

    return valid

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence dna2
    into the first DNA sequence dna1 at the given index 'index'.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 0)
    'ATCCGG'
    >>> insert_sequence('CCGG', 'AT', 3)
    'CCGATG'
    
    """

    if index > len(dna1):
        return "Please, provide a valid index."

    dna3 = dna1[:index] + dna2 + dna1[index:]
    return dna3


def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement by providing a nucleotide. For 'A', it is
    'T', for 'T'-'A', for 'C'-'G', for 'G'-'C'

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    
    """

    if nucleotide not in 'ATCG':
        return "Please, provide a valid nucleotide."
    else:
        if nucleotide == 'A':
            return 'T'
        elif nucleotide == 'T':
            return 'A'
        elif nucleotide == 'C':
            return 'G'
        elif nucleotide == 'G':
            return 'C'

def get_complementary_sequence(dna_seq):
    """ (str) -> (str)

    Return the DNA sequence that is complementary to the given DNA sequence dna_seq.

    >>> get_complementary_sequence('AT'):
    'TA'
    >>> get_complementary_sequence('GCAT'):
    'CGTA'

    """

    complementary_dna = ''
    if not is_valid_sequence(dna_seq):
        return 'Please provide a valid DNA sequence'
    
    for nucleotide in dna_seq:
        complementary_dna = complementary_dna + get_complement(nucleotide)

    return complementary_dna
        
