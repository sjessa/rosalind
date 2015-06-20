s = 'CGAGTCTCGTAGCATGGGGCATCCTACATATCTTGCGTCATCTGTGGTGAAGCCAACCTTGATCGAGTTTCTATCCTTTTTTAACGTGGTAATCCAGACACATATAAGGCAGGAGGGTCGGTATTGATTTAGCCCTACTAGCCACGCTAAAGACCGCCGACCTTAGCTCTAAAGCAGGCAAGATACGAACTCGCGCAATGCGTCACTACAGGACACAACGAAGCATGTCCCTGTCATACTGTGAAGGCTGGGGAGGTCTGAGTTAGATGGATAGAAGTGTTGCCCATAAACTATCACCCTAGTATGCTAGCAACGACCCGGAACAATAACTCTCCGCACCGACAAAGGTGTCCCCACCAAACAGTGCGAATTTTGGGATAAATGTCGAATGCTTCTTGGAAGGTGTCCAAGAAGCAATGTCTGTATGTCCAAGGTACAACTTGGAGACGGGTCTGCCCATATCGTCAGGAGCGGAGACATGAAAGAAGTGCAAGGGAGGTAAGGCACCCCTCCAACCCATGCCTTAAGGGTATGTCGATACAATGGTGTGGTAATCTGGAATTAAGGCAACAGCGGGAATCATGGCAATGATGGTAGGCAGGAACTTAGAATGAGAGACGCAAGTTGTCGCCAGTAACTCTCAAAGAAGCGTTGGAGTCCGGTGTTCAGAGCCAGCTCTGCGTAACTGATTGTGAGGACAGATAATGAGTTTACAATGGGTACAGCAACGGACTCTAACTGTCACACATAAAAATCCGTTAGAGCCGTAGTAACGTAGACTAAGCAGACACATACTATCTTTTGCTTCCTCTGGCGAAGGTCTAAAATAATCCATGGAGAAGATCCGCTAATGCACGAGGTCAAACGTAACATGGGCACGGCACAGCCGTTGCGTTTTCTCCATGTGCGCGTCCTCGTTGGAGATGATCGTAGCCTAG'



slist = list(s)
index = 0

#print slist

for nt in s:
    if nt == 'A':
        slist[index] = 'T'
    if nt == 'T':
        slist[index] = 'A'
    if nt == 'C':
        slist[index] = 'G'
    if nt =='G':
        slist[index] = 'C'
    index = index + 1

#print slist
scomp = ''.join(slist)
#print scomp
srevcomp = scomp[::-1]
print srevcomp