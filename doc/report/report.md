---
title: "Validation of ASaiM framework and its workflows on HMP mock community samples"
subject_session: Sequence analysis
subtitle: "Supplementary material 2"
author:
    - Bérénice Batut
    - Clémence Defois
    - Kévin Gravouil
    - Eric Peyretaillade
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
---

ASaiM framework and its workflows are tested and validated on two mock metagenomic datasets of a controlled microbiota community (with 22 known microbial strains). These datasets are available on *EBI metagenomics* database.

Taxonomic and functional results produced by ASaiM framework are extensively analyzed and compared with results obtained with the [*EBI metagenomics* pipeline](https://www.ebi.ac.uk/metagenomics/pipelines/1.0) [@hunter_ebi_2014]. Details about these analyses (workflows, scripts) are available on a [dedicated GitHub repository](https://github.com/ASaiM/hmp_mock_tests) and results with all intermediary and final files on [Zenodo](https://zenodo.org/).

The main workflow produces accurate and precise taxonomic assignations, wide functional results (gene families, pathways, GO slim terms) and relations between taxonomic and functional results, in few hours on a commodity computer. Hence, these analyses validate ASaiM framework and its main workflow.

# Data

[Two mock community samples](https://www.ebi.ac.uk/metagenomics/projects/SRP004311) for Human Microbiome Project (HMP) are available on [*EBI metagenomics* database](https://www.ebi.ac.uk/metagenomics/). Both samples contain a genomic mixture of 22 microbial strains (Table \ref{expected_species}) with differences in abundances of the strains. In first sample ([SRR072232](https://www.ebi.ac.uk/metagenomics/projects/SRP004311/samples/SRS121012/runs/SRR072232/results/versions/1.0)), the rRNA operon counts vary by up to four orders of magnitude per strains (Table \ref{expected_species}), whereas second sample ([SRR072233](https://www.ebi.ac.uk/metagenomics/projects/SRP004311/samples/SRS121011/runs/SRR072233/results/versions/1.0)) contains equimolar ribosomal rRNA operon counts per strain (Table \ref{expected_species}).

Both samples were sequenced using 454 GS FLX Titanium to get 1,225,169 raw metagenomic sequences for first dataset and 1,386,198 raw metagenomic sequences for second dataset.

# Methods

Both datasets have been analyzed using the ASaiM framework. The results are extensively analyzed and compared to expected results based on reference genomes and *EBI metagenomics* results. Details about these analyses (workflows, scripts) are available on a [dedicated GitHub repository](https://github.com/ASaiM/hmp_mock_tests) and results with all intermediary and final files on [Zenodo](https://zenodo.org/).

## Abundance computation using mapping on reference genomes

Targeted abundances of strains are based on rRNA operon counts added for each strains to simulate the mock community. To get "real" abundances of expected strains in metagenomic datasets, raw reads are mapped on reference genomes of expected strains using BWA [@li_fast_2009;@li_fast_2010] (using default parameters). Relative abundances based on mapping results are compared to relative abundances based on rRNA operon counts as described in sample metadata (Figure \ref{mapping_comparison}).

Composition based on mapping-based relative abundances of strains are similar to composition of targeted relative abundance (Figure \ref{mapping_comparison}) with Bray-Curtis dissimilarity scores equal to 0.338 for SRR02232 and 0.479 for SRR072233. For SRR02232, similar variations in abundances between species are then observed using mapping and rRNA operon count (Figure \ref{mapping_comparison}). Observations are different for SRR072233 (Figure \ref{mapping_comparison}): expected abundances (based on RNA operon abundances) are identical for all species, but unexpected variations are observed for mapping based abundances. These differences between expected abundances (from RNA operon counts) and mapping-based abundances may be due to bias induced during biological manipulations or sequencing. The observed differences can also be explained by copy number variation of targeted rRNA operon between species. Indeed, the targeted abundances are based on rRNA operon count. The number of rRNA operon counts is not identical for all targeted strains. Hence, even with identical targeted abundances of rRNA operon (*e.g.* for SRR072233)

\newpage
\thispagestyle{empty}
\newgeometry{top=2cm, bottom=2cm, left=2cm, right=2cm}
\begin{landscape}
\begin{table}
\begin{tabular}{llm{2.5cm}llllm{2.5cm}m{2.5cm}|rr}
\hline
\multicolumn{9}{c|}{Taxonomy} & \multicolumn{2}{c}{Targeted abundances (\%)}\\
Domain & Kingdom & Phylum & Class & Order & Family & Genus & Species & Strains & SRR072232 & SRR072233 \\
\hline
Archaea & Archaea & Euryarchaeota & Methanobacteria & Methanobacteriales& Methanobacteriaceae & \textit{Methanobrevibacter} & \textit{Methanobrevibacter smithii} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000016525.1_ASM1652v1/}{ATCC 35061} & 1.797 $\cdot 10^{1}$ & 4.545 \\
\hline
Bacteria & Bacteria & Actinobacteria & Actinobacteria & Actinomycetales & Actinomycetaceae & \textit{Actinomyces} & \textit{Actinomyces odontolyticus} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000154225.1_ASM15422v1/}{ATCC 17982} & 1.797 $\cdot 10^{-2}$ & 4.545 \\
\cline{6-11}
 &  &  &  &  & Propionibacteriaceae & \textit{Propionibacterium} & \textit{Propionibacterium acnes} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000008345.1_ASM834v1/}{DSM 16379} & 1.797 $\cdot 10^{-1}$ & 4.545 \\
\cline{3-11}
 & & Bacteroidetes & Bacteroidia & Bacteroidales & Bacteroidaceae & \textit{Bacteroides} & \textit{Bacteroides vulgatus} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000012825.1_ASM1282v1/}{ATCC 8482} & 1.797 $\cdot 10^{-2}$ & 4.545 \\
\cline{3-11}
& & Deinococcus-Thermus & Deinococci & Deinococcales & Deinococcaceae & \textit{Deinococcus} & \textit{Deinococcus radiodurans} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000008565.1_ASM856v1/}{DSM 20539} & 1.797 $\cdot 10^{-2}$ & 4.545 \\
\cline{3-11}
& & Firmicutes & Bacilli & Bacillales & Bacillaceae & \textit{Bacillus} & \textit{Bacillus cereus thuringiensis} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000008005.1_ASM800v1/}{ATCC 10987} & 1.797 & 4.545\\
\cline{6-11}
& & & & & Listeriaceae & \textit{Listeria} & \textit{Listeria monocytogenes} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000196035.1_ASM19603v1/}{ATCC BAA-679} & 1.797 $\cdot 10^{-1}$ & 4.545 \\
\cline{6-11}
& & & & & Staphylococcaceae & \textit{Staphylococcus} & \textit{Staphylococcus aureus} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000153665.1_ASM15366v1/}{ATCC BAA-1718} & 1.797 & 4.545 \\
\cline{8-11}
& & & & & & & \textit{Staphylococcus epidermidis} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000007645.1_ASM764v1/}{ATCC 12228} & 1.797 $\cdot 10^{1}$ & 4.545 \\
\cline{5-11}
& & & & Lactobacillales & Enterococcaceae & \textit{Enterococcus} & \textit{Enterococcus faecalis} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000172575.2_ASM17257v2/}{ATCC 47077} & 1.797 $\cdot 10^{-2}$ & 4.545\\
\cline{6-11}
& & & & & Lactobacillaceae & \textit{Lactobacillus} & \textit{Lactobacillus gasseri} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000014425.1_ASM1442v1/}{DSM 20243} & 1.797 $\cdot 10^{-2}$ & 4.545\\
\cline{6-11}
& & & & & Streptococcaceae & \textit{Streptococcus} & \textit{Streptococcus agalactiae} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000007265.1_ASM726v1/}{ATCC BAA-611} & 1.797 & 4.545\\
\cline{8-11}
& & & & & & & \textit{Streptococcus mutans} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000007465.2_ASM746v2/}{ATCC 700610} & 1.797 $\cdot 10^{1}$ & 4.545\\
\cline{8-11}
& & & & & & & \textit{Streptococcus mitis oralis pneumoniae} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000006885.1_ASM688v1/}{ATCC BAA-334} & 1.797 $\cdot 10^{-2}$ & 4.545\\
\cline{4-11}
& & & Clostridia & Clostridiales & Clostridiaceae & \textit{Clostridium} & \textit{Clostridium beijerinckii} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000016965.1_ASM1696v1/}{ATCC 51743} & 1.797 & 4.545\\
\cline{3-11}
& & Proteobacteria & Alphaproteobacteria & Rhodobacterales & Rhodobacteraceae & \textit{Rhodobacter} & \textit{Rhodobacter sphaeroides} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000012905.2_ASM1290v2/}{ATCC 17023} & 1.797 $\cdot 10^{1}$ & 4.545\\
\cline{4-11}
& & & Betaproteobacteria & Neisseriales & Neisseriaceae & \textit{Neisseria} & \textit{Neisseria meningitidis} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000008805.1_ASM880v1/}{ATCC BAA-335} & 1.797 $\cdot 10^{-1}$ & 4.545\\
\cline{4-11}
& & & Epsilonproteobacteria & Campylobacterales & Helicobacteraceae & \textit{Helicobacter} & \textit{Helicobacter pylori} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000008525.1_ASM852v1/}{ATCC 700392} & 1.797 $\cdot 10^{-1}$ & 4.545\\
\cline{4-11}
& & & Gammaproteobacteria & Pseudomonadales & Moraxellaceae & \textit{Acinetobacter} & \textit{Acinetobacter baumannii} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000015425.1_ASM1542v1/}{ATCC 17978} & 1.797 $\cdot 10^{-1}$ & 4.545\\
\cline{6-11}
& & & & & Pseudomonadaceae & \textit{Pseudomonas} & \textit{Pseudomonas aeruginosa} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000006765.1_ASM676v1/}{ATCC 47085} & 1.797 & 4.545\\
\cline{5-11}
& & & & Enterobacteriales & Enterobacteriaceae & \textit{Escherichia} & \textit{Escherichia coli} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000005845.2_ASM584v2/}{ATCC 70096} & 1.797 $\cdot 10^{1}$ & 4.545\\
\hline
Eukaryotes & Fungi & Ascomycota & Saccharomycetes & Saccharomycetales & Debaryomycetaceae & \textit{Candida} & \textit{Candida albicans} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000182965.2_ASM18296v2/}{SC5314} & 1.797 $\cdot 10^{-2}$ & 4.545 \\
\hline
\end{tabular}
\caption{Expected strains, their taxonomy and their targeted relative abundance (percentage) based on ribosomal RNA operon counts (abundance, from metadata on EBI metagenomics database) on both samples (SRR072232 and SRR072233)}
\label{expected_species}
\end{table}
\end{landscape}
\newpage
\restoregeometry

, the abundance of strains may differ. It will then induce a difference between relative abundance based on mapping reads on whole genome and the targeted relative abundance based on rRNA operon counts because of rRNA copy variation number.

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/mapping_expectation_barplot.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072233/mapping_expectation_barplot.pdf}
    \end{minipage}
    \caption{Comparison of relative abundances (percentage, in log scale) between expectation given the ribosomal RNA operon counts (green, Table \ref{expected_species}) and mapping against reference genomes for both samples (SRR072232 on left, SRR072233 on right)}
    \label{mapping_comparison}
\end{figure}

As taxonomic analyses in *EBI metagenomics* and ASaiM workflows are executed on metagenomic sequences, mapping based abundances are used as expected abundances, instead of relative abundances based on rRNA operon counts from metadata.

## Analyses using *EBI Metagenomics*

Both datasets have been analysed with [*EBI metagenomics* pipeline (Version 1.0)](https://www.ebi.ac.uk/metagenomics/pipelines/1.0) (Figure \ref{ebi_pipeline}). Results are downloaded and formatted to allow comparisons with ASaiM results.

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/ebi_workflow.pdf}
    \caption{\textit{EBI metagenomics} pipeline (version 1.0).
    The grey boxes correspond to data, the blue boxes to pretreatment steps, the red boxes to functional analysis steps and the green boxes to taxonomic analysis steps.}
    \label{ebi_pipeline}
\end{figure}

OTUs with taxonomic assignation are extracted and aggregated to compute relative abundances of each clade at all taxononic levels.

For functional analysis, 3 types of results are generated with *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}): matches with InterPro, complete GO annotations and GO slim annotations. Here for comparison purpose (Figure \ref{asaim_workflow}), we focus on GO slim annotations. Annotations are formatted to extract relative abundances (in percentage) of GO slim term annotations inside each GO slim term categories (cellular components, biological processes and molecular functions).

## Analyses using ASaiM framework

Main workflow (Figure \ref{asaim_workflow}) of ASaiM framework is used to analyze both datasets

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/asaim_workflow.pdf}
    \caption{ASaiM workflow for analysis of raw single-end microbiota sequences. This workflow is available with ASaiM Galaxy instance and used to analyze both datasets. The grey boxes correspond to data, the blue boxes to preprocessing steps, the red boxes to functional analysis steps and the green boxes to taxonomic analysis steps.}
    \label{asaim_workflow}
\end{figure}

For these analyses, ASaiM framework is deployed on a computer with Debian GNU/Linux System, 8 cores Intel(R) Xeon(R) at 2.40 GHz and 32 Go of RAM. During workflow execution, size of used memory and execution time are checked (Table \ref{computation_stats}). Workflow execution is relatively fast: < 5h and < 5h30 for datasets with 1,225,169 and 1,386,198 sequences respectively (Table \ref{computation_stats}). The most time-consuming step is functional assignation with *HUMAnN2* [@abubucker_metabolic_2012] which last $\simeq$ 64% of overall time execution (Table \ref{computation_stats}). Size of the process in memory is stable over workflow execution (variability inferior to 40 kb) (Table \ref{computation_stats}).

\begin{table}[h!]
\centering
\begin{tabular}{llrr}
\hline
\multicolumn{2}{l}{Statistics} & SRR072232 & SRR072233 \\
\hline
Execution time & \textbf{Whole workflow} & \textbf{4h44} & \textbf{5h22} \\
\cline{2-4}
& PRINSEQ & 0h38 & 0h44\\
& Vsearch & 16s & 19s\\
& SortMeRNA & 0h55 & 0h58\\
& MetaPhlAN2 & 0h09 & 0h10\\
& HUMAnN2 & 3h01 & 3h26\\
\hline
Size of the process in memory (kb) & Min & 1,515,732 & 1,515,732\\
 & Mean & 1,515,744 & 1,515,743\\
 & Max & 1,515,768 & 1,515,764\\
\hline
\end{tabular}
\caption{Computation statistics on ASaiM for both samples (SRR072233 and SRR072233)}
\label{computation_stats}
\end{table}

Comparative analysis workflows available with ASaiM framework are used to compare taxonomic and functional results of both datasets.

## Comparison of *EBI metagenomics* results and ASaiM results

*EBI metagenomics* results and ASaiM ones are not directly comparable. Several processing steps are then needed.

With *MetaPhlAn* in ASaiM workflow, relative abundance of clades is computed on assigned reads. No count is made of non assigned reads. To compare relative abundances between both pipelines, we focus on relative abundances computed on OTUS or reads with a complete taxonomic assignation from kingdom to family. These results are also compared to relative abundances computed using mapping of raw reads on reference genomes.

In both *EBI metagenomics* and ASaiM workflows (Figures \ref{ebi_pipeline} and \ref{asaim_workflow}), functional matches are grouped into GO slims terms. These terms are a subset of the terms in the whole Gene Ontology with a focus on microbial metabolic functions. They give a broad overview of the ontology content. To compare *EBI metagenomics* and ASaiM results, relative abundance of GO slim terms for both samples and both workflows are concatenated and compared, given workflow depicted in Figure \ref{go_slim_comparison_workflow}.

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/go_slim_comparison_workflow.pdf}
    \caption{Workflow to compare GO slim annotation abundances between samples (SRR072232, SRR072233) and workflows (\textit{EBI metagenomics}, ASaiM). This workflow is available with ASaiM Galaxy instance. The grey boxes correspond to data, the blue boxes to processing steps.}
    \label{go_slim_comparison_workflow}
\end{figure}

# Results

## Results of preprocessing in pipelines

In both workflows (Figures \ref{ebi_pipeline} and \ref{asaim_workflow}), raw sequences are pre-processed before any taxonomic or functional analysis. These preprocessing steps include quality control to remove low quality, small or duplicated sequences and also a step to sort rRNA/rDNA sequences from non rRNA/rDNA sequences (Figures \ref{ebi_pipeline} and \ref{asaim_workflow}). The used tools and parameters for these pretreatments are different between *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}) and ASaiM workflow (Figure \ref{asaim_workflow}), inducing different pretreatment outputs (Table \ref{pretreatment_stats}).

\begin{table}[h!]
\centering
\begin{tabular}{m{4cm}rrrrrrrr}
\hline
 & \multicolumn{4}{c}{SRR072232} & \multicolumn{4}{c}{SRR072233} \\
Sequences & \multicolumn{2}{c}{EBI} & \multicolumn{2}{c}{ASaiM} & \multicolumn{2}{c}{EBI} & \multicolumn{2}{c}{ASaiM} \\
\hline
Raw sequences & \multicolumn{4}{c}{1,225,169} & \multicolumn{4}{c}{1,386,198}\\
Sequences after quality control and dereplication & 997,622 & 81.4\% & 1,175,853 & 96\% & 1,197,748 & 86.4\% & 1,343,451 & 96.9\% \\
rDNA sequences & 8,910 & 0.9\% & 16,016 & 1.4\% & 9,214 & 0.8\% & 13,850 & 1\%\\
non rDNA sequences & 988,712 & 99.1\% & 1,159,837 & 98.6\% & 1,188,534 & 99.2\% & 1,329,601 & 99\%\\
\hline
\end{tabular}
\caption{Statistics of pretreatments for EBI and ASaiM on both samples (SRR072233 and SRR072233)}
\label{pretreatment_stats}
\end{table}

Sequence number after quality control and dereplication is different in *EBI metagenomics* and ASaiM workflow results (Table \ref{pretreatment_stats}). With ASaiM, more sequences (> 96 \%) are conserved during these first steps of quality control and dereplication than with *EBI metagenomics* (< 87 \%, Table \ref{pretreatment_stats}). This difference may be explained by differences in threshold for minimum length. In *EBI metagenomics* pipeline, sequences with less than 100 nucleotides are removed, while in ASaiM the threshold is fixed to 60 nucleotides. However, this threshold difference does not explain all the observed difference in sequence number after quality control and dereplication. Indeed, when in ASaiM quality control with PRINSEQ [@schmieder_quality_2011] is run with exactly same parameters but filtering of sequences with less than 100 nucleotides, 1,135,008 (92.6%) and 1,304,023 (94.1%) sequences are conserved for SRR072232 and SRR072233 respectively after quality control and dereplication. These proportion are still higher than the one observed with *EBI metagenomics* pipeline (Table \ref{pretreatment_stats}). Smaller length threshold with ASaiM does not then explain all difference in sequence number after quality control and dereplication. Differences are induced by used tools and their underlying algorithms and implementations.

In both datasets and with both workflows, few rDNA sequences are found in datasets (Table \ref{pretreatment_stats}). These datasets are metagenomic datasets and then focus on whole genome sequences. Few copies of rRNA genes are found in organisms (bacteria, archeae or eukaryotes) and are then expected in metagenomic sequences. Despite small number of sequences, a difference of rRNA sequence number is observed between *EBI metagonomics* and ASaiM workflows (Table \ref{pretreatment_stats}): higher proportions of rDNA sequences are systematically found with ASaiM workflow. *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}) uses *rRNASelector* [@lee_rrnaselector:_2011] to select rDNA  bacterial and archaeal sequences (no eukaryotes sequences). In ASaiM workflow (Figure \ref{asaim_workflow}), rRNA sequences are sorted using *SortMeRNA* [@kopylova_sortmerna:_2012] and 8 databases for bacteria, archaea and also eukaryotes rRNA. < 5% of all sequences are matched against databases dedicated to eukaryotes rRNA sequences, and then does not explain all differences of rRNA sequence proportions between *EBI metagenomics* and ASaiM. This difference may be due to completness of the databases: databases used by *rRNASelector* are older and probably less complete than SILVA (v119) databases used by *SortMeRNA*.

After pretreatments, for both samples, more sequences are then conserved for taxonomic and functional analyses in ASaiM workflow than in *EBI metagenomics* pipeline (Table \ref{pretreatment_stats}).

## Taxonomic analyses

The mock metagenomic datasets contain sequences of 22 known microbial strains. The expected taxonomy inside the datasets is then known as well as the expected relative abundances (based on mapping on reference genomes, Figure \ref{mapping_comparison}). We can then use this information (Figure \ref{expected_taxonomy}) to analyze ASaiM framework taxonomic results and compare them to *EBI metagenomics* pipeline taxonomic results.

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/expected_taxonomy.pdf}
    \caption{Expected taxonomy for SRR072232 (left) and SRR072233 (right) from domains to species. Circle diameters at each taxonomic levels are proportional to mapping-based relative abundance of corresponding taxon.}
    \label{expected_taxonomy}
\end{figure}

### ASaiM taxonomic results

In ASaiM workflow (Figure \ref{asaim_workflow}), *MetaPhlAN* (2.0) [@truong_metaphlan2_2015;@segata_metagenomic_2012] is used for taxonomic analyses on sequences after preprocessing. *MetaPhlAn* profiles the microbial community structure using a database of unique clade-specific marker genes identified from 17,000 reference genomes. *MetaPhlAn* execution is fast in ASaiM workflow (less than 10 minutes for > 1,100,000 sequences, Table \ref{computation_stats}).

Raw *MetaPhlAn* results consist in a plain text file with relative abundance of clades at different taxonomic levels. Visualisation tools help to represent *MetaPhlAn* results. In the ASaiM framework, two tools are available: *Krona* [@ondov_interactive_2011] for interactive representations of taxonomic assignation and *GraPhlan* for static representations. Original static representations are modified (*e.g.* colors, legend) to help comparison with expected taxonomy (Figure \ref{asaim_taxonomy}).

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/asaim_taxonomy.pdf}
    \caption{Taxonomy for SRR072232 (left) and SRR072233 (right) from domains to species, found with ASaiM framework. Circle diameters at each taxonomic levels are proportional to relative abundance of corresponding taxon. Colors and family numbers are the same as the ones used in Figure \ref{expected_taxonomy}. Gray circles and lines represent unexpected lineages.}
    \label{asaim_taxonomy}
\end{figure}

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

Despite same expected species, taxonomic diversity in SRR072232 dataset is reduced compared to the one in SRR072233 dataset (Figure \ref{asaim_taxonomy}). Less taxons are found for each taxonomic levels. And, from 22 expected species (Table \ref{expected_species}), 17 are found for SRR072232 and 20 for SRR072233 (Figure \ref{species_abundances}). The 2 expected species (*Candidata albicans* and *Lactobacillus gasseri*) missing in SRR072233 dataset are also missing in SRR072232 dataset (Figure \ref{species_abundances}). Phylogenetic markers for these species  may be missing in the database used by *MetaPhlAn*. On the other hand, few sequences of these species in SRR072233 are found using mapping on expected species genomes. The phylogenetic signal may be too low to detect these species. Hence, all species with mapping-based abundance smaller than 0.1\% are not found using ASaiM for both datasets  (Figure \ref{species_abundances}).

For SRR072232 datasets, two species with mapping-based abundance higher than 0.1\% are not found: *Candida albicans* and *Bacillus cereus thuringiensis*. The first species is not found also with ASaiM in SRR072333, phylogenetic markers for this species may be missing in *MetaPhlAn2* database. As the second species is found with ASaiM in SRR072333, same explanation based on incompletness of reference database.

### Comparison of ASaiM taxonomic results with EBI metagenomics taxonomic results

After these first comparisons between ASaiM taxonomic results and expected ones, we compare ASaiM taxonomic results and *EBI metagenomics* taxonomic results.

In *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}), *QIIME* [@caporaso_qiime_2010] is used on 16S sequences to identify OTUs and taxonomic assignation for these OTUs. In ASaiM (Figure \ref{asaim_workflow}), *MetaPhlAn* is executed on sequences after quality control and dereplication, without any sorting step. *MetaPhlAn* searches diverse phylogenetic markers on all sequence types (rDNA, non rDNA, ...), not only 16S ones as *QIIME* [@caporaso_qiime_2010] does. Among so different sequences, the proportion of sequences with precise and "unique" phylogenetic markers is smaller. With *MetaPhlAn*, the percentage of unassigned reads is $\simeq$ 9 times higher than with *QIIME* (SRR072232: 6.4\% with *EBI metagenomics* against 62.61\% with ASaiM; SRR072233: 13\% with *EBI metagenomics* against 53.93\% with ASaiM). On the other hand, the raw number of assigned sequences using ASaiM framework is >52 times higher than the raw number of assigned sequences using *EBI metagenomics* pipeline. Taxonomic assignations within ASaiM framework are then based on more sequences and more statistically supported than taxonomic assignations from *EBI metagenomics* pipeline.

Moreover, taxonomic lineages from *EBI metagenomics* are limited to family level (Figure \ref{ebi_taxonomy}), while they go to species level with ASaiM (Figure \ref{asaim_taxonomy}). *MetaPhlAn* gives taxonomic assignations which are more complete and statistically supported.

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/ebi_taxonomy.pdf}
    \caption{Taxonomy for SRR072232 (left) and SRR072233 (right) from domains to families, found with EBI metagenomics pipeline. Circle diameters at each taxonomic levels are proportional to relative abundance of corresponding taxon. Colors and family numbers are the same as the ones used in Figure \ref{expected_taxonomy}. Gray circles and lines represent unexpected lineages.}
    \label{ebi_taxonomy}
\end{figure}

With both *EBI metagenomics* pipeline and ASaiM framework, some observed taxonomic assignations are unexpected (Table \ref{unexpected_clades}, Figures \ref{asaim_taxonomy} and \ref{ebi_taxonomy}). For ASaiM framework, 3 species in each sample are identified as "unclassified" (Table \ref{unexpected_clades}): they are affiliated to the correct genus but not to correct species. Corresponding sequences may be then incompletely annotated and affiliated. The expected species (*Escherichia* unclassified, *Pseudomonas* unclassified, *Methanobrevibacter* unclassified, *Deinococcus* unclassified) are observed in datasets (Figure \ref{asaim_taxonomy}), but in lower abundance than expected. If sequences corresponding to close unclassified species are correctly affiliated, these species would have observed relative abundances closer to mapping-based abundances.

\begin{table}[h!]
\centering
\begin{tabular}{llrrrr}
\hline
 & & \multicolumn{2}{c}{SRR072232} & \multicolumn{2}{c}{SRR072233}\\
Taxonomic level & Clade & EBI & ASaiM & EBI & ASaiM \\
\hline
Class & & & & &\\
& Methanopyri & 0.09\% & & 0.21\% & \\
\hline
Order & & & & & \\
& Rickettsiales & 5.71\% & & 1.43\% & \\
& Methanopyrales & 0.09\% & & 0.21\% & \\
\hline
Family & & & & & \\
& Rickettsiales mitochondria & 5.71\% & & 1.43\% & \\
& Methanopyraceae & 0.09\% & & 0.21\% & \\
& Paraprevotellaceae & & & 0.09\% & \\
& Cryptosporangiaceae & & & 0.5\% & \\
\hline
Genus & & \textit{No information} & & \textit{No information} & \\
\hline
Species & & \textit{No information} & & \textit{No information} & \\
& \textit{Escherichia} unclassified & & 4.85\% & & 0.8\% \\
& \textit{Pseudomonas} unclassified & & 1.12\% & & 0.56\% \\
& \textit{Methanobrevibacter} unclassified & & & & 0.24\% \\
& \textit{Deinococcus} unclassified & & 0.16\% & & \\
\hline
\end{tabular}
\caption{Relative abundances of unexpected clades at different taxonomic levels in taxonomic results of \textit{EBI metagenomics} and ASaiM framework for both samples (SRR072233 and SRR072233)}
\label{unexpected_clades}
\end{table}

With *EBI metagenomics*, taxonomic levels of unexpected clades are higher (class, order and family) than taxonomic level of unexpected clades in ASaiM framework (species, Table \ref{unexpected_clades}, Figure \ref{ebi_taxonomy}). Taxonomic assignations with *MetaPhlAN* are then more accurate and precise. As the most precise taxomic level for *EBI metagenomics* is family (Figure \ref{ebi_taxonomy}), further comparisons  focus on this level (Figure \ref{family_abundances}).

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/concatenated_family_abundances.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072233/concatenated_family_abundances.pdf}
    \end{minipage}
    \caption{Relative abundances (percentage, log scale) of expected families for SRR072232 (left) and SRR072233 (right) with comparison between mapping-based relative abundances (red thin bars), abundances obtained with \textit{EBI metagenomics} (green wide bars) and abundances obtained with ASaiM (blue wide bars).}
    \label{family_abundances}
\end{figure}

Similarly to previous observations on raw ASaiM results, species with mapping-based abundance smaller than 0.1\% are found neither with ASaiM nor with *EBI metagenomics* (Figure \ref{family_abundances}). Nonetheless, the detection threshold seems slightly smaller for *EBI metagenomics*: for SRR072232, Listeriaceae family is detected with *EBI metagenomics* and not with ASaiM (Figure \ref{family_abundances}). On the other hand, Bacillaceae and Debaryomycetaceae families are not found with *EBI metagenomics* for both datasets (Figure \ref{family_abundances}), despite mapping-based abundance higher than 0.1\%. Used databases may be then incomplete regarding some phylogenetic markers, particularly the ones corresponding to missing families.

Variations in observed abundances for *EBI metagenomics* or ASaiM correspond to variations in mapping-based abundances (Figure \ref{species_abundances}): small observed abundances for small mapping-based abundances and high observed abundances for high mapping-based abundances. For a broader comparison, a principal coordinate analysis (PCoA) is computed, for each sample, on Bray-Curtis distances on relative abundances of families (Figure \ref{family_pcoa}).

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.43\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/concatenated_family_abundance_pcoa.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.43\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072233/concatenated_family_abundance_pcoa.pdf}
    \end{minipage}
    \caption{Scatter diagram of principal coordinate analysis of the Bray-Curtis dissimilarity scores computed on relative abundances of families for SRR072232 (left) and SRR072233 (right).}
    \label{family_pcoa}
\end{figure}

For SRR072232, *EBI metagenomics* results on family relative abundances are closer to expected abundances than ASaiM framework results are (Figure \ref{family_pcoa}). This observation is not conserved for SRR072233 (Figure \ref{family_pcoa}). The Bray-Curtis dissimilarity scores are close to 0 (Table \ref{taxo_distances}): communities from expectation, *EBI metagenomics* or ASaiM framework have then similar family compositions. For species, the observations are different (Table \ref{taxo_distances}). No information is available on species composition with *EBI metagenomics* and dissimilarity scores are then equal to 1. With ASaiM framework, dissimilarity scores are slightly higher for species than for families but they remain close to 0. Composition in term of species are then similar in expected and ASaiM framework communities.

\begin{table}[h!]
\centering
\begin{tabular}{ll|rrr|rrr}
\hline
 & & \multicolumn{3}{c}{SRR072232} & \multicolumn{3}{c}{SRR072233}\\
 & & Expected & EBI & ASaiM & Expected & EBI & ASaiM \\
\hline
& Expected & - & 0.101 & 0.146 & - & 0.132 & 0.133\\
Family & EBI & & - & 0.111 & & - & 0.213\\
& ASaiM & & & - & & & -\\
\hline
& Expected & - & 1 & 0.178 & - & 1 & 0.140\\
Species & EBI & & - & 1 & & - & 1\\
& ASaiM & & & - & & & -\\
\hline
\end{tabular}
\caption{Bray-Curtis dissimilarity scores on relative abundances of families and species for both samples (SRR072233 and SRR072233)}
\label{taxo_distances}
\end{table}

ASaiM framework gives taxonomic results which are accurate, complete, precise and statistically supported. Moreover, the community structure found with the ASaiM framework is close to expected community structure of the mock community.

## Functional analyses

### ASaiM functional results

In ASaiM framework (Figure \ref{asaim_workflow}), [*HUMAnN*2](http://huttenhower.sph.harvard.edu/humann2) [@abubucker_metabolic_2012] is used for functional analyses. This tool profiles presence/absence and abundance of UniRef50 gene families [@suzek_uniref_2015] and MetaCyc pathways [@caspi_metacyc_2014] from metagenomic/metatranscriptomic datasets. It then describes the metabolic profil of a microbial community with three outputs: abundances of UniRef50 gene families, coverage and abundance of MetaCyc pathways. In both samples, > 90,000 UniRef50 gene families and > 480 MetaCyc pathways (Table \ref{humann2_informations}) are reconstructed from > 1,100,000 non rDNA sequences (Table \ref{pretreatment_stats}).

\begin{table}[h!]
\centering
\begin{tabular}{lrrrr}
\hline
& \multicolumn{2}{c}{UniRef50 gene families} & \multicolumn{2}{c}{MetaCyc pathways}\\
& SRR072232 & SRR072233 & SRR072232 & SRR072233 \\
\hline
Number & 98,569 & 129,691 & 487 & 500\\
Similar & \multicolumn{2}{c}{44,933} & \multicolumn{2}{c}{475} \\
\% of similar inside all & 45.59\% & 34.65\% & 97.54\% & 95\% \\
Relative abundance (\%) & 89.16\% & 50.67\% & 99.85\% & 99.53\%\\
\hline
\end{tabular}
\caption{Global information about UniRef50 gene families and MetaCyc pathways obtained with \textit{HUMAnN2} for both samples (SRR072233 and SRR072233). For each characteristics (gene families and pathways), several information is extracted: all number, number percentage and relative abundance (\%) of similar characteristics.}
\label{humann2_informations}
\end{table}

The used mock datasets are constitued of metagenomic sequences from genomic mixture of 22 microbial strains (Table \ref{expected_species}). The datasets differ on abundance of the 22 strains (Table \ref{expected_species}). Similar metabolic functions made by same species are then supposed to be found in both datasets, but with different abundances.

Differences of metabolic functions between both datasets are observed. Sets of gene families are different: 44,933 gene families are found in both samples (<46\% for both samples, Table \ref{humann2_informations}). But different gene families have a limited impact on overall metabolism (< 50\% of relative abundance, Table \ref{humann2_informations}). They may correspond to gene families which are difficult to detect because they are not abundant or they are "done" by organisms in low abundances. Global metabolism functions such as pathways are similar in both datasets (> 95\% of similar pathways representing > 99.5\% of overall abundance, Table \ref{humann2_informations}). Hence, the unexpected observed differences are limited and may be due to bias induced by low abundances and detection threshold.

On the other hand, abundances of similar metabolic functions are different (Figure \ref{similar_characteristics_abundances}). Hence similar metabolic functions made by same species are found in both datasets in different abundances, as expected.

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_asaim_results/functional_results/raw_gene_families.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_asaim_results/functional_results/raw_pathways.pdf}
    \end{minipage}
    \caption{Normalized relative abundances (\%) for similar UniRef50 gene families (left) and MetaCyc pathways (right) for both samples (SRR072233 and SRR072233). The relative abundances of each similar characteristics (gene families or pathways) is computed with \textit{HUMAnN2} and normalized by the sum of relative abundance for all similar characteristics.}
    \label{similar_characteristics_abundances}
\end{figure}

With more than 90,000 gene families and almost 500 pathways, the metabolic profile of studied microbial community is too large to get a broad overview. Each gene family and pathway is precise and related to specific metabolic functions. This information is interesting when you need detailed metabolic information and to go deeply inside metabolic profil. To get a broad overview of the metabolic processes, UniRef50 gene families and even MetaCyc pathways are too numerous and too precise. UniRef50 gene families and their abundances are then grouped into Gene Ontology (GO) slim terms (Figure \ref{go_abundances}). For both datasets, we observe similar profiles of GO slim terms (Figure \ref{go_abundances}).

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_asaim_results/functional_results/cellular_component.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_asaim_results/functional_results/biological_process.pdf}
    \end{minipage}
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_asaim_results/functional_results/molecular_function.pdf}
    \end{minipage}
    \caption{Relative abundances of GO slim terms in SRR072232 and SRR072233 for cellular components (top left), biological processes (top right) and molecular function (bottom)}
    \label{go_abundances}
\end{figure}

Both communities, with same expected strains but in different abundances, have different metabolic profiles. As expected, the difference are not mostly on metabolic functions, but on abundances of these functions.

### Comparison of ASaiM functional results with *EBI metagenomics* results

In ASaiM workflow (Figure \ref{asaim_workflow}), UniRef50 gene families and their abundances are computed with *HUMAnN2*. In *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}), functional analyses are based on InterPro and its identifiants. These functional results are then not directly comparable. But, in both workflows, UniRef50 gene families and InterPro proteins are grouped into Gene Ontology slim terms to get a broad overview of functional profile of the community.

Barplot representations of GO slim term abundances for both samples and both workflows can be difficult to interpret (*e.g.* for cellular components, Figure \ref{cellular_components}). Bray-Curtis dissimilarity scores are then computed on normalized relative abundance of GO slim term abundance inside each category to simplify comparisons (Table \ref{go_slim_distances}).

\begin{figure}[h!]
    \centering
    \includegraphics[width = .55\linewidth]{../images/concatenated_go_slim_terms/cellular_component_barplot.pdf}
    \caption{Barplot representation (logarithm scale) of the normalized relative abundances (in percentage) of the cellular component GO slim terms for both samples (SRR072233 and SRR072233) and both workflows (\textit{EBI metagenomics} and ASaiM). The relative abundances of each GO slim terms is normalized by the sum of relative abundance for the found cellular component GO slim terms in both samples and with both workflows.}
    \label{cellular_components}
\end{figure}

\begin{table}[h!]
\centering
\begin{tabular}{lllrrrr}
\hline
& & & \multicolumn{2}{c}{SRR072232} & \multicolumn{2}{c}{SRR072233}\\
 & & & EBI & ASaiM & EBI & ASaiM\\
\hline
& SRR072232 & EBI & - & 0.319 & 0.041 & 0.332\\
Biological & & ASaiM & & - & 0.327 & 0.053\\
processes & SRR072233 & EBI & & & - & 0.338\\
 & & ASaiM & & & & -\\
\hline
& SRR072232 & EBI & - & 0.578 & 0.047 & 0.587\\
Cellular & & ASaiM & & - & 0.580 & 0.121\\
components & SRR072233 & EBI & & & - & 0.552\\
 & & ASaiM & & & & -\\
\hline
& SRR072232 & EBI & - & 0.309 & 0.036 & 0.311\\
Molecular & & ASaiM & & - & 0.307 & 0.042\\
functions & SRR072233 & EBI & & & - & 0.305\\
 & & ASaiM & & & & -\\
\hline
\end{tabular}
\caption{Bray-Curtis dissimilarity scores on relative abundances of families and species for both samples (SRR072233 and SRR072233)}
\label{go_slim_distances}
\end{table}

For each category, compositions are highly more similar (dissimilarity scores close to 0) for both samples analyzed with same methods (*EBI metagenomics* or ASaiM) than for same sample analyzed with different methods. These composition differences betwee *EBI metagenomics* and ASaiM may come from different tools, different databases (InterPro for *EBI metagenomics*, UniRef50 for ASaiM framework) and their correspondance to GO slim terms. It is difficult to go beyond with basic comparisons and determine if a tool (*EBI metagenomics* or ASaiM) is better than the other one for functional results as no expected functional profile is available.

## Taxonomically-related functional results

In *HUMAnN2* results, abundances of gene families and pathways are stratified at the community level. We can then relate functional results to taxonomic results and answer questions such as "Which taxa contribute to which metabolic functions? And, in which proportion?". < 35\% of gene families (> 90\% of relative abundance) and > 80\% pathways (> 50\% of relative abundance) can be then related to the community structure (species and their abundance, Table \ref{taxo_rel_funct_results}).

\begin{table}[h!]
\centering
\begin{tabular}{m{7cm}rrrr}
\hline
 & \multicolumn{2}{c}{UniRef50 gene families} & \multicolumn{2}{c}{MetaCyc pathways}\\
 & SRR072232 & SRR072233 & SRR072232 & SRR072233 \\
\hline
Number & 26,219 & 41,005 & 402 & 400 \\
\% of associated to a species inside all & 26.60\% & 31.62\% & 82.56\% & 80\% \\
Relative abundance (\%) & 93.40\% & 90.24\% & 61.08\% & 51.52\%\\
Similar & \multicolumn{2}{c}{19,815} & \multicolumn{2}{c}{363} \\
\% of similar inside associated to a species  & 68.02\% & 48.32\% & 90.30\% & 90.75\% \\
Relative abundance of similar inside associated to a species (\%) & 89.17\% & 44.75\% & 91.87\% & 42.70\%\\
\hline
\end{tabular}
\caption{Global information about UniRef50 gene families and MetaCyc pathways related to species for both samples (SRR072233 and SRR072233). For each characteristics (gene families and pathways), several information is extracted: all number, number percentage and relative abundance (\%) of similar characteristics and \textit{p-value} of Wilcoxon test on relative abundance normalized by the sum of relative abundance for all similar characteristics.}
\label{taxo_rel_funct_results}
\end{table}

For both samples, a significant correlation is observed between CDS number in species (data from GenBank) and number of gene families found for these species (Table \ref{correlation_information}). The correlation, not so bad (*p-value* < 5.09 $\cdot 10^{-3}$), is yet not perfect ($r^{2}$ < 0.71). Indeed, gene families have not a direct mapping to CDS (paralogs, duplications, ...) and rely on exhaustivity of the reference database (UniRef) used by HUMAnN2. So, it may be interesting to investigate the relation between gene families corresponding to found species in UniRef and gene families found using HUMAnN2. This information is not available, but having a significant correlation between gene family number and CDS number is already great.

\begin{table}[h!]
\centering
\begin{tabular}{llrrrr}
\hline
 & & \multicolumn{2}{c}{UniRef50 gene families} & \multicolumn{2}{c}{MetaCyc pathways}\\
 & & SRR072232 & SRR072233 & SRR072232 & SRR072233 \\
\hline
\multicolumn{2}{c}{Number} & & & &\\
\cline{1-2}
Correlation with species CDS number & $r^{2}$ & 0.71 & 0.60 & & \\
& \textit{p-value} & 4.67 $\cdot 10^{-3}$ & 5.09 $\cdot 10^{-3}$ & & \\
\hline
\multicolumn{2}{c}{Mean abundance (Figure \ref{gene_family_pathway_mean})} & & & &\\
\cline{1-2}
Correlation with species abundance & $r^{2}$ & 0.95 & 0.98 & 0.90 & 0.93\\
 & \textit{p-value} & 1.51 $\cdot 10^{-7}$ & 2.9 $\cdot 10^{-13}$ & 1.91 $\cdot 10^{-7}$ & 5.88 $\cdot 10{-12}$ \\
\hline
\multicolumn{2}{c}{Difference of mean abundance} & & & &\\
\cline{1-2}
Correlation with species abundance difference & $r^{2}$ & \multicolumn{2}{c}{0.89} & \multicolumn{2}{c}{0.84}\\
 & \textit{p-value} & \multicolumn{2}{c}{4.12 $\cdot 10^{-7}$} & \multicolumn{2}{c}{4.65 $\cdot 10^{-6}$} \\
\hline
\end{tabular}
\caption{Correlation coefficients and p-values (Pearson's test) for UniRef50 gene families and MetaCyc pathways related to species for both samples (SRR072233 and SRR072233).
CDS number for each strain has been extracted from GenBank given the links in Table \ref{expected_species}}
\label{correlation_information}
\end{table}

For both samples, relative abundances of gene families and pathways are highly correlated to observed relative abundance of involved species (Table \ref{correlation_information}). Sequences of an abundant species in a community are supposed to be abundant in metagenomic sequences of the community. This relation holds for all sequences, particularly sequences corresponding to gene families. For pathways, the relation is more tricky: a pathway is identified if a high proportion of gene families involved in this pathway is found. And the abundance of a pathway is proportional to the number of complete "copies" of this pathway in the species. Then, a pathway is abundant if its parts are all found in numerous copies, leading to a tricky relation between species abundance and pathway abundance. But, the high correlations between species relative abundance and mean relative pathway abundance (Figure \ref{gene_family_pathway_mean}, Table \ref{correlation_information}) confirm good pathway reconstructions in our datasets, particularly for abundant species. To accentuate previous observations and conclusion, we also observe a strong and significant correlation between species abundance difference and difference of gene family and pathway mean abundance between both samples (Figure \ref{gene_family_pathway_mean}, Table \ref{correlation_information}).

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.43\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_asaim_results/functional_results/taxonomically_related_gene_families.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.43\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_asaim_results/functional_results/taxonomically_related_pathways.pdf}
    \end{minipage}
    \caption{Difference in mean abundances for gene families (left) and pathways (right) in function of difference of related species abundance between both samples. Correlation coefficients and p-values are detailed in Table \ref{correlation_information}}
    \label{gene_family_pathway_mean}
\end{figure}

Hence, our approach based on *MetaPhlAn2* and *HUMAnN2* results gives accurate and relevant taxonomically-related functional results.


# Conclusion

With ASaiM framework, raw sequences from a metagenomic dataset are quickly analyzed (in few hours in a commodity computer). Moreover, based on Galaxy, ASaiM framework posseses all Galaxy's strength: accessibility, reproducibility and also modularity. Numerous intermediary results can also be accessed during whole workflow execution, allowing deep investigation of taxonomic and functional analyses of microbial communities.

Taxonomic analysis using *MetaPhlAn2* gives a great insight on community structure with complete, accurate and statistically supported information. With *HUMAnN2* and extraction of GO slim terms, we get a broad overview of metabolic profile of studied microbial community. Furthermore, this metabolic profile is related to community structure to get information such as which species is involved in which metabolic function. This relation between function and taxonomy is really specific to ASaiM and not found in solutions like *EBI metagenomics*.

ASaiM framework based on Galaxy, numerous tools and workflows is a then powerful framework to analyze microbiota from shotgun raw sequence data.

# References
