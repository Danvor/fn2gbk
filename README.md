# fn2gbk
A Python3 script tool to convert FASTA with BED regions and GTF annotations to GenBank flat file format.
The script does not require installation.

Usage: 

```fn2gbk [-h] [-f FASTA] [-b BED] [-g GTF] [-n NAME] [-o ORGANISM] [-a AUTHOR] [-t MOLECULE_TYPE] [-r REVERSE_COMPLEMENT]```

Arguments:

  `-h` or `--help`                Show the help message and exit.
  
  `-f` or `--fasta`               Input fasta file with single sequence line after header.
                        
  `-b` or `--bed`                 Bed file of features on fasta file.
  
  `-g` or `--gtf`                Gtf file of features on fasta file.
  
  `-n` or `--name`                Name of stored sequence and region.
  
 `-o` or `--organism`             Name of organism.
 
 `-a` or `--author`               Authors name. Default is "FASTA & BED to GBK script".
 
  `-t` or `--molecule_type`       Type of molecule. Default is "genomic DNA".
  
  `-r` or `--reverse_complement`  Whether to make a reverse complement GBK of the input files. Default is "FALSE".
