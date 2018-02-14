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
parser.add_argument('-o', '--output_file', type=str, required=False,
                    help='Output FASTQ file prefix (Default: input name and file)')

args = parser.parse_args()
if args.output_file is not None:
    outfile_1 = args.output_file + '_1.fastq'
    outfile_2 = args.output_file + '_2.fastq'
else:
    outfile_1 = args.input_file_1.rsplit('.tagged_filter.fastq')[0] + '_1.fastq'
    outfile_2 = args.input_file_2.rsplit('.tagged_filter.fastq')[0] + '_2.fastq'
print 'Thank you for use WooRead! You set input %s, %s and output %s, %s' % (
    args.input_file_1, args.input_file_2, outfile_1, outfile_2)
fq_file_1 = args.input_file_1
fq_file_2 = args.input_file_2
main_dict = {}
list_1 = []
list_2 = []
with screed.open(fq_file_1) as seqfile_1:
    counter = 0
    for read in seqfile_1:
        counter += 1
        main_dict.update({read.name.split(' ')[0]: [read, None]})
        list_1 += [(counter, read.name.split(' ')[0])]
with screed.open(fq_file_2) as seqfile_2:
    counter = 0
    for read in seqfile_2:
        counter += 1
        list_2 += [(counter, read.name.split(' ')[0])]
        if read.name.split(' ')[0] in main_dict:
            main_dict[read.name.split(' ')[0]][1] = read
list_1.sort()
list_2.sort()
outfh_1 = open(outfile_1, 'w')
outfh_2 = open(outfile_2, 'w')
for item in list_1:
    if main_dict[item[1]][0] is not None and main_dict[item[1]][1] is not None:
        p = '@' + main_dict[item[1]][0]['name'].split('#')[0] + '\n' + main_dict[item[1]][0][
            'sequence'] + '\n+\n' + main_dict[item[1]][0]['quality'] + '\n'
        outfh_1.write(p)
        p = '@' + main_dict[item[1]][1]['name'].split('#')[0] + '\n' + main_dict[item[1]][1][
            'sequence'] + '\n+\n' + main_dict[item[1]][1]['quality'] + '\n'
        outfh_2.write(p)
outfh_1.close()
outfh_2.close()
print 'WooRead finished!'
