# CoExp
This tool allows the identified of genes that are co-expressed with a set of genes of interest. A list of genes and a count table are provided. A co-expression analysis is performed for each gene in the list. All pairs of genes above a certain cutoff are reported in the result table.


## Usage ##

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
```

`--in` specifies a text file containing the genes of interest. Each line lists one gene ID. These IDs need to match the IDs in the first column of the count table.

`--exp` specifies the count table (text file). This file contains a matrix of the gene expression values. The IDs in the first column need to match the IDs in the genes of interest file.

`--out` specifies the output folder. Temporary and result files will be stored in this folder. This folder will be created if it does not exist already.

`--ann` specifies .

`--rcut` specifies .

`--pcut` specifies .

`--expcut` specifies .

