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

`--in` specifies .
`--exp` specifies .
`--out` specifies .
`--ann` specifies .
`--rcut` specifies .
`--pcut` specifies .
`--expcut` specifies .
