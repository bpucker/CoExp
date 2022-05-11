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

`--ann` specifies the annotation file. This file contains a gene ID in the first column and an annotation in the second column. The IDs in this file need to match the IDs of the genes of interest and the IDs in the first column of the count table. If the IDs do not match, it is not possible to assign functional annotations.

`--rcut` specifies the minimal correlation coefficient that serves as a cutoff when reporting co-expressed gene pairs. Default: 0.65.

`--pcut` specifies the maximal p-value that serves as a cutoff when reporting co-expressed gene pairs. Default: 0.05.

`--expcut` specifies the minimal cumulative expression across all samples. Only genes above this cutoff are considered for the co-expression analysis. Default: 5.


## Reference ##


