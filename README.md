[![DOI](https://zenodo.org/badge/490976583.svg)](https://zenodo.org/badge/latestdoi/490976583)

### CoExp is available on our [webserver](https://pbb-tools.de/CoExp/) ###

# CoExp
CoExp allows the identification of genes that are co-expressed with a set of genes of interest. A list of genes and a count table are provided. A co-expression analysis is performed for each gene in the list. All pairs of genes above a certain cutoff are reported in the result table.

This repository also contains several scripts required to process RNA-seq data sets with kallisto. This leads to the generation of count tables that are suitable for the actual co-expression analysis. There is also a script for the filtering of count tables to exclude suspicious/bad samples.


## CoExp analysis ##

```
Usage
python3 coexp3.py --in <FILE> --exp <FILE> --out <DIR>

Mandatory:
--in       STR   Candidate gene file.
--exp      STR   Count table.
--out      STR   Output folder

Optional:
--ann      STR    Annotation file.
--rcut     STR    Minimal correlation cutoff
--pcut     STR    Maximal p-value cutoff
--expcut   STR    Expression cutoff
--verbose         Activates detailed output
```

`--in` specifies a text file containing the genes of interest. Each line lists one gene ID. These IDs need to match the IDs in the first column of the count table.

`--exp` specifies the count table (text file). This file contains a matrix of the gene expression values. The IDs in the first column need to match the IDs in the genes of interest file.

`--out` specifies the output folder. Temporary and result files will be stored in this folder. This folder will be created if it does not exist already.

`--ann` specifies the annotation file. This file contains a gene ID in the first column and an annotation in the second column. The IDs in this file need to match the IDs of the genes of interest and the IDs in the first column of the count table. If the IDs do not match, it is not possible to assign functional annotations.

`--rcut` specifies the minimal correlation coefficient that serves as a cutoff when reporting co-expressed gene pairs. Default: 0.65.

`--pcut` specifies the maximal p-value that serves as a cutoff when reporting co-expressed gene pairs. Default: 0.05.

`--expcut` specifies the minimal cumulative expression across all samples. Only genes above this cutoff are considered for the co-expression analysis. Default: 5.

`--verbose` does not require any additional input, but will activate printing of additional details during the process.


## RNA-seq data processing ##

### kallisto_pipeline3.py ###
```
Usage
python3 kallisto_pipeline3.py --cds <FILE> --reads <DIR> --out <DIR> --tmp <DIR>

Mandatory:
--cds       STR   CDS reference file
--reads     STR   FASTQ file folder
--out       STR   Output folder
--tmp       STR   Temp folder

Optional:
--kallisto  STR    Full path to kallisto [kallisto]
--cpus      STR    Number of CPUs [10]
```

`--cds` specifies a FASTA file that contains the coding sequences (CDS) that are used as a reference by kallisto.

`--reads` specifies a folder containing many subfolders with FASTQ files. Each subfolder should contain one FASTQ file (single end) or two FASTQ files (paired-end).

`--out` specifies an output folder. This folder will be generated if it does not exist already. All individual count tables will be placed in this folder. This folder needs to be given to the next script to merge all single files into one count table.

`--tmp` specifies a temporary output folder. This folder will be generated if it does not exist already.

`--kallisto` specifies the path to kallisto. This is necessary if kallisto is not in the $PATH. Default: kallisto.

`--cpus` specifies the number of CPUs to be used by kallisto. Default: 10.


### merge_kallisto_output3.py ###
```
Usage
python3 merge_kallisto_output3.py --in <DIR> --gff <FILE> --tpms <FILE> --counts <FILE>
Mandatory:
--in      STR   Input folder
--tpms    STR   Output TPM file
--counts  STR   Output counts file

Optional:
--gff     STR   Input GFF file
```

`--in` specifies the input folder that contains the individual count table files. Each file belongs to one SRA sample.

`--tpms` specifies the final TPM output file. One sample will be represented in one column. All genes/transcripts will be listed in the first column. The date will be stored in the top left field of this table.

`--counts` specifies the final counts output file. One sample will be represented in one column. All genes/transcripts will be listed in the first column. The date will be stored in the top left field of this table.

`--gff` specifies a GFF file to merge expression of different transcripts at the gene level. Give an empty text file to keep expression at the transcript level.


### filter_RNAseq_samples.py ###
```
Usage
python3 filter_RNAseq_samples.py --tpms <FILE> --counts <FILE> --out <DIR>

Mandatory:
--tpms    STR   Input TPM file
--counts  STR   Input counts file
--out     STR   Output folder

Optional:
--min     INT   MIN_EXP [10]
--max     INT   MAX_EXP [80]
```

`--tpms` specifies the input file containing the TPMs.

`--counts` specifies the input file containing the counts.

`--out` specifies the output folder. This folder will be created if it does not exist already.

`--min` specifies the minimal percentage of expression that needs to fall on the top100 transcripts. Default: 10%.

`--max` specifies the maximal percentage of expression that needs to fall on the top100 transcripts. Default: 80%.


## References ##

Pucker B, Iorizzo M (2023) Apiaceae FNS I originated from F3H through tandem gene duplication. PLOS ONE 18(1): e0280155. doi:[10.1371/journal.pone.0280155](https://doi.org/10.1371/journal.pone.0280155).

Pucker, B., Walker-Hale, N., Dzurlic, J., Yim, W.C., Cushman, J.C., Crum, A., Yang, Y. and Brockington, S.F. (2024), Multiple mechanisms explain loss of anthocyanins from betalain-pigmented Caryophyllales, including repeated wholesale loss of a key anthocyanidin synthesis enzyme. New Phytol, 241: 471-489. doi:[10.1111/nph.19341](https://doi.org/10.1111/nph.19341).

