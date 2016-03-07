HMP Mock Community samples
==========================

# Data

The HMP metagenomes mock pilot represents the shotgun sequencing of HMP even and staggered Mock communities, distributed to each of the four HMP sequencing centers. The goal of the pilot was to test the sequencing protocol and to evaluate accuracy and consistency between centers.

Two datasets are [available](https://www.ebi.ac.uk/metagenomics/projects/SRP004311) for this project. The first dataset ([SRR072233](https://www.ebi.ac.uk/metagenomics/projects/SRP004311/samples/SRS121011/runs/SRR072233/results/versions/1.0)) is a genomic mixture from 22 bacterial strains containing equimolar riboso-mal RNA operon counts per organism. The second dataset ([SRR072232](https://www.ebi.ac.uk/metagenomics/projects/SRP004311/samples/SRS121012/runs/SRR072232/results/versions/1.0#ui-id-10)) contains also a genomic mixture from the same 22 bacterial strains but the ribosomal RNA operon counts vary by up to four orders of magnitude per organism. The 22 bacterial species in these datasets are 

- *Acinetobacter baumanii*
- *Actinomyces odontolyticus*
- *Bacillus cereus*
- *Bacteroides vulgatus*
- *Candida albicans*
- *Clostridium beijerinckii*
- *Deinococcus radiodurans*
- *Enterococcus faecalis*
- *Escherichia coli*
- *Helicobacter pylori*
- *Lactobacillus gasseri*
- *Listeria monocytogenes*
- *Methanobrevibacter smithii*
- *Neisseria meningitidis*
- *Propionibacterium acnes*
- *Pseudomonas aeruginosa*
- *Rhodobacter sphaeroides*
- *Staphylococcus aureus*
- *Staphylococcus epidermidis*
- *Streptococcus agalactiae*
- *Streptococcus mutans*
- *Streptococcus pneumoniae*

Details about these species, their taxonomy and their expected abundances can be found in [`data/expected_species_w_taxonomy.txt` file](data/expected_species_w_taxonomy.txt).

# Methods

## Get EBI metagenomics results and format them

## Run ASaiM workflow

## Compare EBI metagenomics and ASaiM workflow results

### Taxonomic results

*MetaPhlAn*: relative abundance computed on assigned reads (no count of non assigned reads)

*EBI metagenomics* results: relative abundance on all OTUs

Need to get comparable things



### Functional results

# Results

## Computation stats

time, computer description, cpu %, memory size

## Pretreatments

## Taxonomic analyses

### Assigned reads

EBI metagenomics: 16S sequences
ASaiM: non rRNA sequences

### Details in 

### Comparison with expected abundances

## Functional analyses


