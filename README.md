# WooReadFilter
This is a Python program that could help to compare two fastq files and filt reads with different tags and release only reads with the same tag.

FastQ Screen by Babraham bioinformatics is a nice program that could help to trim reads from unwanted sources. During use 'filter' function of this program for paired-end fastq files, however, might lead to unequal of numbers of reads in new trimmed files, and this would lead to serious troubles in following analysis. For instance, assembly programs such as SPAdes would fail due to unequal reaeds in paired-end files.

To solve this program, I wrote this program to help to find out the differencies of reads in trimmed files and erase them. This program is still a trial, and it might use up part of memory, thus it is suggested to be run in server instead of personal computer, or you may consider to use other program such as TrimGalory instead of FastQ.

In this program, you need to set the addresses of both (yes, only two files are accepted) of your trimmed files, and set the other file name by yourself. The usage is as following:

python WooReadFilter.py -1 filename/file1.tagged.filted.fastq -2 filename/file2.tagged.filted.fastq -o filename/file

Output files are filename/file1.fastq and filename/file2.fastq

The older version would require more memory but less time; the newer one (with "new" in its end) requires much longer time. Both versions could be used but seem not to be so useful, thus you are welcomed to give suggestions about how to better modify this program after your usage.

WU Yuqian from iSynBio, SIAT, PRC in 20180211
