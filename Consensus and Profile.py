# Problem
#
# A matrix is a rectangular table of values divided into rows and columns. An m×n
# matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j
# Say that we have a collection of DNA strings, all having the same length n
# . Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the j
# th position, and so on (see below)
# A consensus string c
# is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j
# -th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.
# DNA Strings
# 	A T C C A G C T
# 	G G G C A A C T
# 	A T G G A T C T
#   A A G C A A C C
# 	T T G G A A C T
# 	A T G C C A T T
# 	A T G G C A C T
# Profile
# 	A   5 1 0 0 5 5 0 0
#   C   0 0 1 4 2 0 6 1
# 	G   1 1 6 3 0 1 0 0
# 	T   1 5 0 0 0 1 1 6
# Consensus
#   A T G C A A C T
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
# Sample Dataset
# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT
# Sample Output
# ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6
import re
input_file = open('FASTA_dataset.txt')
init_string = input_file.read()
string = ''.join(re.split(r'\n', init_string))
dict_fasta = []
while re.match(r'>Rosalind_\d*', string) is not None:
    match = re.match(r'>Rosalind_\d*', string).group(0)
    string = string.replace(match, '')
    match2 = re.match(r'\w*', string).group(0)
    dict_fasta.append(match2)
    length_of_matrix = len(match2)
    string = string.replace(match2, '')
profile_matrix = {'A': [0] * length_of_matrix, 'C': [0] * length_of_matrix, 'G': [0] * length_of_matrix, 'T': [0] * length_of_matrix, }
for genome_word in dict_fasta:
    for index_genome_char in range(length_of_matrix):
        profile_matrix[genome_word[index_genome_char]][index_genome_char] += 1
consensus = [0]*length_of_matrix
consensus_word = ['']*length_of_matrix
consensus_dict = {0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T'}
list_of_values = list(profile_matrix.values())
# print(list_of_values)
for index_type_of_genome in range(4):
    for index_count_genome in range(length_of_matrix):
        if list_of_values[index_type_of_genome][index_count_genome] > consensus[index_count_genome]:
            consensus[index_count_genome] = list_of_values[index_type_of_genome][index_count_genome]
            consensus_word[index_count_genome] = consensus_dict[index_type_of_genome]
result = ''.join(consensus_word)
result += "\nA: " + ' '.join(map(str, (list_of_values[0])))
result += "\nC: " + ' '.join(map(str, (list_of_values[1])))
result += "\nG: " + ' '.join(map(str, (list_of_values[2])))
result += "\nT: " + ' '.join(map(str, (list_of_values[3])))
print(result)
input_file.close()