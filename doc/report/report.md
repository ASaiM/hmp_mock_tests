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
    \caption{\textit{EBI metagenomics} pipeline (version 1.0)}
    \label{ebi_pipeline}
\end{figure}

Interesting results (OTUs with taxonomic assignation and GO slim annotations) are downloaded and formatted. 

Using OTUs with taxonomic assignation, abundances of each assigned clade are extracted and several relative abundance measures are computed: relative abundances of clades for all OTUs and relative abundances of clades for OTUs with accurate taxonomic assignation (taxonomic assignation from kingdom to family). Percentage of unassigned clades is computed at different taxonomic levels (clades without more accurate taxonomic assignation).

*GO slim annotations*

## Analyses with ASaiM workflow

Both datasets are analyzed using ASaiM workflow dedicated to single-end microbiota data (Figure \ref{asaim_workflow}).

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/asaim_workflow.pdf}
    \caption{ASaiM workflow available with ASaiM Galaxy instance and used to analyze both datasets}
    \label{asaim_workflow}
\end{figure}

This workflow is available with ASaiM Galaxy instance. For this analysis, ASaiM Galaxy instance are deployed on a Debian GNU/Linux System with 8 cores Intel(R) Xeon(R) at 2.40GHz and with 32 Go of RAM. Several statistics are followed during workflow execution (Table \ref{computation_stats}).

\begin{table}[h!]
\centering
\begin{tabular}{llrr}
\hline
\multicolumn{2}{l}{Statistics} & SRR072232 & SRR072233 \\
\hline
Execution time & All & 4h44 & $\simeq$ 5h23 \\
& PRINSEQ & 0h38 & \\
& Vsearch & 16s & \\
& SortMeRNA & 0h55 & \\
& MetaPhlAN2 & 0h09 & \\
& HUMAnN2 & 3h01 & \\
\multicolumn{2}{l}{Maximum of \%CPU used} &  & \\
\multicolumn{2}{l}{Maximum RAM size used} & & \\
\hline
\end{tabular}
\caption{Computation statistics on ASaiM for both samples (SRR072233 and SRR072233)}
\label{computation_stats}
\end{table}

*Comments on the computation statistics, (installation of several hours, but relatively fast analyses after), most time consuming task*

In addition to formatting steps in workflow, taxonomic results are formatted to extract the percentage of unassigned clades at different taxonomic levels (clades without more accurate taxonomic assignation)

## Comparison of results from *EBI metagenomics* and ASaiM

Results from *EBI metagenomics* results and the ones from ASaiM are not directly comparable. Several processing steps are then needed.

With *MetaPhlAn* in ASaiM workflow, relative abundance of clades is computed on assigned reads. No count is made of non assigned reads. To compare relative abundances between *EBI metagenomics* and *ASaiM*, we focus on relative abundances computed on OTUS or reads with an accurate taxonomic assignation (taxonomic assignation from kingdom to family). These results are also compared to expected relative abundances obtained from sample descriptions (Table \ref{expected_species}). 

*Functional results*

# Results

## Pretreatments

(Table \ref{pretreatment_stats})

\begin{table}[h!]
\centering
\begin{tabular}{m{4cm}rrrrrrrr}
\hline
 & \multicolumn{4}{c}{SRR072232} & \multicolumn{4}{c}{SRR072233} \\
Sequences & \multicolumn{2}{c}{EBI} & \multicolumn{2}{c}{ASaiM} & \multicolumn{2}{c}{EBI} & \multicolumn{2}{c}{ASaiM} \\
\hline
Raw sequences & \multicolumn{4}{c}{1,225,169} & \multicolumn{4}{c}{1,386,198}\\
Sequences after pretreatments & 997,622 & 81.4\% & 1,175,853 & 96\% & 1,197,748 & 86.4\% & 1,343,451 & 96.9\% \\
rRNA sequences & 8,910 & 0.9\% & 16,016 & 1.4\% & 9,214 & 0.8\% & 13,850 & 1\%\\
non rRNA sequences & 988,712 & 99.1\% & 1,159,837 & 98.6\% & 1,188,534 & 99.2\% & 1,329,601 & 99\%\\
\hline
\end{tabular}
\caption{Statistics of pretreatments for EBI and ASaiM on both samples (SRR072233 and SRR072233)}
\label{pretreatment_stats}
\end{table}


Different thresholds for min length (100 for EBI, 60 for ASaiM (what about 100 for ASaiM?))

When PRINSEQ is run with exactly same parameters but filtering of sequences with less than 100, 1,135,008 (92.6%) and () sequences are conserved for SRR072232 and SRR072233 respectively after quality treatments. These proportion are still higher than the one for *EBI metagenomics*. Smaller length threshold with ASaiM can not then explain all difference in sequence number after pretreatments.

few rRNA sequences (metagenomics data)

## Taxonomic analyses

### Raw ASaiM results

GraPhlAn

KRONA representation: [SRR072232]() and [SRR072233]()

\begin{figure}
    \centering
    \includegraphics[width = .8\linewidth]{../../results/SRR072232/asaim_results/graphlan_on_data_39_image.png}
    \caption{GraPhlAn representation of taxonomic assignation obtained for SRR072232 with ASaiM}
    \label{graphlan_SRR072232}
\end{figure}

\begin{figure}
    \centering
    \includegraphics[width = .8\linewidth]{../../results/SRR072233/asaim_results/graphlan_on_data_39_image.png}
    \caption{GraPhlAn representation of taxonomic assignation obtained for SRR072233 with ASaiM}
    \label{graphlan_SRR072233}
\end{figure}

Higher taxonomic diversity for SRR072233 despite same taxonomy expected

Comparison with expected taxonomy, with relative abundances 

\begin{figure}
    \centering
    \includegraphics[width = .75\linewidth]{../../results/SRR072232/concatenated_results/species_abundances.pdf}
    \caption{Relative abundances of expected species for SRR072232, comparison between expected abundances and abundances obtained with ASaiM}
    \label{species_abundances_SRR072232}
\end{figure}

\begin{figure}
    \centering
    \includegraphics[width = .75\linewidth]{../../results/SRR072233/concatenated_results/species_abundances.pdf}
    \caption{Relative abundances of expected species for SRR072233, comparison between expected abundances and abundances obtained with ASaiM}
    \label{species_abundances_SRR072233}
\end{figure}

### Comparison with EBI results and expected taxonomy

#### Assignation rates

*EBI metagenomics* uses 16S sequences with *QIIME*. In ASaiM, we execute *MetaPhlAn* on non rRNA sequences, to search diverse phylogenetic markers and not only 16S ones. But, with this method, we have also higher unassignation rates (Table \ref{unassignation_rates}):

\begin{table}[h!]
\centering
\begin{tabular}{lrrrr}
\hline
 & \multicolumn{2}{c}{SRR072232} & \multicolumn{2}{c}{SRR072233} \\
Clade & EBI & ASaiM & EBI & ASaiM \\
\hline
All & 6.4\% & 62.61\% & 13\% & \\
Inside Archea & 40.15\% & 3.77\% & 29.79\% & \\ 
Inside Bacteria & 16\% & 96.24\% & 50\% & \\
\hline
\end{tabular}
\caption{Rates of unassignation for EBI and ASaiM on both samples (SRR072233 and SRR072233)}
\label{unassignation_rates}
\end{table}

We also have unexpected taxonomic assignations. For ASaiM, several species are identified as "unclassified" (Table \ref{asaim_unexpected_species}):

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

With *EBI metagenomics*, some taxonomic paths are unexpected (Table \ref{ebi_unexpected_clades}):

\begin{table}[h!]
\centering
\begin{tabular}{lrr}
\hline
Clade & SRR072232 & SRR072233\\
\hline
Methanopyraceae (family) & 0.09\% & 0.21\% \\
Paraprevotellaceae (family) & - & 0.09\% \\
Rickettsiales (order) & 5.71\% & 1.43\% \\
Cryptosporangiaceae (family) & - & 0.5\% \\
\hline
\end{tabular}
\caption{Relative abundances of unexpected clades in EBI taxonomic results for both samples (SRR072233 and SRR072233)}
\label{ebi_unexpected_clades}
\end{table}

#### Assignation, relative abundances and comparison with expectations



\begin{figure}
    \centering
    \includegraphics[width = .8\linewidth]{../../results/SRR072232/concatenated_results/family_abundances.pdf}
    \caption{Relative abundances of families for SRR072232}
    \label{family_abundances_SRR072232}
\end{figure}

\begin{figure}
    \centering
    \includegraphics[width = .8\linewidth]{../../results/SRR072233/concatenated_results/family_abundances.pdf}
    \caption{Relative abundances of families for SRR072233}
    \label{family_abundances_SRR072233}
\end{figure}

test

tezarezqfds



tezqfd

## Functional analyses


