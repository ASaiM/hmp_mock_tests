---
title: "Validation of ASaiM framework and its workflows on HMP mock community smaples and comparison with *EBI metagenomics* results"
subject_session: Sequence analysis
subtitle: "Supplementary material 2"
author: 
    - Bérénice Batut
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

ASaiM framework, particularly the main workflow, was tested and validated on two mock metagenomic datasets from a controlled microbiota community (with 22 known microbial strains). These datasets are available on *EBI metagenomics* dataset.

Taxonomic and functional results produced by ASaiM framework have been extensively analyzed and compared with results obtained with *EBI metagenomics* pipleine (https://www.ebi.ac.uk/metagenomics/pipelines/1.0) [@hunter_ebi_2014]. Details about these analyses (workflows, scripts) are available on a [dedicated GitHub repository](https://github.com/ASaiM/hmp_mock_tests) and the results on [Zenodo](https://zenodo.org/).

These analyses validate ASaiM framework and its main workflow. Hence, the main workflow produces accurate and precise taxonomic assignations, wide functional results (gene families, pathways, GO slim terms) and relations between taxonomic and functional results, in few hours on a standard computer. 

# Data

[Two HMP mock community samples](https://www.ebi.ac.uk/metagenomics/projects/SRP004311) are available on [EBI met](https://www.ebi.ac.uk/metagenomics/). Both of them contain a genomic mixture of same 22 microbial strains (Table \ref{expected_species}). The samples differ only by the abundances of the strains: in the first sample ([SRR072232](https://www.ebi.ac.uk/metagenomics/projects/SRP004311/samples/SRS121012/runs/SRR072232/results/versions/1.0)), the ribosomal RNA operon counts vary by up to four orders of magnitude per strains (Table \ref{expected_species}), wherease the second sample ([SRR072233](https://www.ebi.ac.uk/metagenomics/projects/SRP004311/samples/SRS121011/runs/SRR072233/results/versions/1.0)) contains equimolar ribosomal RNA operon counts per strain (Table \ref{expected_species}). 

Both samples were sequenced using 454 GS FLX Titanium to get 1,22,169 raw metagenomic sequences for the first dataset and 1,386,198 raw metagenomic sequences for the second dataset.

# Methods

Both datasets have been analyzed using ASaiM framework. The results extensively analyzed and compared to expected results and *EBI metagenomics* results. Details about these analyses (workflows, scripts) are available on a [dedicated GitHub repository](https://github.com/ASaiM/hmp_mock_tests) and the results on [Zenodo](https://zenodo.org/).

## Abundance computation using mapping on reference genomes

The expected abundances based on ribosomal RNA operon counts. During biological manipulations and sequencing, some bias may arise that modify the abundances of strains. Indeed, to get "real" abundances of expected strains, raw metagenomic sequences of both samples are mapped on genomes of expected strains using BWA [@li_fast_2009;@li_fast_2010].

\newpage
\thispagestyle{empty}
\newgeometry{top=2cm, bottom=2cm, left=2cm, right=2cm}
\begin{landscape}
\begin{table}
\begin{tabular}{llm{2.5cm}llllm{2.5cm}m{2.5cm}|rr}
\hline
\multicolumn{9}{c|}{Taxonomy} & \multicolumn{2}{c}{Abundances}\\
Domain & Kingdom & Phylum & Class & Order & Family & Genus & Species & Strains & SRR072232 & SRR072233 \\
\hline
Archaea & Archaea & Euryarchaeota & Methanobacteria & Methanobacteriales& Methanobacteriaceae & \textit{Methanobrevibacter} & \textit{Methanobrevibacter smithii} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000016525.1_ASM1652v1/}{ATCC 35061} & 1,000,000 & 100,000 \\
\hline
Bacteria & Bacteria & Actinobacteria & Actinobacteria & Actinomycetales & Actinomycetaceae & \textit{Actinomyces} & \textit{Actinomyces odontolyticus} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000154225.1_ASM15422v1/}{ATCC 17982} & 1,000 & 100,000 \\
\cline{6-11}
 &  &  &  &  & Propionibacteriaceae & \textit{Propionibacterium} & \textit{Propionibacterium acnes} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000008345.1_ASM834v1/}{DSM 16379} & 10,000 & 100,000 \\
\cline{3-11}
 & & Bacteroidetes & Bacteroidia & Bacteroidales & Bacteroidaceae & \textit{Bacteroides} & \textit{Bacteroides vulgatus} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000012825.1_ASM1282v1/}{ATCC 8482} & 1,000 & 100,000 \\
\cline{3-11}
& & Deinococcus-Thermus & Deinococci & Deinococcales & Deinococcaceae & \textit{Deinococcus} & \textit{Deinococcus radiodurans} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000008565.1_ASM856v1/}{DSM 20539} & 1,000 & 100,000 \\
\cline{3-11}
& & Firmicutes & Bacilli & Bacillales & Bacillaceae & \textit{Bacillus} & \textit{Bacillus cereus thuringiensis} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000008005.1_ASM800v1/}{ATCC 10987} & 100,000 & 100,000\\
\cline{6-11}
& & & & & Listeriaceae & \textit{Listeria} & \textit{Listeria monocytogenes} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000196035.1_ASM19603v1/}{ATCC BAA-679} & 10,000 & 100,000 \\
\cline{6-11}
& & & & & Staphylococcaceae & \textit{Staphylococcus} & \textit{Staphylococcus aureus} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000153665.1_ASM15366v1/}{ATCC BAA-1718} & 100,000 & 100,000 \\
\cline{8-11}
& & & & & & & \textit{Staphylococcus epidermidis} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000007645.1_ASM764v1/}{ATCC 12228} & 1,000,000 & 100,000 \\
\cline{5-11}
& & & & Lactobacillales & Enterococcaceae & \textit{Enterococcus} & \textit{Enterococcus faecalis} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000172575.2_ASM17257v2/}{ATCC 47077} & 1,000 & 100,000\\
\cline{6-11}
& & & & & Lactobacillaceae & \textit{Lactobacillus} & \textit{Lactobacillus gasseri} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000014425.1_ASM1442v1/}{DSM 20243} & 10,000 & 100,000\\
\cline{6-11}
& & & & & Streptococcaceae & \textit{Streptococcus} & \textit{Streptococcus agalactiae} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000007265.1_ASM726v1/}{ATCC BAA-611} & 100,000 & 100,000\\
\cline{8-11}
& & & & & & & \textit{Streptococcus mutans} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000007465.2_ASM746v2/}{ATCC 700610} & 1,000,000 & 100,000\\
\cline{8-11}
& & & & & & & \textit{Streptococcus mitis oralis pneumoniae} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000006885.1_ASM688v1/}{ATCC BAA-334} & 1,000 & 100,000\\
\cline{4-11}
& & & Clostridia & Clostridiales & Clostridiaceae & \textit{Clostridium} & \textit{Clostridium beijerinckii} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000016965.1_ASM1696v1/}{ATCC 51743} & 100,000 & 100,000\\
\cline{3-11}
& & Proteobacteria & Alphaproteobacteria & Rhodobacterales & Rhodobacteraceae & \textit{Rhodobacter} & \textit{Rhodobacter sphaeroides} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000012905.2_ASM1290v2/}{ATCC 17023} & 1,000,000 & 100,000\\
\cline{4-11}
& & & Betaproteobacteria & Neisseriales & Neisseriaceae & \textit{Neisseria} & \textit{Neisseria meningitidis} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000008805.1_ASM880v1/}{ATCC BAA-335} & 10,000 & 100,000\\
\cline{4-11}
& & & Epsilonproteobacteria & Campylobacterales & Helicobacteraceae & \textit{Helicobacter} & \textit{Helicobacter pylori} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000008525.1_ASM852v1/}{ATCC 700392} & 10,000 & 100,000\\
\cline{4-11}
& & & Gammaproteobacteria & Pseudomonadales & Moraxellaceae & \textit{Acinetobacter} & \textit{Acinetobacter baumannii} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000015425.1_ASM1542v1/}{ATCC 17978} & 10,000 & 100,000\\
\cline{6-11}
& & & & & Pseudomonadaceae & \textit{Pseudomonas} & \textit{Pseudomonas aeruginosa} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000006765.1_ASM676v1/}{ATCC 47085} & 100,000 & 100,000\\
\cline{5-11}
& & & & Enterobacteriales & Enterobacteriaceae & \textit{Escherichia} & \textit{Escherichia coli} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000005845.2_ASM584v2/}{ATCC 70096} & 1,000,000 & 100,000\\
\hline
Eukaryotes & Fungi & Ascomycota & Saccharomycetes & Saccharomycetales & Debaryomycetaceae & \textit{Candida} & \textit{Candida albicans} & \href{ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF_000182965.2_ASM18296v2/}{SC5314} & 1,000 & 100,000 \\
\hline
& & & & & & & & \textbf{Total} & 5,566,000 & 2,200,000\\
\cline{9-11}
\end{tabular}
\caption{Expected strains, their taxonomy and their ribosomal RNA operon counts (abundance, from metadata on EBI metagenomics database) on both samples (SRR072232 and SRR072233)}
\label{expected_species}
\end{table} 
\end{landscape}
\newpage
\restoregeometry

## Analyses using *EBI Metagenomics*

Both datasets have been analysed with [*EBI metagenomics* pipeline (Version 1.0)](https://www.ebi.ac.uk/metagenomics/pipelines/1.0) (Figure \ref{ebi_pipeline}). We downloaded the results and formatted them to help comparison with ASaiM results.

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/ebi_workflow.pdf}
    \caption{\textit{EBI metagenomics} pipeline (version 1.0).
    The grey boxes correspond to data, the blue boxes to pretreatment steps, the red boxes to functional analysis steps and the green boxes to taxonomic analysis steps.}
    \label{ebi_pipeline}
\end{figure}

First, from OTUs with taxonomic assignation, abundances of each assigned clade are extracted. Several relative abundance measures are computed: relative abundances of clades for all OTUs and relative abundances of clades for OTUs with complete taxonomic assignation from kingdom to family. Percentage of unassigned clades (without complete taxonomic assignation) is also computed for each taxonomic level.

For functional analysis, *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}) offers 3 types of results: matches with InterPro, complete GO annotations and GO slim annotations. Here, we focus on GO slim annotations for easy comparison with ASaiM results (Figure \ref{asaim_workflow}). Annotations are formatted to extract relative abundances (in percentage) of GO slim term annotations inside each GO slim term group (cellular components, biological processes and molecular functions).

## Analyses using ASaiM framework

Main workflow (Figure \ref{asaim_workflow}) of ASaiM framework is used to analyze both datasets

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/asaim_workflow.pdf}
    \caption{ASaiM workflow for analysis of raw single-end microbiota sequences. This workflow is available with ASaiM Galaxy instance and used to analyze both datasets. The grey boxes correspond to data, the blue boxes to pretreatment steps, the red boxes to functional analysis steps and the green boxes to taxonomic analysis steps.}
    \label{asaim_workflow}
\end{figure}

For these analyses, ASaiM framework is deployed on a computer with Debian GNU/Linux System, 8 cores Intel(R) Xeon(R) at 2.40GHz and 32 Go of RAM. During workflow execution, we follow size of used memory and execution time (Table \ref{computation_stats}). Indeed, workflow execution is relatively fast: < 5h and < 5h30 for datasets with 1,225,169 and 1,386,198 sequences respectively (Table \ref{computation_stats}). The main time consuming step is the functional assignation with *HUMAnN2* [@abubucker_metabolic_2012] which last $\simeq$ 64% of overall time execution (Table \ref{computation_stats}). And, the size of the process in memory is stable over workflow execution (variability inferior to 40 kb) (Table \ref{computation_stats}).

\begin{table}[h!]
\centering
\begin{tabular}{llrr}
\hline
\multicolumn{2}{l}{Statistics} & SRR072232 & SRR072233 \\
\hline
Execution time & Whole workflow & 4h44 & 5h22 \\
& PRINSEQ & 0h38 & 0h44\\
& Vsearch & 16s & 19s\\
& SortMeRNA & 0h55 & 0h58\\
& MetaPhlAN2 & 0h09 & 0h10\\
& HUMAnN2 & 3h01 & 3h26\\
Size of the process in memory (kb) & Min & 1,515,732 & 1,515,732\\
 & Mean & 1,515,744 & 1,515,743\\
 & Max & 1,515,768 & 1,515,764\\
\hline
\end{tabular}
\caption{Computation statistics on ASaiM for both samples (SRR072233 and SRR072233)}
\label{computation_stats}
\end{table}

After workflow execution, taxonomic results are formatted to extract the percentage of unassigned clades at different taxonomic levels (clades without more accurate taxonomic assignation). 

No further formatting step is needed for functional results (relative abundance of gene families, pathways with and without species relation and GO slim terms) of one sample. To compare functional results (gene families and pathways) between both samples (SRR072232 and SRR072233), a workflow is developed and executed (Figure \ref{asaim_humann2_comparison_results}).

\begin{figure}[h!]
    \centering
    \includegraphics[width = .7\linewidth]{../images/asaim_humann2_comparison_results.pdf}
    \caption{Workflow to compare ASaiM functional results (gene families or pathways) between both samples. This workflow is available with ASaiM Galaxy instance. The grey boxes correspond to data, the blue boxes to processing steps.}
    \label{asaim_humann2_comparison_results}
\end{figure}

## Comparison of *EBI metagenomics* results and ASaiM results

*EBI metagenomics* results and ASaiM ones are not directly comparable. Several processing steps are then needed.

With *MetaPhlAn* in ASaiM workflow, relative abundance of clades is computed on assigned reads. No count is made of non assigned reads. To compare relative abundances between both pipelines, we focus on relative abundances computed on OTUS or reads with a complete taxonomic assignation from kingdom to family. These results are also compared to expected relative abundances obtained from sample descriptions (Table \ref{expected_species}). 

In both *EBI metagenomics* and ASaiM workflows (Figures \ref{ebi_pipeline} and \ref{asaim_workflow}), functional matches are grouped into GO slims terms. These terms are a subset of the terms in the whole Gene Ontology with a focus on microbial metabolic functions. They give a broad overview of the ontology content. To compare *EBI metagenomics* and ASaiM results, relative abundance of GO slim terms for both samples and both workflows are concatenated and compared, given the workflow depicted in Figure \ref{go_slim_comparison_workflow}. 

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/go_slim_comparison_workflow.pdf}
    \caption{Workflow to compare GO slim annotation abundances between samples (SRR072232, SRR072233) and workflows (\textit{EBI metagenomics}, ASaiM). This workflow is available with ASaiM Galaxy instance. The grey boxes correspond to data, the blue boxes to processing steps.}
    \label{go_slim_comparison_workflow}
\end{figure}

# Results

## Results of pretreatments in pipelines

In both workflows (Figures \ref{ebi_pipeline} and \ref{asaim_workflow}), raw sequences are pre-processed before any taxonomic or functional analysis. These preprocessing steps include quality control to remove low quality, small or duplicated sequences and also rRNA sorting to sort rRNA/rDNA sequences from non rRNA sequences (Figures \ref{ebi_pipeline} and \ref{asaim_workflow}). The used tools and parameters for these pretreatments are different between *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}) and ASaiM workflow (Figure \ref{asaim_workflow}). So, even with similar raw input sequences, pretreatment outputs are different (Table \ref{pretreatment_stats}).

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

The first interesting point in pretreatment results is the difference in sequence number after quality control and dereplication (Table \ref{pretreatment_stats}). With ASaiM, more sequences (> 96 \%) are conserved during these first steps of quality control and dereplication than with *EBI metagenomics* (< 87 \%, Table \ref{pretreatment_stats}). This difference may be explained by threshold differences for minimum length. In *EBI metagenomics* pipeline, sequences with less than 100 nucleotides are removed (Figure \ref{ebi_pipeline}), while in ASaiM the threshold is fixed to 60 nucleotides (Figure \ref{asaim_workflow}). However, this threshold difference does not explain all the observed difference in sequence number after quality control and dereplication. Indeed, when in ASaiM quality control with PRINSEQ [@schmieder_quality_2011] is run with exactly same parameters but filtering of sequences with less than 100 nucleotides, 1,135,008 (92.6%) and 1,304,023 (94.1%) sequences are conserved for SRR072232 and SRR072233 respectively after quality control and dereplication. These proportion are still higher than the one observed with *EBI metagenomics* pipeline (Table \ref{pretreatment_stats}). Smaller length threshold with ASaiM does not then explain all difference in sequence number after quality control and dereplication. The differences come from then from the used tools and their underlying algorithms and implementations.

In both datasets and with both workflows, few rDNA sequences are found in datasets (Table \ref{pretreatment_stats}). Indeed, these datasets are metagenomic datasets and then focus on gene sequences. Few copies of rRNA genes are found in organisms (bacteria, archeae or eukaryotes) and are then expected in metagenomic sequences. Despite small number of sequences, a difference of rRNA sequence number is observed between *EBI metagonomics* and ASaiM workflows (Table \ref{pretreatment_stats}). Higher proportions of rDNA sequences are systematically found with ASaiM workflow. Indeed, in *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}), *rRNASelector* [@lee_rrnaselector:_2011] is used to select rDNA  bacterial and archaeal sequences (no eukaryotes sequences). In ASaiM workflow (Figure \ref{asaim_workflow}), rRNA sequences are sorted using *SortMeRNA* [@kopylova_sortmerna:_2012] and 8 databases for bacteria, archaea and also eukaryotes rRNA. < 5% of all sequences are matched against databases dedicated to eukaryotes rRNA sequences, and then does not explain all differences of rRNA sequence proportions between *EBI metagenomics* and ASaiM. This difference may be due to completness of the databases: databases used by *rRNASelector* [@lee_rrnaselector:_2011] are older and probably less complete than databases used by *SortMeRNA* [@kopylova_sortmerna:_2012].

After pretreatments, more sequences are then conserved for taxonomic and functional analyses in ASaiM workflow than in *EBI metagenomics* pipeline, for both samples (Table \ref{pretreatment_stats}).

## Taxonomic analyses

### Abundances of expected strains and taxonomy

The expected abundances based on ribosomal RNA operon counts. During biological manipulations and sequencing, some bias may arise that modify the abundances of strains. Indeed, to get "real" abundances of expected strains, raw metagenomic sequences of both samples are mapped on genomes of expected strains. 

For SRR02232, variations in abundances between species are similar using mapping than RNA operon count (Figure \ref{mapping_comparison}). Observations are different for SRR072233 (Figure \ref{mapping_comparison}): expected abundances (based on RNA operon abundances) are identical for all species, but unexpected variations exist for mapping based abundances. 

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/mapping_expectation_barplot.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072233/mapping_expectation_barplot.pdf}
    \end{minipage} 
    \caption{Comparison of relative abundances between expectation given the ribosomal RNA operon counts (green, Table \ref{expected_species}) and mapping against reference genomes for both samples (SRR072232 on left, SRR072233 on right)}
    \label{mapping_comparison}
\end{figure}

These differences between expected abundances (from RNA operon counts) and mapping-based abundances may be due to bias induced during biological manipulations or sequencing. As next taxonomic analyses are based on raw metagenomic sequences, abundances based on mapping counts are used on further analyses instead of abundances based on ribosomal RNA operon counts from metadata (Figure \ref{expected_taxonomy}).

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/expected_taxonomy.pdf}
    \caption{Expected taxonomy for SRR072232 (left) and SRR072233 (right) from domains to species. Circle diameters at each taxonomic levels are proportional to mapping-based relative abundance of corresponding taxon.}
    \label{expected_taxonomy}
\end{figure}


### Raw ASaiM results

In ASaiM workflow (Figure \ref{asaim_workflow}), taxonomic analysis is made using *MetaPhlAN* (2.0) [@truong_metaphlan2_2015;@segata_metagenomic_2012] on sequences after pretreatments. *MetaPhlAn* profiles the microbial community structure using a database of unique clade-specific marker genes identified from 17,000 reference genomes. This step of taxonomic assignation with *MetaPhlAn* is fast in ASaiM Galaxy instance (less than 10 minutes for > 1,100,000 sequences, Tables \ref{computation_stats} and \ref{pretreatment_stats}). 

Raw *MetaPhlAn* results consist in a plain text file with relative abundance of clades at different taxonomic levels. Visualisation tools help to represent *MetaPhlAn* results. In ASaiM, two such tools are used: *Krona* [@ondov_interactive_2011] for interactive representations of taxonomic assignation and *GraPhlan* for static representations. These static representations are modified (legend *e.g.* colors, numbers for families) to help comparison with expected taxonomy (Figure \ref{asaim_taxonomy}).

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/asaim_taxonomy.pdf}
    \caption{Taxonomy for SRR072232 (left) and SRR072233 (right) from domains to species, found with ASaiM framework. Circle diameters at each taxonomic levels are proportional to mapping-based relative abundance of corresponding taxon. Colors and family numbers are the same as the ones used in Figure \ref{expected_taxonomy}. Gray circles and lines represent unexpected lineages.}
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

Despite same expected species, taxonomic diversity in SRR072232 dataset is reduced compared to the one in SRR072233 dataset (Figure \ref{asaim_taxonomy}). Less taxons are found for each taxonomic levels. From 22 expected species (Table \ref{expected_species}), 17 are found for SRR072232 and 20 for SRR072233 (Figure \ref{species_abundances}). The 2 expected species (*Candidata albicans* and *Lactobacillus gasseri*) missing in SRR072233 dataset are also missing in SRR072232 dataset (Figure \ref{species_abundances}). This may be due to a lack of phylogenetic markers for these species in the database used in *MetaPhlAn*. On the other hand, few sequences of these species in SRR072233 are found using mapping on expected species genomes. The signal may be too low to detect the species. Indeed, all species with mapping-based abundance smaller than 0.1\% are not found using ASaiM for both datasets  (Figure \ref{species_abundances}).

For SRR072232 datasets, two species with mapping-based abundance higher than 0.1\% are not found: *Candida albicans* and *Bacillus cereus thuringiensis*. The first species is not found also with ASaiM in SRR072333, phylogenetic markers for this species may be lacking in *MetaPhlAn2* database. As the second species is found with ASaiM in SRR072333, same explanation based on lack on corresponding phylogenetic markers does not hold. 

### Comparison with EBI results and expected taxonomy

After these first comparisons between ASaiM results taxonomic and expected ones, we compare ASaiM taxonomic results and *EBI metagenomics* taxonomic results.

In *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}), *QIIME* [@caporaso_qiime_2010] is used on 16S sequences to identify OTUs and taxonomic assignation for these OTUs. In ASaiM (Figure \ref{asaim_workflow}), *MetaPhlAn* [@truong_metaphlan2_2015;@segata_metagenomic_2012] is computed on sequences after quality control and dereplication, without any sorting step. *MetaPhlAn* [@truong_metaphlan2_2015;@segata_metagenomic_2012] searches diverse phylogenetic markers, and not only 16S ones as *QIIME* [@caporaso_qiime_2010] does, on all sequence types (rRNA, non rRNA, ...). Inside so different sequences, the proportion of sequences with phylogenetic markers is smaller. Indeed, with *MetaPhlAn* [@truong_metaphlan2_2015;@segata_metagenomic_2012], the percentage of unassigned reads is $\simeq$ 9 times higher than with *QIIME* [@caporaso_qiime_2010] (SRR072232: 6.4\% with *EBI metagenomics* against 62.61\% with ASaiM; SRR072233: 13\% with *EBI metagenomics* against 53.93\% with ASaiM). Nevertheless, taxonomic lineages from *EBI metagenomics* are limited to family level (Figure \ref{ebi_taxonomy}), while they go to species level with ASaiM (Figure \ref{asaim_taxonomy}). Hence, with *MetaPhlAn* [@truong_metaphlan2_2015;@segata_metagenomic_2012], the taxonomic assignations are more accurate, complete (until species level) and statistically supported (based on more sequences).

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/ebi_taxonomy.pdf}
    \caption{Taxonomy for SRR072232 (left) and SRR072233 (right) from domains to families, found with EBI metagenomics pipeline. Circle diameters at each taxonomic levels are proportional to mapping-based relative abundance of corresponding taxon. Colors and family numbers are the same as the ones used in Figure \ref{expected_taxonomy}. Gray circles and lines represent unexpected lineages.}
    \label{ebi_taxonomy}
\end{figure}

With both *EBI metagenomics* and ASaiM, some observed taxonomic assignations are unexpected (Tables \ref{asaim_unexpected_species} and \ref{ebi_unexpected_clades}, Figures \ref{asaim_taxonomy} and \ref{ebi_taxonomy}). For ASaiM, 3 species in each sample are identified as "unclassified" (Table \ref{asaim_unexpected_species}). They are affiliated to the correct genus but not to the species. These unclassified sequences may be due to incomplete annotations in reference database, because expected species are known and observed. These expected species are observed in lower abundance than expected (Figure \ref{species_abundances}) and would be closer to expected abundances with correct annotation of unclassified species. Similarly, some observed clades and their sub-clades are unexpected in *EBI metagenomics* taxonomic results (Table \ref{ebi_unexpected_clades}). The taxonomic levels of these unexpected clades are higher (class, order and family) than unexpected taxonomic level in ASaiM (species, Table \ref{unexpected_clades}, Figure \ref{ebi_taxonomy}). Taxonomic assignations with *MetaPhlAN* [@truong_metaphlan2_2015;@segata_metagenomic_2012] are then more accurate and precise.

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

Taxonomic results obtained with *EBI metagenomics* pipeline are less precise than the one obtained with ASaiM workflow. Indeed, the most precise taxonomic level is family for *EBI metagenomics* (Figure \ref{ebi_taxonomy}) and species for ASaiM (Figure \ref{asaim_taxonomy}). Comparison of taxonomic results focus then on family level (Figure \ref{family_abundances}).

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/concatenated_family_abundances.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072233/concatenated_family_abundances.pdf}
    \end{minipage} 
    \caption{Relative abundances of expected families for SRR072232 (left) and SRR072233 (right) with comparison between expected abundances (red thin bars), abundances obtained with \textit{EBI metagenomics} (green wide bars) and abundances obtained with ASaiM (blue wide bars) and }
    \label{family_abundances}
\end{figure}

Similarly, to previous observations on raw ASaiM results, species with mapping-based abundance smaller than 0.1\% are not found either with ASaiM or with *EBI metagenomics* (Figure \ref{family_abundances}). Nonetheless, the detection threshold seems slightly smaller for *EBI metagenomics*: for SRR072232, Listeriaceae family is detected with *EBI metagenomics* and not with ASaiM (Figure \ref{family_abundances}). On the other hand, Bacillaceae and Debaryomycetaceae families are not found with *EBI metagenomics* for both datasets (Figure \ref{family_abundances}), despite mapping-based abundance higher than 0.1\%. Used databases may be then incomplete regarding some phylogenetic markers, particularly the ones for missing families. 

Except missing species, variations in observed abundances for *EBI metagenomics* or ASaiM correspond to variations in mapping-based abundances (Figure \ref{species_abundances}): small observed abundances for small mapping-based abundances and high observed abundances for high mapping-based abundances. 

For a broader comparison, a principal component analysis (PCA) is runned, for each sample, on observed families (for which abundance is not null in *EBI metagenomics* or ASaiM results). First axis of these analyses explains most of data variability (98\% for both datasets, Figure \ref{family_pca}). Mapping-based, *EBI metagenomics* and ASaiM abundances are not discriminated on this first axis (Figure \ref{family_pca}), only on the second one which explains less than 2\% of overall data variability. Differences between mapping-based, *EBI metagenomics* and ASaiM abundances are then reduced. Hence, similar abundances for observed families are then obtained for *EBI metagenomics* and ASaiM and these abundances are close to abundances computed using mapping to expected species.

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.43\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072232/concatenated_family_abundance_pca.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.43\linewidth}
    \includegraphics[width = \linewidth]{../images/SRR072233/concatenated_family_abundance_pca.pdf}
    \end{minipage} 
    \caption{Scatter diagram of principal component analysis of the relative abundances (in percentage) of families for SRR072232 (in left) and SRR072233 (in right). Only observed families in EBI metagenomics or ASaiM are used in these analyses.}
    \label{family_pca}
\end{figure}

ASaiM framework gives taxonomic results which are more accurate, complete (until species level) and statistically supported (based on more sequences) than *EBI metagenomics*. Moreover, community structure found with ASaiM framework is close to expected community structure of these mock datasets.

## Functional analyses

### Raw ASaiM results

In ASaiM framework (Figure \ref{asaim_workflow}), [*HUMAnN*2](http://huttenhower.sph.harvard.edu/humann2) [@abubucker_metabolic_2012] is used for functional analyses. This tool profiles presence/absence and abundance of UniRef50 gene families and MetaCyc pathways from metagenomic/metatranscriptomic datasets. It then describes the metabolic profil of a microbial community. 

*HUMAnN*2 generates three outputs: abundances of UniRef50 gene families, coverage and abundance of MetaCyc pathways. In both samples, > 90,000 UniRef50 gene families and > 480 MetaCyc pathways (Table \ref{humann2_informations}) are reconstructed from > 1,100,000 non rDNA sequences (Table \ref{pretreatment_stats}).

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
\end{tabular}
\caption{Global information about UniRef50 gene families and MetaCyc pathways obtained with \textit{HUMAnN2} for both samples (SRR072233 and SRR072233). For each characteristics (gene families and pathways), several information is extracted: all number, number percentage and relative abundance (\%) of similar characteristics and \textit{p-value} of Wilcoxon test on relative abundance normalized by the sum of relative abundance for all similar characteristics.}
\label{humann2_informations}
\end{table}

Datasets are constitued of metagenomic sequences from genomic mixture of identical 22 microbioal strains (Table \ref{expected_species}). Differences between datasets are on abundance of these strains. Similar metabolic functions made by same species are then supposed to be found in both datasets, but with different abundances.

However, differences of metabolic functions between both datasets are observed. Sets of gene families are different: 44,933 gene families are found in both samples (<46\% for both samples, Table \ref{humann2_informations}). However, different gene families have a limited impaxt on overall metabolism (< 50\% of relative abundance, Table \ref{humann2_informations}). Global metabolism functions such as pathways are similar in both datasets (> 95\% of similar pathways representing > 99.5\% of overall abundance, Table \ref{humann2_informations}). Hence, the unexpected observed differences are limited and may be due to bias induced by biological manipulations or sequencing. 

On the other hand, abundances of similar metabolic functions are different (Figure \ref{similar_characteristics_abundances}), as expected.


\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_asaim_results/functional_results/raw_gene_families.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.49\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_asaim_results/functional_results/raw_pathways.pdf}
    \end{minipage} 
    \caption{Normalized relative abundances (\%) for similar UniRef50 gene families (left graphics) and MetaCyc pathways (right graphics) for both samples (SRR072233 and SRR072233). The relative abundances of each similar characteristics (gene families or pathways) is computed with \textit{HUMAnN2} and normalized by the sum of relative abundance for all similar characteristics.}
    \label{similar_characteristics_abundances}
\end{figure}

With more than 90,000 gene families and almost 500 pathways, the metabolic profile of studied microbial community is too large to get a broad overview. Each gene family and pathway is precise and related to specific metabolic functions. This information is interesting when you need detailed metabolic information and to go deeply inside metabolic profil. However, to get a broad overview of the metabolic processes, UniRef50 gene families and even MetaCyc pathways are too numerous and too precise. UniRef50 gene families and their abundances are then grouped into slim Gene Ontology terms (Figure \ref{SRR072232_go_abundances}). Inside the 3 groups, the GO slim terms have similar abundances in both samples (Figure \ref{go_abundances}).

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

Both communities, with same expected strains but with different abundances of these species, are similarly doing metabolic tasks. Hence, functional results obtained with ASaiM fill the expectations.

### Comparison of *EBI metagenomics* and ASaiM results

In *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}), functional analyses are based on InterPro and its identifiants. In ASaiM workflow (Figure \ref{asaim_workflow}), we have access to UniRef50 gene families and their abundances computed with *HUMAnN2*. These functional results are then not directly comparable. But, in both workflows, UniRef50 gene families and InterPro proteins are grouped into Gene Ontology slim terms to get a broad overview of functional profile of the community. These GO slim terms are grouped into 3 groups: cellular components, biological processes and molecular functions.

Few GO slim terms are different for *EBI metagenomics* and ASaiM (Table \ref{incomplete_go_slims}). They are negligible in term of relative abundance inside the three groups.

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

Barplot representations of GO slim term abundances for both samples and both workflows can be difficult to interpret (*e.g.* for the cellular component on Figure \ref{cellular_components}). We used then a principal component analysis (PCA) on normalized relative abundance of GO slim term abundance inside each group to simplify visualization and interpretation (Figures \ref{cellular_components} and \ref{biological_process}).

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.55\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_go_slim_terms/cellular_component_barplot.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.43\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_go_slim_terms/cellular_component_pca.pdf}
    \end{minipage} 
    \caption{Barplot representation (in left, logarithm scale) and scatter diagram of principal component analysis of the normalized relative abundances (in percentage) of the cellular component GO slim terms for both samples (SRR072233 and SRR072233) and both workflows (\textit{EBI metagenomics} and ASaiM). The relative abundances of each GO slim terms is normalized by the sum of relative abundance for the found cellular component GO slim terms in both samples and with both workflows.}
    \label{cellular_components}
\end{figure}

\begin{figure}[h!]
    \centering
    \begin{minipage}[c]{.43\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_go_slim_terms/biological_process_pca.pdf}
    \end{minipage} \hfill
    \begin{minipage}[c]{.43\linewidth}
    \includegraphics[width = \linewidth]{../images/concatenated_go_slim_terms/molecular_function_pca.pdf}
    \end{minipage} 
    \caption{Scatter diagram of principal component analysis of the normalized relative abundances (in percentage) of the biological process (in left) and of the molecular functions (in right) GO slim terms for both samples (SRR072233 and SRR072233) and both workflows (\textit{EBI metagenomics} and ASaiM). The relative abundances of each GO slim terms is normalized by the sum of relative abundance for the found biological process GO slim terms in both samples and with both workflows.}
    \label{biological_process}
\end{figure}

Scatter representation of first plan (first two axes) of the PCA is similar for the three groups (Figures \ref{cellular_components} and \ref{biological_process}). First axis explains most data variability (between 64\% and 87\%, Table \ref{pca_info}). GO slim terms found on left part of scatter representation (Figures \ref{cellular_components} and \ref{biological_process}) are highly abundant: cellular processes related to membrane and cytoplasm (Figure \ref{cellular_components}), biosynthetic processes, nitrogen compound metabolic process, small molecular metabolic process, transport and DNA metabolic process for biological processes (Figure \ref{biological_process}) and nucleotide binding for molecular functions (Figure \ref{biological_process}). This first axis does not discrimate samples or workflows (Figures \ref{cellular_components} and \ref{biological_process}). Results from ASaiM workflow are then similar in term of GO slim term abundances to the one obtained with *EBI metagenomics* pipeline.

\begin{table}[h!]
\centering
\begin{tabular}{lrrr}
\hline
 & Cellular components & Biological processes & Molecular functions\\
\hline
First axis & 64\% & 87 \% & 85\%\\
\hline
Second axis & 35\% & 13 \% & 15\%\\
\hline
\end{tabular}
\caption{Explained variability by axes of Principal component analysis (PCA) for GO slim terms of cellular components, biological processes and molecular functions}
\label{pca_info}
\end{table}

The discrimination between *EBI metagenomics* and ASaiM results appears with second axis (Table \ref{pca_info}), explaining between 13\% and 35\% of overall data variability (Table \ref{pca_info}). Some GO slim terms such as membrane, hydrolase activity or nitrogen compound metabolic process are found in higher proportion in *EBI metagenomics* results than in ASaiM and some like biosynthetic process, plasma membrane or nucleotide binding in lower proportion (Figures \ref{cellular_components} and \ref{biological_process}).

None of the first two axes discriminates between samples. Variability between both samples seems then less important than variability between both workflows and mostly variability between GO slim terms.

*EBI metagenomics* and ASaiM functional results are similar in terms of GO slim terms abundance: the discrimination between both workflow results appears as a secondary explanation for variability in GO slim term abundances.

## Taxonomically-related functional results

In *HUMAnN2* results, abundances of gene families and pathways are stratified at the community level. We can then relate functional results to taxonomic result and answer questions such as "Which species contribute to which metabolic functions? In which proportion?". < 35\% of gene families (> 90\% of relative abundance) and > 80\% pathways (> 50\% of relative abundance) can be related to the community structure (species and their abundance, Table \ref{taxo_rel_funct_results}). 

\begin{table}[h!]
\centering
\begin{tabular}{m{3cm}m{5cm}rrrr}
\hline
 & & \multicolumn{2}{c}{UniRef50 gene families} & \multicolumn{2}{c}{MetaCyc pathways}\\
 & & SRR072232 & SRR072233 & SRR072232 & SRR072233 \\
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
\label{taxo_rel_funct_results}
\end{table}

For both samples, we observed a significant correlation between CDS number in species (data from GenBank) and number of gene families found for these species (Table \ref{correlation_information}). The correlation, not so bad, is yet not perfect. Indeed, gene families have not a direct mapping to CDS (paralogs, duplications, ...) and rely on exhaustivity of the reference database (UniRef) used by HUMAnN2. So, it may be interesting to investigate the relation between gene families corresponding to found species in UniRef and gene families found using HUMAnN2. This information is not available, but having a significant correlation between gene family number and CDS number is already a great point.

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
\caption{Correlation coefficients and p-values (Pearson's test) for UniRef50 gene families and MetaCyc pathways obtained with \textit{HUMAnN2} for both samples (SRR072233 and SRR072233).
CDS number for each strain has been extracted from GenBank given the links in Table \ref{expected_species}}
\label{correlation_information}
\end{table}

For both samples, relative abundances of gene families and pathways are highly correlated to observed relative abundance of involved species (Figure \ref{gene_family_pathway_mean} and Table \ref{correlation_information}). Sequences of an abundant species in a community are supposed to be abundant in metagenomic sequences of the community. This relation concerns all sequences, particularly sequences corresponding to gene families. For pathways, the relation is more tricky: a pathway is identified if a high proportion of gene families involved in this pathway is found. And the abundance of a pathway is proportional to the number of complete "copies" of this pathway in the species. Then, a pathway is abundant if its parts are all found in numerous copies, leading to a tricky relation between species abundance and pathway abundance. But, the high correlations between species relative abundance and mean relative pathway abundance (Figure \ref{gene_family_pathway_mean}, Table \ref{correlation_information}) confirm good pathway reconstructions in our datasets, particularly for abundant species. To accentuate previous observations and conclusion, we also observe a strong and significant correlation between species abundance difference and difference of gene family and pathway mean abundance between both samples (Table \ref{correlation_information}). 

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

Hence, our approach based on MetaPhlAn2 and HUMAnN2 gives accurate and relevant taxonomically-related functional results.


# Conclusion

With ASaiM framework, raw sequences from a metagenomic dataset are fast analyzed (in few hours in a standard computer). Moreover, based on Galaxy, ASaiM framework posseses all Galaxy's strength: accessibility, reproducibility and also modularity. Numerous intermediary results can also be accessed during whole workflow execution.

Taxonomic analysis using *MetaPhlAn2* gives a great insight on community structure wtih complete, accurate and statistically supported information. With *HUMAnN2* results and post-treatments on functional results, we get a broad overview of metabolic profile of studied microbial community. Furthermore, this metabolic profile is related to community structure to get information such as which species is involved in which metabolic function. This relation between function and taxonomy is really specific to ASaiM and not found in solutions like *EBI metagenomics*.

ASaiM framework based on Galaxy, numerous tools and workflows is a then powerful framework to analyze microbiota from shotgun raw sequence data.

# References

