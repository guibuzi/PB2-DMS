"""
This script subsamples an alignment to create small alignments with only
one sequence per year.

The sequences are assumed to follow a naming scheme similar to the IVR.
Other naming schemes may lead to incorrect parsing of the year.

This script is also written specifically for H1N1 sequences. That is, it
        assumes all sequences are collected between 1918 and 2009.
SS, 20180320: I modified this script to collect all sequences between 1918 and 2018.


The general procedure is to
1. Shuffle the sequences
2. Extract the date from each sequece header and make a dictionary of lists
        of sequences keyed by the year
3. For each final alignment, loop through the years and take one sequence.
4. Output the final alignments


SKH, Jan 2017
"""
import argparse
from Bio import SeqIO
import random
import re
import sys

class ArgumentParserNoArgHelp(argparse.ArgumentParser):
    """Like *argparse.ArgumentParser*, but prints help when no arguments."""
    def error(self, message):
        sys.stderr.write('error: %s\n\n' % message)
        self.print_help()
        sys.exit(2)

def ParseArguments():
    """Argument parser for script."""
    parser = ArgumentParserNoArgHelp(
            description='Subsample IVR H3N2 alignment',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            )
    parser.add_argument('IVRseqs', help='File IVR alignment.')
    parser.add_argument('alignmentNumber', type=int, help='Total number of final alignments.')
    parser.add_argument('outPrefix', help='Prefix for created alignment files')
    return parser

def createDateDictionary(sequences):
    """
    This function organizes the sequences by year of collection.

    This function assumes that for a sequence collected in 2000 there is a string
            '2000_2000' somewhere in the header.

    A list of headers which cannot be parsed will be printed at the end.

    input: list of BioPython records
    output: dictionary keyed by date with a
            list of sequence records from that year.
    """
    seed = 1
    random.seed(seed)
    random.shuffle(sequences)
    datesDictionary = {}

    for seq in sequences: #go through each sequence
        regex = r"(/\d+_+\d+/)" #look for dates
        match = re.search(regex, seq.id)
        if match: # if a date is found, extract the exact date
            print(match)
            match = re.search(r"(\d\d\d\d)", (match.group(0)))
            print(match)
            if match:
                year =  int(match.group(0))
                if year not in range(1918,2019): #make sure the extracted date makes sense
                    print("wrong parse of year", seq.id)
                elif year in datesDictionary.keys(): #add sequence to the dictionary
                    datesDictionary[year].extend([seq])
                else:
                    datesDictionary[year] = [seq]
        else: #if date is not found
            print("Couldn't parse", seq.id)

    dates = list(datesDictionary.keys())
    dates.sort() #sort the dates
    print
    print("The years in the alignment are: ",dates)
    print(len(dates))
    oneSeqYears = []
    for year in datesDictionary.keys():
        if len(datesDictionary[year]) ==1:
            oneSeqYears.append(year)
    oneSeqYears.sort()
    print
    print("There are {0} year(s) with only one sequence".format(len(oneSeqYears)))
    for one in oneSeqYears:
        print(one)
    return datesDictionary

def createAlignments(finalNumber,dates):
    """
    The function defines which sequences end up in each final alignment.

    As the sequnces have already been randomized and sorted, the first alignment
        gets the first sequence for the year, the second alignment gets the
        second sequence for the year, etc.

    input: total number of alignments, dictionary of sequences by date
    output: A list of lists the length of the total number of alignments.
            Each list contains the exact same number of sequences.
    """

    finalSequences = [[] for x in range(finalNumber)] #make the list of lists

    for date in dates.keys(): #assign sequences to each alignment
        if len(dates[date]) >= finalNumber: #
            for i in range(finalNumber):
                finalSequences[i].append(dates[date][i])
        else:
            repeat =  int(finalNumber / len(dates[date]))\
                + (finalNumber % len(dates[date]) > 0)
            temp = list(range(len(dates[date]))) * repeat
            for i in range(finalNumber):
                finalSequences[i].append(dates[date][temp[i]])

    assert len([len(l) for l in finalSequences]) == finalNumber #all alignments should have the same number of sequences
    assert len(set([len(l) for l in finalSequences])) == 1 #all sequences should be the same length
    assert len(finalSequences[0]) == len(dates.keys()) #each alignment should have one squence per year

    return finalSequences

def main():
    #read in arguments
    args = vars(ParseArguments().parse_args())
    print("Read the following command line arguments:")
    print("\t{0}".format("\n\t".join(["{0} = {1}".format(key, value) for (key, value) in args.items()])))

    #main functions for alignment creation
    IVRrecords = list(SeqIO.parse(args['IVRseqs'], "fasta")) #read in the large alignment
    dates = createDateDictionary(IVRrecords) #organize the sequences by date
    finalSeqs = createAlignments(args['alignmentNumber'], dates) #sort sequences into alignments

#     #summary of overlap between the sequences
#     for i in range(len(finalSeqs)):
#         for j in range(i+1, len(finalSeqs)): #for each pair of alignments
#             overlap =  [x.id for x in finalSeqs[i]] #seq ids in the first alignment
#             overlap.extend([x.id for x in finalSeqs[j]]) #seq ids in the second alignment
#             assert len(overlap) == 2 * len(dates.keys()) #make sure all the seq ids were counted
#             overlap = list(set([x for x in overlap if overlap.count(x) == 2])) #count the overlap
#             print("The overlap between alignment {0} and alignment {0} is {2}.".format(i,j,len(overlap)))
#             print("The sequences are {0}".format(",".join(overlap)))
#             print

    #output the alignments.
    for i in range(len(finalSeqs)):
        n = args['outPrefix']+"_"+str(i)+".fa"
        SeqIO.write(finalSeqs[i], n, "fasta")

if __name__ == '__main__':
	main() # run the script
