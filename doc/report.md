---
title: Test of HMP Mock Community samples on ASaiM Galaxy instance
subtitle: Comparison with results from *EBI metagenomics*
date: March 2016
author: Bérénice Batut
geometry: margin=3cm
header-includes:
    - \usepackage{dirtree}
---

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

- Download interesting datasets on EBI metagenomics website
- Format taxonomic results
    - Extract abundances of each clade at different taxonomic levels
    - Compute several abundances measures
        - Relative abundances of clades for all OTUs
        - Relative abundances of clades for OTUs with accurate taxonomic assignation (taxonomic assignation from kingdom to family)
    - Extract percentage of unassigned clades at different taxonomic levels (clades without more accurate taxonomic assignation)     

## Run ASaiM workflow

- Run ASaiM workflow on ASaiM Galaxy instance, with scripts
- Export generated outputs
- Format one outputs to extract percentage of unassigned clades at different taxonomic levels (clades without more accuration taxonomic assignation)

## Compare EBI metagenomics and ASaiM workflow results

### Pretreatments

### Taxonomic results

In *MetaPhlAn*, relative abundance is computed on assigned reads. No count is made of non assigned reads. The comparison of relative abundances between EBI metagenomics and ASaiM results is then made on relative abundances computed on OTUS or reads with an accurate taxonomic assignation (taxonomic assignation from kingdom to family). We compare these results with expected relative abundances obtained from sample descriptions. 

### Functional results

# Results

## Computation statistics on ASaiM

We launch ASaiM Galaxy instance on Debian GNU/Linux System with 8 cores Intel(R) Xeon(R) at 2.40GHz and with 32 Go of RAM.

Statistics | SRR072232 | SRR072233
--- | --- | ---
Execution time | 4h46 | 5h23
Maximum of %CPU used | | 
Maximum RAM size used | | 

## Pretreatments

## Taxonomic analyses

### Assignation rates

*EBI metagenomics* uses 16S sequences with *QIIME*. In ASaiM, we execute *MetaPhlAn* on non rRNA sequences, to search diverse phylogenetic markers and not only 16S ones. But, with this method, we have also higher unassignation rates:

Clade | EBI (SRR072232) | ASaiM (SRR072232) | EBI (SRR072233) | ASaiM (SRR072233)
--- | --- | --- | --- | ---
All | 6.4% | 62.61% | 13% | 
Inside Archea | 40.15% | 3.77% | 29.79% | 
Inside Bacteria | 16% | 96.24% | 50% |

We also have unexpected taxonomic assignations. For ASaiM, several species are identified as "unclassified":

Species | Relative abundance for SRR072232 | Relative abundance for SRR072233
--- | --- | ---
*Escherichia* unclassified | 4.85 | 0.8
*Pseudomonas* unclassified | 1.12 | 0.56
*Methanobrevibacter* unclassified | | 0.24
*Deinococcus* unclassified | 0.16 | 

With *EBI metagenomics*, some taxonomic paths are unexpected:

Taxonomic path | Relative abundance for SRR072232 | Relative abundance for SRR072233
--- | --- | ---
Methanopyraceae (family) | 0.09 | 0.21
Paraprevotellaceae (family) | | 0.09
Rickettsiales (order) | 5.71 | 1.43
Cryptosporangiaceae (family) | | 0.5

### Assignation, relative abundances and comparison with expectations


![Relative abundances of families for SRR072232 \label{db_query}](results/SRR072232/concatenated_results/family_abundances.pdf)

![Relative abundances of families for SRR072233 \label{db_query}](results/SRR072233/concatenated_results/family_abundances.pdf)

## Functional analyses


