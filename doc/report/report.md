---
title: "Supplementary material: Test of HMP Mock community samples on ASaiM Galaxy instance and comparison with *EBI metagenomics* results"
subject_session: Sequence analysis
subtitle: "ASaiM: a Galaxy-based framework to analyze shotgun sequence data from microbiota"
author: 
    - Bérénice Batut
    - Jean-François Brugère
    - Pierre Peyret
address: EA-4678 CIDAM, Clermont Université, Université d’Auvergne, Clermont-Ferrand, France
geometry: margin=2.5cm
year: 2016
header-includes:
    - \usepackage{dirtree}
    - \usepackage{geometry}
    - \usepackage{pdflscape}
    - \usepackage{array}
    - \usepackage{multirow}
abstract: "The HMP metagenomes mock pilot represents the shotgun sequencing of HMP even and staggered Mock communities, distributed to each of the four HMP sequencing centers. The goal of the pilot was to test the sequencing protocol and to evaluate accuracy and consistency between centers.\\

These controlled datasets are available in [*EBI metagenomics* database](https://www.ebi.ac.uk/metagenomics/projects/SRP004311), with taxonomic and functional analyses obtained with [*EBI metagenomics* pipeline (version 1.0)](https://www.ebi.ac.uk/metagenomics/pipelines/1.0).\\

We analyzed these datasets with the workflow available with ASaiM Galaxy instance and compared taxonomic and functional results with the ones available on [*EBI metagenomics* database](https://www.ebi.ac.uk/metagenomics/projects/SRP004311).\\

Details about these analyses (scripts, parameters, ...) are available on a [dedicated GitHub repository](https://github.com/ASaiM/hmp_mock_tests).
"
---

# Data

Two datasets are [available](https://www.ebi.ac.uk/metagenomics/projects/SRP004311) for this project. The first dataset ([SRR072233](https://www.ebi.ac.uk/metagenomics/projects/SRP004311/samples/SRS121011/runs/SRR072233/results/versions/1.0)) is a genomic mixture from 22 bacterial strains (Table \ref{expected_species}) containing equimolar ribosomal RNA operon counts per organism. The second dataset ([SRR072232](https://www.ebi.ac.uk/metagenomics/projects/SRP004311/samples/SRS121012/runs/SRR072232/results/versions/1.0#ui-id-10)) contains also a genomic mixture from the same 22 bacterial strains (Table \ref{expected_species}) but the ribosomal RNA operon counts vary by up to four orders of magnitude per organism (Table \ref{expected_species})

\newpage
\thispagestyle{empty}
\newgeometry{top=2cm, bottom=3cm, left=3cm, right=2cm}
\begin{landscape}
\begin{table}
\begin{tabular}{llm{2.5cm}llllm{2.5cm}|rr}
\hline
\multicolumn{8}{c|}{Taxonomy} & \multicolumn{2}{c}{Abundances}\\
Domain & Kingdom & Phylum & Class & Order & Family & Genus & Species & SRR072232 & SRR072233 \\
\hline
Archaea & Archaea & Euryarchaeota & Methanobacteria & Methanobacteriales& Methanobacteriaceae & \textit{Methanobrevibacter} & \textit{Methanobrevibacter smithii} & 1,000,000 & 100,000 \\
\hline
Bacteria & Bacteria & Actinobacteria & Actinobacteria & Actinomycetales & Actinomycetaceae & \textit{Actinomyces} & \textit{Actinomyces odontolyticus} & 1,000 & 100,000 \\
\cline{6-10}
 &  &  &  &  & Propionibacteriaceae & \textit{Propionibacterium} & \textit{Propionibacterium acnes} & 10,000 & 100,000 \\
 \cline{3-10}
 & & Bacteroidetes & Bacteroidia & Bacteroidales & Bacteroidaceae & \textit{Bacteroides} & \textit{Bacteroides vulgatus} & 1,000 & 100,000 \\
 \cline{3-10}
& & Deinococcus-Thermus & Deinococci & Deinococcales & Deinococcaceae & \textit{Deinococcus} & \textit{Deinococcus radiodurans} & 1,000 & 100,000 \\
 \cline{3-10}
& & Firmicutes & Bacilli & Bacillales & Bacillaceae & \textit{Bacillus} & \textit{Bacillus cereus thuringiensis} & 100,000 & 100,000\\
 \cline{6-10}
& & & & & Listeriaceae & \textit{Listeria} & \textit{Listeria monocytogenes} & 10,000 & 100,000 \\
\cline{6-10}
& & & & & Staphylococcaceae & \textit{Staphylococcus} & \textit{Staphylococcus aureus} & 100,000 & 100,000 \\
\cline{8-10}
& & & & & & & \textit{Staphylococcus epidermidis} & 1,000,000 & 100,000 \\
\cline{5-10}
& & & & Lactobacillales & Enterococcaceae & \textit{Enterococcus} & \textit{Enterococcus faecalis} & 1,000 & 100,000\\
\cline{6-10}
& & & & & Lactobacillaceae & \textit{Lactobacillus} & \textit{Lactobacillus gasseri} & 10,000 & 100,000\\
\cline{6-10}
& & & & & Streptococcaceae & \textit{Streptococcus} & \textit{Streptococcus agalactiae} & 100,000 & 100,000\\
\cline{8-10}
& & & & & & & \textit{Streptococcus mutans} & 1,000,000 & 100,000\\
\cline{8-10}
& & & & & & & \textit{Streptococcus mitis oralis pneumoniae} & 1,000 & 100,000\\
\cline{4-10}
& & & Clostridia & Clostridiales & Clostridiaceae & \textit{Clostridium} & \textit{Clostridium beijerinckii} & 100,000 & 100,000\\
\cline{3-10}
& & Proteobacteria & Alphaproteobacteria & Rhodobacterales & Rhodobacteraceae & \textit{Rhodobacter} & \textit{Rhodobacter sphaeroides} & 1,000,000 & 100,000\\
\cline{4-10}
& & & Betaproteobacteria & Neisseriales & Neisseriaceae & \textit{Neisseria} & \textit{Neisseria meningitidis} & 10,000 & 100,000\\
\cline{4-10}
& & & Epsilonproteobacteria & Campylobacterales & Helicobacteraceae & \textit{Helicobacter} & \textit{Helicobacter pylori} & 10,000 & 100,000\\
\cline{4-10}
& & & Gammaproteobacteria & Pseudomonadales & Moraxellaceae & \textit{Acinetobacter} & \textit{Acinetobacter baumannii} & 10,000 & 100,000\\
\cline{6-10}
& & & & & Pseudomonadaceae & \textit{Pseudomonas} & \textit{Pseudomonas aeruginosa} & 100,000 & 100,000\\
\cline{5-10}
& & & & Enterobacteriales & Enterobacteriaceae & \textit{Escherichia} & \textit{Escherichia coli} & 1,000,000 & 100,000\\
\hline
Eukaryotes & Fungi & Ascomycota & Saccharomycetes & Saccharomycetales & Debaryomycetaceae & \textit{Candida} & \textit{Candida albicans} & 1,000 & 100,000 \\
\hline
& & & & & & & \textbf{Total} & 5,566,000 & 2,200,000\\
\cline{8-10}
\end{tabular}
\caption{Expected species, their taxonomy and their abundances on both samples (SRR072233 and SRR072233)}
\label{expected_species}
\end{table} 
\end{landscape}
\newpage
\restoregeometry

# Methods

## Analyses from *EBI Metagenomics*

Both datasets were analysed using [*EBI metagenomics* pipeline (Version 1.0)](https://www.ebi.ac.uk/metagenomics/pipelines/1.0) (Figure \ref{ebi_pipeline}).

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/ebi_workflow.pdf}
    \caption{\textit{EBI metagenomics} pipeline (version 1.0).
    The grey boxes correspond to data, the blue boxes to pretreatment steps, the red boxes to functional analysis steps and the green boxes to taxonomic analysis steps.}
    \label{ebi_pipeline}
\end{figure}

Interesting results (OTUs with taxonomic assignation and GO slim annotations) are downloaded and formatted. 

Using OTUs with taxonomic assignation, abundances of each assigned clade are extracted and several relative abundance measures are computed: relative abundances of clades for all OTUs and relative abundances of clades for OTUs with accurate taxonomic assignation (taxonomic assignation from kingdom to family). Percentage of unassigned clades is computed at different taxonomic levels (clades without more accurate taxonomic assignation).

For functional analysis, *EBI metagenomics* offers 3 types of results:

- Matches with InterPro
- Complete GO annotations
- GO slim annotations

As in ASaiM, GO slim annotations are used. They are downloaded and formatted to extract relative abundances (in percentage) of GO slim annotations for the tree annotation classes (cellular components, biological processes and molecular functions).

## Analyses with ASaiM workflow

Both datasets are analyzed using ASaiM workflow dedicated to single-end microbiota data (Figure \ref{asaim_workflow}).

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/asaim_workflow.pdf}
    \caption{ASaiM workflow available with ASaiM Galaxy instance and used to analyze both datasets.
    The grey boxes correspond to data, the blue boxes to pretreatment steps, the red boxes to functional analysis steps and the green boxes to taxonomic analysis steps.}
    \label{asaim_workflow}
\end{figure}

This workflow is available with ASaiM Galaxy instance. For this analysis, ASaiM Galaxy instance are deployed on a Debian GNU/Linux System with 8 cores Intel(R) Xeon(R) at 2.40GHz and with 32 Go of RAM. Several statistics are followed during workflow execution (Table \ref{computation_stats}).

\begin{table}[h!]
\centering
\begin{tabular}{llrr}
\hline
\multicolumn{2}{l}{Statistics} & SRR072232 & SRR072233 \\
\hline
Execution time & All & 4h44 & 5h22 \\
& PRINSEQ & 0h38 & 0h44\\
& Vsearch & 16s & 19s\\
& SortMeRNA & 0h55 & 0h58\\
& MetaPhlAN2 & 0h09 & 0h10\\
& HUMAnN2 & 3h01 & 3h26\\
\%CPU used & Min & 4.8\% & 4.8\%\\
 & Mean & 4.8\% & 4.8\%\\
 & Max & 4.8\% & 4.8\%\\
Size of the process in memory (kb) & Min & 1,515,732 & 1,515,732\\
 & Mean & 1,515,744 & 1,515,743\\
 & Max & 1,515,768 & 1,515,764\\
\hline
\end{tabular}
\caption{Computation statistics on ASaiM for both samples (SRR072233 and SRR072233)}
\label{computation_stats}
\end{table}

Once ASaiM Galaxy instance is deployed, a task that can take several hours, datasets analyses are relatively fast: < 5h and < 5h30 for datasets with 1,225,169 and 1,386,198 sequences respectively (Table \ref{computation_stats}). The main time consuming step is the functional assignation with *HUMAnN2* [@abubucker_metabolic_2012] which last $\simeq$ 64% of overall time execution (Table \ref{computation_stats}). The percentage of used CPU is stable over workflow execution, just like the size of the process in memory (variability inferior to 40 kb) (Table \ref{computation_stats}).

In addition to formatting steps in workflow, taxonomic results are formatted to extract the percentage of unassigned clades at different taxonomic levels (clades without more accurate taxonomic assignation). 

No further formatting step is needed for functional results (relative abundance of gene families, pathways and GO slim terms) of one sample. A workflow is developed and executed to compare raw *HUMAnN2* results (gene families and pathways) between both samples (SRR072232 and SRR072233) (Figure \ref{asaim_humann2_comparison_results}).

\begin{figure}[h!]
    \centering
    \includegraphics[width = .8\linewidth]{../images/asaim_humann2_comparison_results.pdf}
    \caption{Workflow to compare normalized \textit{HUMANnN2} outputs (abundances of gene families and pathways). This workflow is available with ASaiM Galaxy instance. The grey boxes correspond to data, the blue boxes to processing steps.}
    \label{asaim_humann2_comparison_results}
\end{figure}

## Comparison of results from *EBI metagenomics* and ASaiM

Results from *EBI metagenomics* results and the ones from ASaiM are not directly comparable. Several processing steps are then needed.

With *MetaPhlAn* in ASaiM workflow, relative abundance of clades is computed on assigned reads. No count is made of non assigned reads. To compare relative abundances between *EBI metagenomics* and *ASaiM*, we focus on relative abundances computed on OTUS or reads with an accurate taxonomic assignation (taxonomic assignation from kingdom to family). These results are also compared to expected relative abundances obtained from sample descriptions (Table \ref{expected_species}). 

In both *EBI metagenomics* and ASaiM workflows, functional matches are grouped into GO slims terms. These terms are a subset of the terms in the whole Gene Ontology. They give a broad overview of the ontology content. To compare *EBI metagenomics* and ASaiM results, relative abundance of GO slim terms for both samples and both workflows are concatenated and compared, given the workflow depicted in Figure \ref{go_slim_comparison_workflow}. 

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/go_slim_comparison_workflow.pdf}
    \caption{Workflow to compare GO slim annotation abundances between samples (SRR072232, SRR072233) and workflows (\textit{EBI metagenomics}, ASaiM). This workflow is available with ASaiM Galaxy instance. The grey boxes correspond to data, the blue boxes to processing steps.}
    \label{go_slim_comparison_workflow}
\end{figure}

# Results

## Pretreatments

In both workflows (Figures \ref{ebi_pipeline} and \ref{asaim_workflow}), raw sequences are pre-processed before any taxonomic or functional analyses. These preprocessing steps include quality control to remove low quality, small or duplicated sequences and also rRNA sorting to differentiate rRNA sequences from non rRNA sequences (Figures \ref{ebi_pipeline} and \ref{asaim_workflow}). The used tools and parameters for these pretreatments are different between *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}) and ASaiM workflow (Figure \ref{asaim_workflow}). Even with similar raw sequences, pretreatment outputs are different (Table \ref{pretreatment_stats}).

\begin{table}[h!]
\centering
\begin{tabular}{m{4cm}rrrrrrrr}
\hline
 & \multicolumn{4}{c}{SRR072232} & \multicolumn{4}{c}{SRR072233} \\
Sequences & \multicolumn{2}{c}{EBI} & \multicolumn{2}{c}{ASaiM} & \multicolumn{2}{c}{EBI} & \multicolumn{2}{c}{ASaiM} \\
\hline
Raw sequences & \multicolumn{4}{c}{1,225,169} & \multicolumn{4}{c}{1,386,198}\\
Sequences after quality control and dereplication & 997,622 & 81.4\% & 1,175,853 & 96\% & 1,197,748 & 86.4\% & 1,343,451 & 96.9\% \\
rRNA sequences & 8,910 & 0.9\% & 16,016 & 1.4\% & 9,214 & 0.8\% & 13,850 & 1\%\\
non rRNA sequences & 988,712 & 99.1\% & 1,159,837 & 98.6\% & 1,188,534 & 99.2\% & 1,329,601 & 99\%\\
\hline
\end{tabular}
\caption{Statistics of pretreatments for EBI and ASaiM on both samples (SRR072233 and SRR072233)}
\label{pretreatment_stats}
\end{table}

The first interesting point in pretreatments is the difference in sequence number after quality control and dereplication (Table \ref{pretreatment_stats}). With ASaiM, more sequences are conserved during these first steps of quality control and dereplication (> 96\% against < 87\% with *EBI metagenomics*, Table \ref{pretreatment_stats}). This difference may be explained by the difference in thresholds for min length. In *EBI metagenomics* pipeline, sequences with less than 100 nucleotides are removed (Figure \ref{ebi_pipeline}), while in ASaiM the threshold is fixed to 60 nucleotides (Figure \ref{asaim_workflow}). However, this threshold difference can not explained all the observed difference in sequence number after quality control and dereplication. Indeed, when in ASaiM workflow PRINSEQ is run with exactly same parameters but filtering of sequences with less than 100 nucleotides, 1,135,008 (92.6%) and 1,304,023 (94.1%) sequences are conserved for SRR072232 and SRR072233 respectively after quality control and dereplication. These proportion are still higher than the one observed with *EBI metagenomics* pipeline (Table \ref{pretreatment_stats}). Smaller length threshold with ASaiM can not then explain all difference in sequence number after quality control and dereplication.

In both datasets and with both workflows, few rRNA sequences are found in datasets (Table \ref{pretreatment_stats}). Indeed, these datasets are metagenomic datasets and then focus on gene sequences. Few copies of rRNA genes are found in organisms (bacteria, archeae or eukaryotes) and then expected in metagenomic sequences. Despite small number of sequences, a difference is observed between *EBI metagonomics* and ASaiM workflows for the number of rRNA sequences (Table \ref{pretreatment_stats}). Higher proportions of rRNA sequences are systematically found with ASaiM workflow. Indeed, in *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}), *rRNASelector* [@lee_rrnaselector:_2011] is used to select rRNA  bacterial and archaeal sequences. In ASaiM workflow (Figure \ref{asaim_workflow}), rRNA sequences are searched using *SortMeRNA* [@kopylova_sortmerna:_2012] and 8 databases for bacteria, archaea and eukaryotes rRNA. % of sequences are matched against databases dedicated to eukaryotes rRNA sequences, but it does not explain the differences between *EBI metagenomics* and ASaiM. This difference may be due to the completness of the databases: databases used by *rRNASelector* [@lee_rrnaselector:_2011] are older and may be less filled than databases used by *SortMeRNA* [@kopylova_sortmerna:_2012].

## Taxonomic analyses

### Raw ASaiM results

In ASaiM workflow (Figure \ref{asaim_workflow}), taxonomic analysis is made using *MetaPhlAN* (2.0) [@truong_metaphlan2_2015;@segata_metagenomic_2012] on sequences after pretreatments. *MetaPhlAn* profiles the composition of microbial communities using a database of unique clade-specific marker genes identified from 17,000 reference genomes. This step of taxonomic assignation with *MetaPhlAn* is fast in ASaiM Galaxy instance (less than 10 minutes for > 1,100,000 sequences, Tables \ref{computation_stats} and \ref{pretreatment_stats}). 

Raw *MetaPhlAn* results consist in a plain text file with relative abundance of clades at different taxonomic levels. Visualisation tools help to represent *MetaPhlAn* results. In ASaiM, two such tools are used: *Krona* [@ondov_interactive_2011] for an interactive representation of taxonomic assignation ([SRR072232]() and [SRR072233]()) and *GraPhlan* for a static representation (Figures \ref{graphlan_SRR072232} and \ref{graphlan_SRR072233}). 

\begin{figure}[h!]
    \centering
    \includegraphics[width = .8\linewidth]{../images/SRR072232/graphlan.png}
    \caption{GraPhlAn representation of taxonomic assignation obtained for SRR072232 with ASaiM}
    \label{graphlan_SRR072232}
\end{figure}

\begin{figure}[h!]
    \centering
    \includegraphics[width = .8\linewidth]{../images/SRR072233/graphlan.png}
    \caption{GraPhlAn representation of taxonomic assignation obtained for SRR072233 with ASaiM}
    \label{graphlan_SRR072233}
\end{figure}

Despite same expected taxonomy, the taxonomic diversity in SRR072232 dataset (Figure \ref{graphlan_SRR072232}) is reduced compared to the one in SRR072233 dataset (Figure \ref{graphlan_SRR072233}). Less taxons are found for each taxonomic levels. 

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/species_abundances.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072233/species_abundances.pdf}
    \end{minipage} 
    \caption{Relative abundances (percentage in log scale) of expected species for SRR072232 (left) and SRR072232 (right) with comparison between expected abundances (red thin bars) and abundances obtained with ASaiM (blue wide bars)}
    \label{species_abundances}
\end{figure}

From the 22 expected species (Table \ref{expected_species}), 17 are found for SRR072232 and 20 for SRR072233 (Figure \ref{species_abundances}). The 2 expected species (*Candidata albicans*  and *Lactobacillus gasseri*) which are not found in SRR072233 dataset are also not found SRR072232 dataset (Figure \ref{species_abundances}). This may be due to a lack of phylogenetic markers for these species in the database used in *MetaPhlAn*. 

Except some species, the observed relative abundances of species for SRR072232 follows the expected ones (Figure \ref{species_abundances}): smaller for small expected abundances and higher for high expected abundances. For SRR072233, same abundance is expected for all species, but more variability is observed (Figure \ref{species_abundances}). 

One species is interesting: *Deinococcus radiodurans*. In both samples, this species is found at abundances $\simeq$ 9 times higher than expected (Figure \ref{species_abundances}). This over-abundance in both samples may be explained by over-abundance in reference database and also by the high resistance of this bacteria.

### Comparison with EBI results and expected taxonomy

After these first comparison between ASaiM results taxonomic and expected ones, we compare ASaiM taxonomic results and *EBI metagenomics* taxonomic results.

In *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}), *QIIME* [@caporaso_qiime_2010] is used on 16S sequences to identify OTUs and taxonomic assignation for these OTUs. In ASaiM (Figure \ref{asaim_workflow}), *MetaPhlAn* [@truong_metaphlan2_2015;@segata_metagenomic_2012] is computed on sequences after quality control and dereplication, without any sorting step. *MetaPhlAn* [@truong_metaphlan2_2015;@segata_metagenomic_2012] searches diverse phylogenetic markers, and not only 16S ones as *QIIME* [@caporaso_qiime_2010] does, on all type of sequences (rRNA, non rRNA, ...). With so wide type sequences, the interesting information is less clear. Indeed, with *MetaPhlAn* [@truong_metaphlan2_2015;@segata_metagenomic_2012], the rate of non assignation is $\simeq$ 9 times higher than with *QIIME* [@caporaso_qiime_2010] (SRR072232: 6.4\% with *EBI metagenomics* against 62.61\% with ASaiM; SRR072233: 13\% with *EBI metagenomics* against 53.93\% with ASaiM). However, with *MetaPhlAn* [@truong_metaphlan2_2015;@segata_metagenomic_2012], the taxonomic assignations are more accurate, precise (until species level) and statistically supported (based on more sequences) and do not focus only on bacteria or archea.

With both *EBI metagenomics* and ASaiM, some observed taxonomic assignations are unexpected (Tables \ref{asaim_unexpected_species} and \ref{ebi_unexpected_clades}). For ASaiM, 3 species in each sample are identified as "unclassified" (Table \ref{asaim_unexpected_species}). They are affiliated to the correct genus but not to the species. These unclassified sequences may be due to incomplete annotations in reference database, because expected species are known and observed. However, these expected species are observed in lower abundance (Figure \ref{species_abundances}) and could be closer to expected abundances with correct annotation of unclassified species.

\begin{table}[h!]
\centering
\begin{tabular}{lrr}
\hline
Species & SRR072232 & SRR072233\\
\hline
\textit{Escherichia} unclassified & 4.85\% & 0.8\% \\
\textit{Pseudomonas} unclassified & 1.12\% & 0.56\% \\
\textit{Methanobrevibacter} unclassified & - & 0.24\% \\
\textit{Deinococcus} unclassified & 0.16\% & - \\ 
\hline
\end{tabular}
\caption{Relative abundances of unclassified species in ASaiM taxonomic results for both samples (SRR072233 and SRR072233)}
\label{asaim_unexpected_species}
\end{table}

Similarly, some observed clades and their sub-clades are unexpected in *EBI metagenomics* taxonomic results (Table \ref{ebi_unexpected_clades}). The taxonomic levels of these unexpected clades are higher (class, order and family) than unexpected taxonomic level in ASaiM (species, Table \ref{unexpected_clades}). Taxonomic assignations with *MetaPhlAN* [@truong_metaphlan2_2015;@segata_metagenomic_2012] are then more accurate and precise.

\begin{table}[h!]
\centering
\begin{tabular}{llrr}
\hline
Clade & Taxonomic level & SRR072232 & SRR072233\\
\hline
Methanopyri & Class & 0.09\% & 0.21\% \\
Rickettsiales & Order & 5.71\% & 1.43\% \\
Methanopyrales & Order & 0.09\% & 0.21\% \\
Rickettsiales mitochondria & Family & 5.71\% & 1.43\% \\
Methanopyraceae & Family & 0.09\% & 0.21\% \\
Paraprevotellaceae & Family & - & 0.09\% \\
Cryptosporangiaceae & Family & - & 0.5\% \\
\hline
\end{tabular}
\caption{Relative abundances of unexpected clades and their sub-clades in \textit{EBI metagenomics} taxonomic results for both samples (SRR072233 and SRR072233)}
\label{ebi_unexpected_clades}
\end{table}

\begin{table}[h!]
\centering
\begin{tabular}{lrrrr}
\hline
 & \multicolumn{2}{c}{SRR072232} & \multicolumn{2}{c}{SRR072233}\\
Taxonomic level & EBI & ASaiM & EBI & ASaiM \\
\hline
Domain & - & - & - & - \\
Kingdom & - & - & - & -\\
Phylum & - & - & - & -\\
Class & 0.09\% & - & 0.21\% & -\\
Order & 5.71\% & - & 1.64\% & - \\
Family & 5.71\% & - & 2.23\% & - \\
Genus & \textit{No information} & - & \textit{No information} & - \\
Species & \textit{No information} & 6.13\% & \textit{No information} & 1.6\%\\
\hline
\end{tabular}
\caption{Relative abundances of unexpected clades at different taxonomic levels in taxonomic results of \textit{EBI metagenomics} and ASaiM for both samples (SRR072233 and SRR072233)}
\label{unexpected_clades}
\end{table}

Interestingly, for both workflows (*EBI metagenomics* and ASaiM), the proportion of unexpected clades is higher for SRR072232 than for SRR072233 (Table \ref{unexpected_clades}). We do not have a good explanation for this phenomenon.

Taxonomic results obtained with *EBI metagenomics* pipeline are less precise than the one obtained with ASaiM workflow. Indeed, the most precise taxonomic level is family for *EBI metagenomics* and species for ASaiM. Then, to compare taxonomic results, we focus on family level (Figure \ref{family_abundances}).

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/concatenated_family_abundances.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072233/concatenated_family_abundances.pdf}
    \end{minipage} 
    \caption{Relative abundances of expected families for SRR072232 (left) and SRR072232 (right) with comparison between expected abundances (red thin bars), abundances obtained with \textit{EBI metagenomics} (green wide bars) and abundances obtained with ASaiM (blue wide bars) and }
    \label{family_abundances}
\end{figure}

Except two families (Listeriacecae and Bacillaceae), all families found with *EBI metagenomics* are found with ASaiM (Figure \ref{family_abundances}). Families not found with both methods can be explained by two reasons. 

The first reason relies on incompletness of reference databases used to assign taxonomy in workflow. Indeed, if sequences of some families do no match with any sequence in references databases, the corresponding families and the corresponding taxonomy will not be found. It can be the case of Listeriaceae: this family is found with correct abundance with *EBI metagenomics* pipeline, but with ASaiM, this family is not found for SRR072232 and found in under-abundance for SRR072233 (Figure \ref{family_abundances}). Then, sequences corresponding to this family match some sequences in *MetaPhlAn* reference database, but this database is incomplete to match all expected sequences and correctly estimate abundance. 

However, this incompletness of reference databases can not explain families not found with both *EBI metagenomics* and ASaiM (different tools and reference databases). An other explanation for these not found families can be proposed: too few sequences corresponding to the expected families in datasets despite the expected abundance. This phenomenon may be due to experimental or sequencing errors. Sequences corresponding to expected families are then underrepresented in overall sequences and can not be spotted in taxonomic analyses. Bacillaceae family seems a good example for this explanation. This family is not found neither by *EBI metagenomics* taxonomic analyses for both samples nor by ASaiM taxonomic analyses for SRR072232 (Figure \ref{family_abundances}), but it is found in low abundance by ASaiM taxonomic analyses for SRR072233 (abundance 29 times smaller than expected). The taxonomic signal of this family is really low, too low to be detected by *EBI metagnomics*. This under abundance of sequences corresponding to some families is a good explanation for families not found by the two methods, particularly when the expected abundance for these families is low (\textit{e.g} Debaryomycetaceae, Actinomycetaceae, Bacteroidaceae, Enterococcaceae, Figure \ref{family_abundances}).

In these families with expected low abundance, one family is an exception: Deinococcaceae (Figure \ref{family_abundances}). In SRR072232 sample, unlike other families with low expected abundance, this family is found and with an abundance > 10 times higher than expected. In SRR072233 sample, the observed abundance is > 7 times higher than expected with both methods (Figure \ref{family_abundances}). In this family, one species is expected: \textit{Deinococcus radiodurans}. An over-abundance of this species has already been observed in ASaiM taxonomic results (Figure \ref{species_abundances}). 

## Functional analyses

### Raw ASaiM results

In ASaiM workflow (Figure \ref{asaim_workflow}), functional analyses is made using [*HUMAnN*2](http://huttenhower.sph.harvard.edu/humann2) [@abubucker_metabolic_2012]. This tool profiles the presence/absence and abundance of UniRef50 gene families and MetaCyc pathways using *MinPath* from metagenomic/metatranscriptomic datasets. It is helpful to describe the metabolic profil of a microbiol community. This step of functional profiling with *HUMAnN*2 is the longest step in ASaiM workflow (Table \ref{computation_stats}). 

*HUMAnN*2 generates three outputs: UniRef50 gene families, coverage and abundance of MetaCyc pathways. In both samples, > 90,000 UniRef50 gene families and > 480 MetaCyc pathways (Table \ref{humann2_informations}) are reconstructed from > 1,100,000 non rRNA sequences (Table \ref{pretreatment_stats}). More gene families and pathways are found for SRR072233 than for SRR072232 (Table \ref{humann2_informations}) but the values are similar. 

\begin{table}[h!]
\centering
\begin{tabular}{m{3cm}m{5cm}rrrr}
\hline
 & & \multicolumn{2}{c}{UniRef50 gene families} & \multicolumn{2}{c}{MetaCyc pathways}\\
 & & SRR072232 & SRR072233 & SRR072232 & SRR072233 \\
\hline
All & Number & 98,569 & 129,691 & 487 & 500\\
 & Similar & \multicolumn{2}{c}{44,933} & \multicolumn{2}{c}{475} \\
& \% of similar inside all & 45.59\% & 34.65\% & 97.54\% & 95\% \\
& Relative abundance (\%) & 89.16\% & 50.67\% & 99.85\% & 99.53\%\\
& \textit{p-value} of Wilcoxon test on normalized relative abundance & \multicolumn{2}{c}{1.31 $\cdot 10^{-14}$ (***)} & \multicolumn{2}{c}{0.24} \\
\hline
Associated to a species & Number & 26,219 & 41,005 & 402 & 400 \\
& \% of associated to a species inside all & 26.60\% & 31.62\% & 82.56\% & 80\% \\
& Relative abundance (\%) & 93.40\% & 90.24\% & 61.08\% & 51.52\%\\
& Similar & \multicolumn{2}{c}{19,815} & \multicolumn{2}{c}{363} \\
& \% of similar inside associated to a species  & 68.02\% & 48.32\% & 90.30\% & 90.75\% \\
& Relative abundance of similar inside associated to a species (\%) & 89.17\% & 44.75\% & 91.87\% & 42.70\%\\
\hline
\end{tabular}
\caption{Global information about UniRef50 gene families and MetaCyc pathways obtained with \textit{HUMAnN2} for both samples (SRR072233 and SRR072233). For each characteristics (gene families and pathways), several information is extracted: all number, number percentage and relative abundance (\%) of similar characteristics and \textit{p-value} of Wilcoxon test on relative abundance normalized by the sum of relative abundance for all similar characteristics.}
\label{humann2_informations}
\end{table}

44,933 gene families are found in both samples (Table \ref{humann2_informations}). Even if less than 50\% of gene families are similar, the similar gene families represent more than 50\% of the relative abundance in both samples (Table \ref{humann2_informations}). Inside similar gene families, relative abundance of gene families in both samples is different (Figure \ref{similar_characteristics_abundances}): the median value of normalized abundance of similar gene families is smaller for SRR072232 (significant *p-value* for Wilcoxon test, Table \ref{humann2_informations}).

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_samples/gene_families_SRR072232_SRR072233.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_samples/pathways_SRR072232_SRR072233.pdf}
    \end{minipage} 
    \caption{Normalized relative abundances (\%) for similar UniRef50 gene families (left graphics) and MetaCyc pathways (right graphics) for both samples (SRR072233 and SRR072233). The relative abundances of each similar characteristics (gene families or pathways) is computed with \textit{HUMAnN2} and normalized by the sum of relative abundance for all similar characteristics.}
    \label{similar_characteristics_abundances}
\end{figure}

Similarly, a high proportion (> 95 \%) of pathways are found in both samples (Table \ref{humann2_informations}) and they represents nearly all abundance (> 99.5 \%, Table \ref{humann2_informations}). Unlike gene families, relative abundance of pathways are similar in both samples (non-significant *p-value* for Wilcoxon test, Table \ref{humann2_informations} and Figure \ref{similar_characteristics_abundances}).

In *HUMAnN2* results, abundances of gene families and pathways are stratified at the community level. Contribution of identified species for < 35\% of gene families and > 80\% pathways are then accessible and they represent > 90\% of relative abundance for gene families and > 50\% for pathways (Table \ref{humann2_informations}). This taxonomic information (relation between species and gene families or pathways) can be related to taxonomic information and species abundances from *MetaPhlAN2* (Figure \ref{gene_family_pathway_mean}). 

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/mean_gene_family_abundance.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/mean_pathway_abundance.pdf}
    \end{minipage}
    \caption{Mean abundances of gene families (left) and pathways (right) in fonction of related species abundance for SRR072232 (log scale). Correlation coefficients and p-values are detailed in Table \ref{correlation_information}}
    \label{gene_family_pathway_mean}
\end{figure}

For both samples, relative abundances of gene families and pathways are highly correlated to observed relative abundance of corresponding species (Figure \ref{gene_family_pathway_mean} and Table \ref{correlation_information}). This relation is expected for gene families: a species is more abundant if more sequences corresponding to this species are found and then the relative abundance of these sequences is high. It applies to all sequences, even sequences corresponding to gene families. For pathways, the relation is more complex: a pathway is identified if a high proportion of the gene families expected for this pathway is found. And the abundance of a pathway is proportional to the number of complete "copies" of this pathway in the species.
Then, a pathway is abundant if its parts are all found in numerous copies. The high correlations between species relative abundance and mean relative pathway abundance (Figure \ref{gene_family_pathway_mean}, Table \ref{correlation_information}) confirm the correct pathway reconstruction with *HUMAnN2*.

\begin{table}[h!]
\centering
\begin{tabular}{llrrrr}
\hline
 & & \multicolumn{2}{c}{UniRef50 gene families} & \multicolumn{2}{c}{MetaCyc pathways}\\
 & & SRR072232 & SRR072233 & SRR072232 & SRR072233 \\
\hline
\multicolumn{2}{c}{Mean abundance (Figure \ref{gene_family_pathway_mean})} & & & &\\
\cline{1-2}
Correlation with species abundance & $r^{2}$ & 0.91 & 0.98 & 0.90 & 0.93\\
 & \textit{p-value} & 1.51 $\cdot 10^{-7}$ & $<$ 2.2 $\cdot 10^{-16}$ & 1.91 $\cdot 10^{-7}$ & 5.88 $\cdot 10{-12}$ \\
\hline
\multicolumn{2}{c}{Difference of mean abundance between SRR072233 and SRR072232} & & & &\\
\multicolumn{2}{c}{(Figure \ref{diff_gene_family_pathway_mean})} & & & &\\
\cline{1-2}
Correlation with difference of species abundance & $r^{2}$ & \multicolumn{2}{c}{0.89} & \multicolumn{2}{c}{0.84}\\
 & \textit{p-value} & \multicolumn{2}{c}{4.121 $\cdot 10^{-7}$} & \multicolumn{2}{c}{4.651 $\cdot 10^{-6}$} \\
\hline
\multicolumn{2}{c}{Number (Figure \ref{gene_family_nb_protein_nb})} & & & &\\
\cline{1-2}
Correlation with species abundance & $r^{2}$ & 0.1 & 0.04 & & \\
  & \textit{p-value} & 0.27 & 0.39 & & \\
\cline{1-2}
Correlation with species median protein number & $r^{2}$ & 0.56 & 0.37 & & \\
& \textit{p-value} & 2.027 $\cdot 10^{-3}$ & 4.28 $\cdot 10^{-3}$ & & \\
\hline
\multicolumn{2}{c}{Difference of number between SRR072233 and SRR072232} & & & &\\
\cline{1-2}
Correlation with difference of species abundance & $r^{2}$ & \multicolumn{2}{c}{0.42} & \multicolumn{2}{c}{0.29}\\
& \textit{p-value} & \multicolumn{2}{c}{0.013} & \multicolumn{2}{c}{0.046} \\
\hline
\end{tabular}
\caption{Correlation coefficients and p-values (Pearson's test) for UniRef50 gene families and MetaCyc pathways obtained with \textit{HUMAnN2} for both samples (SRR072233 and SRR072233).}
\label{correlation_information}
\end{table}

Similar relations between species abundances and gene family or pathway mean abundances are found in both samples (Table \ref{correlation_information}). Indeed, differences in gene families and pathways abundances between both samples are mostly explained by differences in abundance of corresponding species (high correlation, Figure \ref{diff_gene_family_pathway_mean}, Table \ref{correlation_information}).

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_samples/mean_gene_family_abundance.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_samples/mean_pathway_abundance.pdf}
    \end{minipage}
    \caption{Difference in mean abundances for gene families (left) and pathways (right) in fonction of difference of related species abundance between SRR072233 and SRR072232. Correlation coefficients and p-values are detailed in Table \ref{correlation_information}}
    \label{diff_gene_family_pathway_mean}
\end{figure}

Unlike mean abundance, number of different gene families for each species is not correlated to species abundances (Figure \ref{gene_family_nb_protein_nb}, Table \ref{correlation_information}). Then, a highly abundant species is abundant because of numerous copies of its gene families but not necessarily because of numerous different gene families. The number of different gene families for each species is more correlated with the median number of protein for these species (Figure \ref{gene_family_nb_protein_nb}, Table \ref{correlation_information}). We expect also a correlation with the number of gene families corresponding to these species in reference database (UniRef50) of *HUMAnN2*.

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/gene_family_nb.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/gene_family_nb_protein_nb.pdf}
    \end{minipage} 
    \caption{Number of gene families in fonction of corresponding species abundance (left) and median protein number for species (right) for SRR072232. Correlation coefficients and p-values are detailed in Table \ref{correlation_information}. The median protein number for each species has been extracted from NCBI. }
    \label{gene_family_nb_protein_nb}
\end{figure}

In both samples, less abundant a species is, higher is the difference between number of observed gene families for this species and expected median protein number (Figure \ref{gene_family_nb_protein_nb}). Indeed, less abundant species have fewer sequences than more abundant species in overall dataset of sequences. And, the signal to identify these sequences and corresponding gene families is low and noisy. Lower proportion of expected gene families are then identified for less abundant species.

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/diff_prot_nb_gene_family_number.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072233/diff_prot_nb_gene_family_number.pdf}
    \end{minipage} 
    \caption{Difference between observed number of different gene families and expected median protein number in function of relative abundance of corresponding species (log scale) for SRR072232 (left) and SRR072233 (right). The median protein number for each species has been extracted from NCBI. }
    \label{gene_family_nb_protein_nb}
\end{figure}

With more than 40,000 gene families and almost 500 pathways, it is difficult to get a broad overview of metabolic profil of the studied microbial community. Each gene family and pathway is precise and related to specific metabolic functions. This information is interesting when you need detailed metabolic information and to go deeply inside metabolic profil. However, to get a general overview of the metabolic processes, UniRef50 gene families and even MetaCyc pathways are too numerous and too precise. UniRef50 gene families and their abundances can be grouped into slim Gene Ontology terms (Figure \ref{SRR072232_go_abundances}). These results are commented in relation with *EBI metagenomics* results in next section.

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/cellular_components.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/biological_processes.pdf}
    \end{minipage} 
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/molecular_functions.pdf}
    \end{minipage}
    \caption{Relative abundances of GO slim terms in SRR072232 for cellular components (top left), biological processes (top right) and molecular function (bottom)}
    \label{SRR072232_go_abundances}
\end{figure}

### Comparison of *EBI metagenomics* and ASaiM results

In *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}), functional analyses are based on InterPro and its identifiants. In ASaiM workflow (Figure \ref{asaim_workflow}), we have access to UniRef50 gene families and their abundances computed with *HUMAnN2*. These functional results are then not directly comparable. But, in both workflows, UniRef50 gene families and InterPro proteins are grouped in slim Gene Ontology terms to get a broad overview of the functional profile of the community. The GO slim terms are grouped inside 3 groups: cellular processes, biological processes and molecular functions.

Few GO slim terms are not similar for *EBI metagenomics* and ASaiM (Table \ref{incomplete_go_slims}). They represent low relative abundance inside the three groups (< 20\%).

\begin{table}[h!]
\centering
\begin{tabular}{llrrrr}
\hline
 & & \multicolumn{2}{c}{SRR072232} & \multicolumn{2}{c}{SRR072233}\\
GO id & GO name & EBI & ASaiM & EBI & ASaiM \\
\hline
\multicolumn{2}{l}{Cellular components} & & & & \\
\href{http://amigo.geneontology.org/amigo/term/GO:0031012}{GO:0031012} & Extracellular matrix & 1.71 $\cdot 10^{-2}$ & - & 2.74 $\cdot 10^{-2}$ & 1.37 $\cdot 10^{-5}$ \\
\href{http://amigo.geneontology.org/amigo/term/GO:0005667}{GO:0005667} & Transcription factor complex & 0 & - & 9.81 $\cdot 10^{-3}$ & -\\
\href{http://amigo.geneontology.org/amigo/term/GO:0005694}{GO:0005694} & Chromosome & 2.80 & - & 2.61 & -\\
\href{http://amigo.geneontology.org/amigo/term/GO:0005856}{GO:0005856} & Cytoskeleton & 2.23 $\cdot 10^{-1}$ & - & 8.44 $\cdot 10^{-2}$ & -\\
\href{http://amigo.geneontology.org/amigo/term/GO:0016469}{GO:0016469} & Proton-transporting two-sector ATPase complex & 1.34 & - & 1.44 & -\\
\href{http://amigo.geneontology.org/amigo/term/GO:0019861}{GO:0019861} & Flagellum & 9.78 $\cdot 10^{-1}$ & - & 6.24 $\cdot 10^{-1}$ & -\\
\href{http://amigo.geneontology.org/amigo/term/GO:0005575}{GO:0005575} & Unknown cellular component & - & 19.29 & - & 19.84 \\
\hline
\multicolumn{2}{l}{Biological processes} & & & & \\
\href{http://amigo.geneontology.org/amigo/term/GO:0006351}{GO:0006351} & Transcription, DNA-dependent & 3.27 & - & 3.06 & - \\
\href{http://amigo.geneontology.org/amigo/term/GO:0044403}{GO:0044403} & Symbiosis, encompassing mutualism through parasitism & 1.91 $ \cdot 10^{-2}$ & - & 4.35 $\cdot 10^{-3}$ & - \\
\href{http://amigo.geneontology.org/amigo/term/GO:0046039}{GO:0046039} & GTP metabolic process & 5.59 $\cdot 10^{-2}$ & - & 5.29 $\cdot 10^{-2}$ & - \\
\href{http://amigo.geneontology.org/amigo/term/GO:0008150}{GO:0008150} & Unknown biological process & - & 6.84 & - & 5.29 \\
\hline
\multicolumn{2}{l}{Molecular functions} & & & & \\
\href{http://amigo.geneontology.org/amigo/term/GO:0001071}{GO:0001071} & Nucleic acid binding transcription factor activity & 1.56 & - & 1.33 & - \\
\href{http://amigo.geneontology.org/amigo/term/GO:0003774}{GO:0003774} & Motor activity & 9.87 $\cdot 10^{-2}$ & - & 5.32 $\cdot 10^{-2}$ & - \\
\href{http://amigo.geneontology.org/amigo/term/GO:0045182}{GO:0045182} & Translation regulator activity & 1.38 $\cdot 10^{-3}$ & - & 0 & - \\
\href{http://amigo.geneontology.org/amigo/term/GO:0003674}{GO:0003674} & Unknown molecular function & - & 9.34 & - & 10.88 \\
\hline
\end{tabular}
\caption{GO slim terms not found in both samples (SRR072232, SRR072233) and/or with both workflows (EBI metagenomics, ASaiM), with the relative abundance (in percentage) in GO slim groups (cellular components, biological processes and molecular functions)}
\label{incomplete_go_slims}
\end{table}

Barplot representations of GO slim term abundances for both samples and both workflows can be difficult to interpret (*e.g* for the cellular component on Figure \ref{cellular_components}). A principal component analysis (PCA) on normalized relative abundance of GO slim term abundance inside each group simplifies visualization and interpretation (Figures \ref{cellular_components} and \ref{biological_process}).

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.55\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_samples//cellular_component_barplot.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.43\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_samples//cellular_component_pca.pdf}
    \end{minipage} 
    \caption{Barplot representation (in left, logarithm scale) and scatter diagram of principal component analysis of the normalized relative abundances (in percentage) of the cellular component GO slim terms for both samples (SRR072233 and SRR072233) and both workflows (\textit{EBI metagenomics} and ASaiM). The relative abundances of each GO slim terms is normalized by the sum of relative abundance for the found cellular component GO slim terms in both samples and with both workflows.}
    \label{cellular_components}
\end{figure}

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_samples/biological_process_pca.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_samples/molecular_function_pca.pdf}
    \end{minipage} 
    \caption{Scatter diagram of principal component analysis of the normalized relative abundances (in percentage) of the biological process (in left) and of the molecular functions (in right) GO slim terms for both samples (SRR072233 and SRR072233) and both workflows (\textit{EBI metagenomics} and ASaiM). The relative abundances of each GO slim terms is normalized by the sum of relative abundance for the found biological process GO slim terms in both samples and with both workflows.}
    \label{biological_process}
\end{figure}

Scatter representation of first plan (constitued of first two axes) of the PCA is similar for the three groups (Figures \ref{cellular_components} and \ref{biological_process}). First axis explains most of data variability (between 64\% and 87\%) and is highly negatively correlated with total abundance on both samples and both workflows of GO slim terms (Table \ref{pca_info}). Then GO slim terms found on left part of scatter representation (Figures \ref{cellular_components} and \ref{biological_process}) are highly abundant. Cellular processes related to membrane and cytoplasm are more abundant (Figure \ref{cellular_components}). Similarly, biosynthetic processes, nitrogen compound metabolic process, small molecular metabolic process, transport and DNA metabolic process are the more abundant biological processes (Figure \ref{biological_process}). Nucleotide binding is highly more abundant than other other molecular functions (Figure \ref{biological_process}). This first axis does not discrimate samples or workflows (Figures \ref{cellular_components} and \ref{biological_process}). Previous conclusions can be then extrapolated for both workflows and both samples. Results from ASaiM workflow are then similar in term of GO slim term abundances to the one obtained with *EBI metagenomics* pipeline.

\begin{table}[h!]
\centering
\begin{tabular}{llrrr}
\hline
 & & Cellular components & Biological processes & Molecular functions\\
\hline
\multicolumn{2}{c}{First axis} & & & \\
\cline{1-2}
\multicolumn{2}{l}{Explained variability} & 64\% & 87 \% & 85\%\\
Correlation with total abundance & $r^{2}$ & 0.999 & 0.999 & 0.996\\
& \textit{p-value} & $<$ 2.2 $\cdot 10^{-16}$ & $<$ 2.2 $\cdot 10^{-16}$ & $<$ 2.2 $\cdot 10^{-16}$\\
\hline
\multicolumn{2}{c}{Second axis} & & & \\
\cline{1-2}
\multicolumn{2}{l}{Explained variability} & 35\% & 13 \% & 15\%\\
\hline
\end{tabular}
\caption{Principal component analysis (PCA) axes and correlations. Total abundance corresponds for each GO slim terms to the sum of abundance of this GO slim term for both samples and both workflows.}
\label{pca_info}
\end{table}

The second axis explaining between 13\% and 35\% of overall data variability (Table \ref{pca_info}) discriminate data obtained with *EBI metagenomics* pipeline from the ones obtained with ASaiM workflow. This discrimination is secondary relatively to abundance differences in first axis. Some GO slim terms such as membrane, hydrolase activity or nitrogen compound metabolic process are over-expressed in *EBI metagenomics* results and some like biosynthetic process, plasma membrane or nucleotide binding are under-expressed (Figures \ref{cellular_components} and \ref{biological_process}).

None of the first two axes discriminates both samples. Variability between both samples is then less important than variability between both workflows and mostly variability between GO slim terms.

# Conclusion

ASaiM workflow allow a fast analysis (few hours) of raw sequences from a metagenomic dataset. Relying on Galaxy, ASaiM workflow posseses all forces of Galaxy: accessibility, reproducibility and also modularity (possibility to change parameters or steps). The results can be accessed during workflow execution.

Taxonomic analysis is accurate with *MetaPhlAn2*. From the expected taxonomy of both samples, few clades are not found or unexpected. The lowest accurate taxonomic level (species) is more precise than the one obtained with *EBI metagenomics*. 

With *HUMAnN2* results combined to *MetaPhlan2* results and GO slim term grouping, functional analyses are complete: precise and also broad overview of metabolic profile of studied microbial community and relation with observed community structure. 

Many post-treatments are also possible in ASaiM Galaxy instance. For example, most of graphic representations and most statistical analyses of this report are done inside ASaiM Galaxy instance with [dedicated workflows available for reproducibility]().

ASaiM Galaxy instance with its workflows and tools is a powerful framework to analyze shotgun raw sequence data from microbiota.

# References

