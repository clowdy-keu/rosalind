# Problem
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
# Sample Dataset
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT
# Sample Output
# Rosalind_0808
# 60.919540
import re
input_file = open('FASTA_dataset.txt')
init_string = input_file.read()
string = ''.join(re.split(r'\n', init_string))
dict_fasta = {}
while re.match(r'>Rosalind_\d{4}', string) is not None:
    match = re.match(r'>Rosalind_\d{4}', string).group(0)
    string = string.replace(match, '')
    match2 = re.match(r'\w*', string).group(0)
    dict_fasta[match] = match2
    string = string.replace(match2, '')
highest_gc = 0
name_dataset = ''
for elem in dict_fasta:
    temp_gc = 0
    for char in dict_fasta[elem]:
        if char == 'C' or char =='G':
            temp_gc += 1
    if temp_gc/len(dict_fasta[elem])*100 > highest_gc:
        highest_gc = temp_gc/len(dict_fasta[elem])*100
        name_dataset = elem
print(name_dataset[1:], highest_gc, sep = '\n')
input_file.close()