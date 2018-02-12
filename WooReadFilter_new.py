import argparse
import os
import screed

parser = argparse.ArgumentParser(description='WooRead - A tool to filt unequal reads from FastQ Screen. '
                                             'For research team of Dr. Liu in iSynBio, SIAT only. '
                                             'Usage: python WooRead.py '
                                             '-1 file/name1.tagged_filter.fastq -2 file/name2.tagged_filter.fastq '
                                             'Output: file/name_1.fastq file/name_2.fastq '
                                             'Copyleft: Jacky Woo from ZHK Research team, iSynBio, SIAT.')
parser.add_argument('-1', '--input_file_1', type=str, help='Input FASTQ file R1')
parser.add_argument('-2', '--input_file_2', type=str, help='Input FASTQ file R2')
parser.add_argument('-o', '--output_file', type=str, help='Output FASTQ file prefix (Default: input name and file)')

args = parser.parse_args()
print 'Thank you for use WooRead! You set input %s, %s and output %s' % (
    args.input_file_1, args.input_file_2, args.output_file)
main_dict = [[], [], []]
for count, seq in enumerate([args.input_file_1, args.input_file_2]):
    seqfile = open(seq)
    for read in seqfile:
        if not count:
            main_dict[0] += [read.name.split(' ')[0]]
            main_dict[1] += [read]
            main_dict[2] += [None]
        elif read.name.split(' ')[0] in main_dict[0]:
            main_dict[2][main_dict[0].index(read.name.split(' ')[0])] = read
    seqfile.close()
outfh_1 = open(args.output_file + '1.fastq', 'w')
outfh_2 = open(args.output_file + '2.fastq', 'w')
for co, item in enumerate(main_dict[2]):
    if item:
        for count, counter in enumerate([outfh_1, outfh_2]):
            p = '@' + main_dict[count + 1][co]['name'].split('#')[0] + '\n' + main_dict[count + 1][co]['sequence'] + \
                '\n+\n' + main_dict[count + 1][co]['quality'] + '\n'
            counter.write(p)
outfh_1.close()
outfh_2.close()
print 'WooRead finished!'
