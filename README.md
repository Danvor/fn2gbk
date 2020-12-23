# fn2gbk
**A Python3 script tool to convert FASTA with BED regions and GTF annotations to GenBank flat file format.
The script does not require installation.**
---

### Usage: 

```python3
fn2gbk [-h] [-f FASTA_FILE] [-b BED_FILE] [-g GTF_FILE] [-n NAME] 
            [-o ORGANISM] [-a AUTHOR] [-t MOLECULE_TYPE] [-r REVERSE_COMPLEMENT]
```

---

### Arguments:

+  `-h` or `--help`
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;Show the help message and exit.
 
+  `-f` or `--fasta`
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; Input fasta file with single sequence line after header.
                        
+  `-b` or `--bed`
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; Bed file of features on fasta file.
  
+  `-g` or `--gtf`
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; Gtf file of features on fasta file.
  
+  `-n` or `--name`
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Name of stored sequence and region.
  
+  `-o` or `--organism`
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Name of organism.
 
+  `-a` or `--author`
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Authors name. Default is "FASTA & BED to GBK script".
 
+  `-t` or `--molecule_type`
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp; Type of molecule. Default is "genomic DNA".
  
+  `-r` or `--reverse_complement`
&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; Whether to make a reverse complement GBK of the input files. Default is "FALSE".
