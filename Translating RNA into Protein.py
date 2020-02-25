# Problem
# The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.
# The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.
# Given: An RNA string s
# corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s
# Sample Dataset
# AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
# Sample Output
# MAMAPRTEINSTRING
input_file = open("file.txt")
dataset = input_file.read()
RNA_codon_file = open("RNA_codon_dict.txt")
output_file = open("result.txt", "w")
string = ' '.join('  '.join(RNA_codon_file.read().split("\n")).split()).split()
RNA_codon_dict = {}
result = ''
for index in range(0, len(string), 2):
    RNA_codon_dict[string[index]] = string[index + 1]
for index in range(0, len(dataset), 3):
    sample = dataset[index:index+3]
    if RNA_codon_dict[sample] == 'Stop':
        break
    else:
        result += RNA_codon_dict[sample]
print(result)
output_file.write(result)
input_file.close()
output_file.close()