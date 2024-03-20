#Given a DNA sequence, a user should be able to input exon 1 and 2
##start and end points which define the total coding region along the 
##DNA sequence and the percent of the DNA sequence the CR encompasses
dnaSeq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
dnaLength = len(dnaSeq)

##function to ensure valid input is an integer and exons do not overlap
##in reality, exons can potentially overlap due to ORF frames
##for this code's percent sake, we will not consider overlapping ORF's
def valid_input(userinput, min_limit, max_limit):
    while True:
        try:
            val = int(input(userinput))
            if val < min_limit or val > max_limit:
                print(f"This value must be between {min_limit} and {max_limit}.")
            else:
                break
        except ValueError:
            print(f"Please enter a valid integer between {min_limit} and {max_limit}.")
    return val

##calls back the valid_input function and establishes where the exon bounds are
exon1_start = valid_input("Please enter the start postion of the first exon: ", 1, dnaLength - 3)
exon1_end = valid_input(f"Please enter the end postion of the first exon (between {exon1_start + 1} and {dnaLength - 2}): ", exon1_start + 1, dnaLength - 2)
exon2_start = valid_input(f"Please enter the start postion of the second exon (between {exon1_end + 1} and {dnaLength - 1}): ", exon1_end + 1, dnaLength - 1)
exon2_end = valid_input(f"Please enter the end postion of the second exon (between {exon2_start + 1} and {dnaLength}): ", exon2_start + 1, dnaLength)

##new line and printing out the exon regions
print()
print(f"Exon 1 region: {exon1_start} to {exon1_end}")
print(f"Exon 2 region: {exon2_start} to {exon2_end}")

##establishing and coding region and percent and printing result
coding_region = dnaSeq[exon1_start - 1 : exon1_end] + dnaSeq[exon2_start - 1 : exon2_end]
coding_percent = len(coding_region)/dnaLength * 100
print(f"The combined coding region for these 2 exons is {coding_region}")
print(f"This coding region accounts for {coding_percent}% of the total DNA sequence")


##Task is such a user input for two DNA sequences
##check for reverse complementarity
###create library and convert all inputs to upper case
dna1_input = input("Please input your first DNA sequence: ").upper()
dna2_input = input("Please input your second DNA sequence: ").upper()
complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

##generate blank for dna2_comp variable and create a for loop 
##that retreives a value for each key according to the nucleotides in sequence
##and adds them to the dna2_comp variable
dna2_comp = ""
for nuc in dna2_input:
    comp_nuc = complements.get(nuc)
    dna2_comp += comp_nuc

##check reverse of dna2_comp to see if it matches
##note if they are reverse complements dna1_input and dna2_input should not look identicalS
if dna1_input == dna2_comp[::-1]:
    print("Wow! Your two DNA sequences are reverse complements of one another!")
    print(f"5' - {dna1_input} - 3'")
    print(f"3' - {dna2_input[::-1]} - 5'")
else:
    print("These two sequences are not reverse complements to each other.")


