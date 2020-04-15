#!/usr/bin/python3
import argparse
#argument parsing
parser = argparse.ArgumentParser(description='Convert Fasta sequence file with bed and gtf features to geneBank flat format.')
parser.add_argument('-f', '--fasta', help='Input fasta file with single sequence line after header.')
parser.add_argument('-b', '--bed', help='Bed file of features on fasta file.')
parser.add_argument('-g', '--gtf', help='Gtf file of features on fasta file.')
parser.add_argument('-n', '--name', help='Name of stored sequence and region.')
parser.add_argument('-o', '--organism', help='Name of organism.')
parser.add_argument('-a', '--author', default='FASTA & BED to GeneBank GBK script', help='Authors name. Default is \"FASTA & BED to GBK script\".')
parser.add_argument('-t', '--molecule_type', default='genomic DNA', help='Type of molecule. Default is \"genomic DNA\"')
args = parser.parse_args()
#preparing input files
#fasta file
input_fasta_file = open("./{}".format(args.fasta))
input_fasta = input_fasta_file.read()
header = input_fasta.splitlines()[0]
fasta = input_fasta.splitlines()[1]
result0 = []
for i in range(0, len(fasta), 10):
   result0.append(fasta[i:i+10].lower())
#bed file
input_bed_file = open("./{}".format(args.bed))
bed_lines = input_bed_file.read().splitlines()
result_bed = []
for b in bed_lines:
    result_bed.append(b.split("\t"))
#gtf file
input_gtf_file = open("./{}".format(args.gtf))
gtf_lines = input_gtf_file.read().splitlines()
result_gtf = []
for g in gtf_lines:
    result_gtf.append(g.split("\t"))

#writing GBK file into a variable
result1 = []
result1.append("LOCUS       {0}               {1} bp ds-DNA     linear".format(header[1:], len(fasta)))
result1.append("DEFINITION  }".format(args.name))
result1.append("ACCESSION   .")
result1.append("VERSION     .")
result1.append("KEYWORDS    {}".format(args.name))
result1.append("SOURCE      natural DNA sequence")
result1.append("  ORGANISM  {}".format(args.organism))
result1.append("REFERENCE   1  (bases 1 to {})".format(len(fasta)))
result1.append("  AUTHORS   {}".format(args.author))
result1.append("  TITLE     {} locus GenBank formatted file".format(args.name))
result1.append("  JOURNAL   Unpublished")
result1.append("FEATURES             Location/Qualifiers")
result1.append("     source          1..{}".format(len(fasta)))
result1.append("                     /organism=\"{}\"".format(args.organism))
result1.append("                     /mol_type=\"{}\"".format(args.molecule_type))
for i in result_bed:
    result1.append("     misc_feature    {0}..{1}".format(str(int(i[1])+1), i[2]))
    result1.append("                     /label=\"{}\"".format(i[3]))
for i in result_gtf:
    result1.append("     exon            {0}..{1}".format(i[3], i[4]))
    result1.append("                     /label=\"{}\"".format(i[8].split("\"")[5]))
result1.append("ORIGIN")
#Next block has an issue that the number of nucleotides is not calculated correctly
for h, i in zip(range(1, len(fasta), 60), range(0, len(result0), 6)):
        result1.append("{:>9}".format(str(h)) + " " + " ".join(result0[i:i+6]))
result1.append("//")
#printing GBK variable as a single formatted string-file
print(*result1, sep='\n')