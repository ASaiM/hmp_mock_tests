---
title: "Validation of the ASaiM framework and its workflows on HMP mock community samples"
subject_session: Sequence analysis
subtitle: "Supplementary material 2"
author:
    - Bérénice Batut
    - Clémence Defois
    - Kévin Gravouil
    - Jean-François Brugère
    - Eric Peyretaillade
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

The ASaiM framework and its workflows have been tested and validated on two mock metagenomic data of an artificial community (with 22 known microbial strains). The datasets are available on *EBI metagenomics* database. Taxonomic and functional results produced by the ASaiM framework have been extensively analyzed and compared to expectations and to results obtained with the [*EBI metagenomics* pipeline](https://www.ebi.ac.uk/metagenomics/pipelines/1.0) [@hunter_ebi_2014].

For these datasets, the ASaiM framework produces accurate and precise taxonomic assignations, different functional results (gene families, pathways, GO slim terms) and results combining taxonomic and functional information. Despite almost 1.4 millions of raw metagenomic sequences, these analyses were executed in less than 6h on a commodity computer. Hence, the ASaiM framework and its workflows are proved to be relevant for the analyses of microbiota datasets.

# Data

On [*EBI metagenomics* database](https://www.ebi.ac.uk/metagenomics/), [two mock community samples](https://www.ebi.ac.uk/metagenomics/projects/SRP004311) for Human Microbiome Project (HMP) are available. Both samples contain a genomic mixture of 22 known microbial strains which are targeted based on 16S abundance (Table \ref{expected_species}). In first sample ([SRR072232](https://www.ebi.ac.uk/metagenomics/projects/SRP004311/samples/SRS121012/runs/SRR072232/results/versions/1.0)), the targeted 16S copies of the strains vary by up to four orders of magnitude between the strains (Table \ref{expected_species}), whereas in second sample ([SRR072233](https://www.ebi.ac.uk/metagenomics/projects/SRP004311/samples/SRS121011/runs/SRR072233/results/versions/1.0)) same 16S copy number is targeted for each strain (Table \ref{expected_species}). After pooling, the DNA of the strains of both samples were sequenced using 454 GS FLX Titanium. 1,225,169 and 1,386,198 raw metagenomic sequences are then respectively obtained for the first dataset (SRR072232) and the second dataset (SRR072233).

# Methods

Both datasets have been analyzed using the ASaiM framework. The results are extensively analyzed and compared to expected results from reference genome information and to *EBI metagenomics* results. Details about these analyses (workflows, scripts) are available on a dedicated GitHub repository ([https://github.com/ASaiM/hmp_mock_tests](https://github.com/ASaiM/hmp_mock_tests)).

## Abundance computation using mapping on reference genomes

In both datasets, abundance of each strain is targeted based on 16S quantity to build the genomic mixture before sequencing. But these targeted abundances may be not reflect the final abundances (*e.g.* 16S copy number variation, sequencing bias). We have a known composition of the datasets with an expected abundances before sequencing but no information about the real abundance of the strains after sequencing.

Before any analysis of *EBI metagenomics* and ASaiM results, we need more insights in the real abundance of the strains after sequencing. We mapped raw reads on reference genomes of expected strains using BWA [@li_fast_2009;@li_fast_2010] (using default parameters). We then extract the "exact" abundances of expected strains in the metagenomic datasets, after DNA pooling and sequencing (*i.e.* not based on targeted rRNA operon counts in PCR).

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
\caption{Expected strains, their taxonomy and their targeted relative abundance (percentage) based on 16S gene copy counts (abundance, from metadata on \textit{EBI metagenomics} database) on both samples (SRR072232 and SRR072233)}
\label{expected_species}
\end{table}
\end{landscape}
\newpage
\restoregeometry

Similar community compositions are observed using mapping-based relative abundances of strains or targeted relative abundance (Figure \ref{mapping_comparison}): the Bray-Curtis dissimilarity scores are smaller than 0.5 (0.338 for SRR02232 and 0.479 for SRR072233). For SRR02232, similar variations in relative abundances between the species are then observed using both mapping and targeted abundances (Figure \ref{mapping_comparison}). However, different observations are made for SRR072233 (Figure \ref{mapping_comparison}): identical targeted abundances are expected for all species, but variations are observed for mapping based abundances. The variation of 16S gene copy number between the species can explain the differences between targeted abundances and mapping-based abundances. Indeed, the targeted abundances are based on 16S copy number targeted in PCR to build the DNA pool. But, the number of 16S gene copies is not identical in the strains (from 1 for *Candida albicans* to 14 for *Clostridium beijerinckii*). Hence, even with identical targeted abundances (*e.g.* for SRR072233), a species with twice 16S gene copies in its genome would be found twice less abundant in mapping-based relative abundance results. The 16S gene copy number variation induces then a difference between the relative abundance based on mapping reads on whole genome and the relative abundance based on the targeted 16S gene counts.

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

Taxonomic analyses in *EBI metagenomics* and ASaiM workflows are executed on metagenomic sequences, *i.e.* on data after DNA pooling and sequencing. Mapping-based relatives abundances computed on raw metagenomic sequences are then more appropriate expected abundance information than the relative abundances based on 16S counts. We will then use this information in the next sections.

## Analyses using *EBI Metagenomics*

In *EBI metagenomics* database, both datasets have been analysed with [*EBI metagenomics* pipeline (Version 1.0)](https://www.ebi.ac.uk/metagenomics/pipelines/1.0) (Figure \ref{ebi_pipeline}).

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/ebi_workflow.pdf}
    \caption{\textit{EBI metagenomics} pipeline (version 1.0).
    The grey boxes correspond to data, the blue boxes to pretreatment steps, the red boxes to functional analysis steps and the green boxes to taxonomic analysis steps.}
    \label{ebi_pipeline}
\end{figure}

To ease comparison with ASaiM results, *EBI metagenomics* pipeline results were downloaded from *EBI metagenomics* database and formatted. First, to compute relative abundances of each clade at all taxonomic levels, OTUs with taxonomic assignation are extracted and aggregated. Second, *EBI metagenomics* pipeline generates 3 types of functional results (Figure \ref{ebi_pipeline}): matches with InterPro, complete GO annotations and GO slim annotations. Here, we focus on GO slim annotations. The annotations are formatted to extract relative abundances (in percentage) of GO slim term annotations inside each GO slim term category (cellular components, biological processes and molecular functions).

## Analyses using ASaiM framework

Main workflow (Supplementary material 1) of the ASaiM framework is used to analyze both datasets. The ASaiM framework were deployed on a computer with Debian GNU/Linux System, 8 cores Intel(R) Xeon(R) at 2.40 GHz and 32 Go of RAM. On this computer, the workflow execution is relatively fast: < 5h and < 5h30 for datasets with 1,225,169 and 1,386,198 sequences respectively (Table \ref{computation_stats}). The most time-consuming step is functional profiling using *HUMAnN2* [@abubucker_metabolic_2012] which last $\simeq$ 64% of overall time execution (Table \ref{computation_stats}). Size of the process in memory is stable over workflow execution (variability inferior to 40 kb) (Table \ref{computation_stats}).

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

To compare taxonomic and functional results of both datasets, we used the comparative analysis workflows available with the ASaiM framework (Supplementary material 1).

To verify taxonomic results, we checked that each expected organism can be found using same tools and databases than in ASaiM. A dataset is then built for each reference genome. To build these datasets, the reference genome of each expected organism is randomly cut in smaller sequences such as the size distribution of sequences is identical to the one in SRR072232 databaset after quality control and dereplication, with same sequence number. Taxonomic assignation for each dataset is then extracted using MetaPhlAN [@truong_metaphlan2_2015;@segata_metagenomic_2012], as in ASaiM.

## Comparison of *EBI metagenomics* results and ASaiM results

The first step in comparison of *EBI metagenomics* results and ASaiM results is the comparison of rRNA sequences extracted with both methods to determine if similar rRNA sequences are found with both methods. We first compare the extracted rRNA sequences using the names of the corresponding raw sequences. However, rRNA sequence extraction process is executed after quality treatment and dereplication in both pipelines. Some duplicated sequences were then eliminated during dereplication process and the pool of sequences are then not comparable using only their names. To compare rRNA sequences, we run Blast [@camacho_blast_2009] on rRNA sequences found with *EBI metagenomics* against rRNA sequences found with ASaiM. Sequences are considered as similar between both pipelines if the similarity percentage is higher than 98\% on more than 98\% of the sequence length and if the e-value is below 1$\cdot 10^{-16}$. We also compare to expected rRNA sequences: we run SortMeRNA with same parameters as in ASaiM but with a database made of rRNAs extracted from the reference genomes of the expected organisms.

In ASaiM framework, *MetaPhlAn* computes the relative abundance of clades only on assigned reads. No count is made of non assigned reads unlike *EBI metagenomics* pipeline. To compare relative abundances between both pipelines, we focus on relative abundances computed on OTUS or reads with a complete taxonomic assignation from kingdom to family. These results are also compared to relative mapping-based abundances.

Both *EBI metagenomics* and ASaiM workflows group functional matches into GO slim terms, a subset of the terms in the whole Gene Ontology focusing on microbial metabolic functions. These GO slim terms give a broad overview of the ontology content. To compare *EBI metagenomics* and ASaiM results, relative abundance of GO slim terms for both samples and both workflows are concatenated and compared, given the workflow depicted in Figure \ref{go_slim_comparison_workflow}.

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/go_slim_comparison_workflow.pdf}
    \caption{Workflow to compare GO slim annotation abundances between samples (SRR072232, SRR072233) and workflows (\textit{EBI metagenomics}, ASaiM). This workflow is available with ASaiM Galaxy instance. The grey boxes correspond to data, the blue boxes to processing steps.}
    \label{go_slim_comparison_workflow}
\end{figure}

# Results

## Preprocessing steps

In both workflows, raw sequences are pre-processed before any taxonomic or functional analysis. These preprocessing steps include a quality control to remove low quality, small or duplicated sequences and also a step to sort rRNA/rDNA sequences from non rRNA/rDNA sequences.

The tools and the parameters in the ASaiM framework differ from the ones used in *EBI metagenomics* pipeline. We then observe different preprocessing outputs (Table \ref{pretreatment_stats}).

\begin{table}[h!]
\centering
\begin{tabular}{lrrrrrrrr}
\hline
 & \multicolumn{4}{c}{SRR072232} & \multicolumn{4}{c}{SRR072233} \\
Sequences & \multicolumn{2}{c}{EBI} & \multicolumn{2}{c}{ASaiM} & \multicolumn{2}{c}{EBI} & \multicolumn{2}{c}{ASaiM} \\
\hline
Raw sequences & \multicolumn{4}{c}{1,225,169} & \multicolumn{4}{c}{1,386,198}\\
Sequences after quality control and dereplication & 997,622 & 81.4\% & 1,175,853 & 96\% & 1,197,748 & 86.4\% & 1,343,451 & 96.9\% \\
rDNA sequences & 9,453 & 0.95\% & 16,016 & 1.4\% & 9,698 & 0.81\% & 13,850 & 1\%\\
non rDNA sequences & 988,169 & 99.05\% & 1,159,837 & 98.6\% & 1,188,050 & 99.19\% & 1,329,601 & 99\%\\
\hline
\end{tabular}
\caption{Statistics of pretreatments for EBI and ASaiM on both samples (SRR072233 and SRR072233)}
\label{pretreatment_stats}
\end{table}

The number of sequence after quality control and dereplication are different between both pipelines (Table \ref{pretreatment_stats}). ASaiM framework conserves more sequences (> 96 \%) during these first steps of quality control and dereplication than *EBI metagenomics* does (< 87 \%, Table \ref{pretreatment_stats}). These differences may come from the difference of minimal length sequence. In *EBI metagenomics* pipeline, sequences with less than 100 nucleotides are removed, while in ASaiM the threshold is fixed to 60 nucleotides. More sequences are then conserved with ASaiM. However, this threshold difference explain only small part of observed difference in sequence number after quality control and dereplication. Indeed, if quality control in ASaiM framework is run with same length threshold as in *EBI metagenomics* pipeline, more sequences are eliminated (7.4% and 5.9%) than with standard length threshold (Table \ref{pretreatment_stats}). These proportions remain lower than the one observed with *EBI metagenomics* pipeline (Table \ref{pretreatment_stats}). Sequence number differences after quality control and dereplication are then induced moderately by smaller length thresholds in ASaiM. Main sequence number difference are more probably induced by the different used tools, their underlying algorithms and implementations.

In both datasets and with both workflows, few rDNA sequences are found in datasets (Table \ref{pretreatment_stats}). These datasets are composed of whole genome metagenomic sequences. Few copies of rDNA genes are present in organisms (bacteria, archeae or eukaryotes) and are then expected in metagenomic sequences, as observed for the datasets. Nevertheless, higher proportions of rDNA sequences are found with ASaiM framework (1-1.4\%) than with *EBI metagonomics* (0.8-0.9\%, Table \ref{pretreatment_stats}). In *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}) *rRNASelector* [@lee_rrnaselector:_2011] is used to select rDNA bacterial and archaeal sequences. In ASaiM framework, sequences are sorted using *SortMeRNA* [@kopylova_sortmerna:_2012] and databases with bacteria, archaea and also eukaryotes rDNA sequences. Differences of rRNA reference databases, particularly the use of eukaryotic database in ASaiM, may then explain the differences in rRNA sequence proportions extracted by both workflows. In ASaiM framework, 0.03-0.05\% of all sequences are matched against databases dedicated to eukaryotic rDNA sequences, but this small proportion does however not explain the whole difference of rDNA sequence proportion between *EBI metagenomics* and ASaiM framework. The rRNA sequences found with *EBI metagenomics* correspond to a subset of rRNA sequences found with ASaiM: more than 97\% of rRNA sequences found with *EBI metagenomics* are similarly also found as rRNA sequences with ASaiM framework, less than 2.5\% of rRNA sequences found with *EBI metagenomics* are identified as non rRNA sequences with ASaiM framework, the other sequences (<60) may correspond to sequences differentially filtered or trimmed during quality control. *EBI metagenomics* and ASaiM pipelines extract then similar rRNA sequences and these sequences corresponds to sequences from expected organisms. A high proportion (80-86\%) of rRNA sequences found with ASaiM and its general rRNA databases are also found with  SortMeRNA and databases constitued only of rRNA sequences from expected organisms, and 98.8-99.3\% of rRNA sequences found with expected organism rRNA sequence databases are found with ASaiM general databases. Hence, sequence sorting in ASaiM extracts rRNA/rDNA sequences close to rRNA sequences of expected organisms.

## Taxonomic analyses

Both metagenomic datasets come from a genomic mixture of 22 known microbial strains whose abundance is known (based on mapping on reference genomes, Figure \ref{expected_taxonomy}). The expected community structures inside the datasets are then known. This information can then be used to analyze ASaiM framework taxonomic results and compare them to *EBI metagenomics* pipeline taxonomic results.

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/expected_taxonomy.pdf}
    \caption{Expected taxonomy for SRR072232 (left) and SRR072233 (right) from domains to species. Circle diameters at each taxonomic levels are proportional to mapping-based relative abundance of corresponding taxon.}
    \label{expected_taxonomy}
\end{figure}

### ASaiM taxonomic results

ASaiM workflow uses *MetaPhlAN* (2.2.5) [@truong_metaphlan2_2015;@segata_metagenomic_2012] for taxonomic analyses. *MetaPhlAn* profiles the microbial community structure using a database of unique clade-specific marker genes identified from 17,000 reference genomes. *MetaPhlAn* runs fast within ASaiM framework: less than 10 minutes to assign taxonomy on > 1,100,000 sequences (Table \ref{computation_stats}).

*MetaPhlAn* generates a plain text file with relative abundance of clades at different taxonomic levels. To visualize *MetaPhlAn* results, *Krona* [@ondov_interactive_2011] generates interactive representations of taxonomic assignation and *GraPhlan* for static representations. Original static representations are modified (*e.g.* colors, legend) to help comparison with expected taxonomy (Figure \ref{asaim_taxonomy}).

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
    \caption{Relative abundances (percentage in log scale) of expected species for SRR072232 (left) and SRR072232 (right) with comparison between expected abundances (based on mapping counts, red thin bars) and abundances obtained with ASaiM (blue wide bars)}
    \label{species_abundances}
\end{figure}

Same species are expected in both dataset, but the taxonomic diversity in SRR072232 dataset is reduced compared to the one in SRR072233 dataset (Figure \ref{asaim_taxonomy}) with less taxons found at each taxonomic levels. 17 and 20 of the 22 expected species are found for SRR072232 and SRR072233 respectively (Figure \ref{species_abundances}).

The expected species *Candidata albicans* is missing in both dataset results, because of the used *MetaPhlAn2* database. The phylogenetic markers for this species seem to be missing in *MetaPhlAn2* database: even on a dataset with only sequences extracted from *Candidata albicans* reference genomes, this species is not found with *MetaPhlAn2*.

Other missing species (*e.g.* *Enterococcus faecalis* or *Lactobacillus gasseri*) correspond to underrepresented species, *i.e.* species whose few sequences are found using mapping (Figure \ref{species_abundances}). The phylogenetic signal is then too low to detect these species using *MetaPhlAn2*. Indeed, for both datasets, ASaiM framework can not detect any species with mapping-based relative abundance smaller than 0.1\% (Figure \ref{species_abundances}).

One species with mapping-based relative abundance higher than 0.1\% is not found for SRR072232 datasets: *Bacillus cereus thuringiensis*. Few phylogenetic markers for this species are found in *MetaPhlAn2* database. Indeed, on dataset with only *Bacillus cereus thuringiensis* reference genome's sequences, phylogenetic markers for *Bacillus cereus thuringiensis* are found in very low percentage of sequences (0.14\% of sequences against 2.28\% on average for other expected species). The phylogenetic signal may be then too low to detect this species inside whole metagenomic sequences.

### Comparison of ASaiM taxonomic results with EBI metagenomics taxonomic results

We can now compare ASaiM taxonomic results to *EBI metagenomics* ones.

\begin{figure}[h!]
    \centering
    \includegraphics[width = \linewidth]{../images/ebi_taxonomy.pdf}
    \caption{Taxonomy for SRR072232 (left) and SRR072233 (right) from domains to families, found with EBI metagenomics pipeline. Circle diameters at each taxonomic levels are proportional to relative abundance of corresponding taxon. Colors and family numbers are the same as the ones used in Figure \ref{expected_taxonomy}. Gray circles and lines represent unexpected lineages.}
    \label{ebi_taxonomy}
\end{figure}

*EBI metagenomics* pipeline uses *QIIME* [@caporaso_qiime_2010] to identify Operational Taxonomic Units (OTUs) and taxonomic assignation for these OTUs. *EBI metagenomics* focuses on taxonomic assignations of 16S sequences. In ASaiM framework, *MetaPhlAn* is executed on quality treated sequences, before any sorting step. Diverse phylogenetic markers are searched on all sequence types (rDNA, non rDNA), not only 16S ones as *QIIME* [@caporaso_qiime_2010] does. In both datasets, 16S sequences represent a low proportion of sequences (Table \ref{pretreatment_stats}). Taxonomic assignations of *EBI metagenomics* rely then on less sequences than the ones of ASaiM framework: they are less statistically supported.

The taxonomic assignations in *EBI metagenomics* go from kingdom to family (Figure \ref{ebi_taxonomy}), while in ASaiM framework *MetaPhlAn* outputs taxonomic assignations from kingdom to species (Figure \ref{asaim_taxonomy}). In ASaiM framework, the taxonomic assignations are more precise and more statistically supported than in *EBI metagenomics*.

In both *EBI metagenomics* and ASaiM framework, we observe taxonomic assignations which are unexpected (Table \ref{unexpected_clades}, Figures \ref{asaim_taxonomy} and \ref{ebi_taxonomy}). While only species are found as unexpected in ASaiM framework, *EBI metagenomics* founds unexpected classes, orders and families (Table \ref{unexpected_clades}, Figure \ref{ebi_taxonomy}). For ASaiM framework, 4 species in each sample are identified as "unclassified" (Table \ref{unexpected_clades}): they are affiliated to the correct genus but not to correct species. Corresponding sequences may be highly similar in several species from the same genus and can not then be assigned to a specific species. Taxonomic assignations with *MetaPhlAN* are then more accurate (less unexpected clades and for a higher level).

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
Genus & & $^{1}$ & & $^{1}$ & \\
\hline
Species & & $^{1}$ & & $^{1}$ & \\
& \textit{Escherichia} unclassified & & 4.85\% & & 0.8\% \\
& \textit{Pseudomonas} unclassified & & 1.12\% & & 0.56\% \\
& \textit{Methanobrevibacter} unclassified & & & & 0.24\% \\
& \textit{Deinococcus} unclassified & & 0.16\% & & \\
\hline
\end{tabular}
\caption{Relative abundances of unexpected clades at different taxonomic levels in taxonomic results of \textit{EBI metagenomics} and ASaiM framework for both samples (SRR072233 and SRR072233).
$^{1}$ No information for this taxonomic level with EBI metagenomics.}
\label{unexpected_clades}
\end{table}

As mentioned before, the most precise taxonomic level for *EBI metagenomics* is family (Figure \ref{ebi_taxonomy}). The further comparisons between *EBI metagenomics* and ASaiM framework results are then focused on this level (Figure \ref{family_abundances}).

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

Neither ASaiM nor *EBI metagenomics* found any low abundance families (mapping-based abundance smaller than 0.1\%, Figure \ref{family_abundances}), similarly to the previous observations on raw ASaiM results. Some families with higher abundances are not found too:

- Listeriaceae family

    The expected abundance for this family is close to the 0.1\% threshold. This family is detected with *EBI metagenomics* but not with ASaiM. *EBI metagenomics* may be then better to detect families with expected low abundance than ASaiM, at least for Listeriaceae family (Figure \ref{family_abundances}).

- Bacillaceae and Debaryomycetaceae families

    Both of these families are not found with *EBI metagenomics* for both datasets (Figure \ref{family_abundances}), despite mapping-based abundance higher than 0.1\%. Bacillaceae and Debaryomycetaceae correspond to the family level of *Bacillus cereus thuringiensis* and *Candida albicans* species, respectively. Both species are either not found or hardly found with ASaiM (Figure \ref{species_abundances}): few phylogenetic markers for these species in *MetaPhlAn2* database. Similarly, the used databases in *EBI metagenomics* may be incomplete regarding phylogenetic markers for the missing families.

Despite less sequences used for the taxonomic assignations, *EBI metagenomics* seems better to detect low abundance families than ASaiM framework.

More generally, variations in observed abundances for *EBI metagenomics* or ASaiM framework correspond to variations in mapping-based abundances (Figure \ref{family_abundances}). For a broader comparison, Bray-Curtis dissimilarity scores are computed on relative abundances of families (Table \ref{taxo_distances}). With scores close to 0, the communities based family compositions are then similar for mapping, *EBI metagenomics* or ASaiM framework results. Bray-Curtis dissimilarity scores are close but higher to 0, small differences are then observed between the different tools. *EBI metagenomics* results on family relative abundances are closer to expected abundances than ASaiM framework results (Table \ref{taxo_distances}). But the differences are small, particularly for SRR072233 datasets, and the scores remain close to 0 (Table \ref{taxo_distances}).

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

For species, the observations are different (Table \ref{taxo_distances}). No information is available on species composition with *EBI metagenomics* and dissimilarity scores are then equal to 1. With ASaiM framework, dissimilarity scores are slightly higher for species than for families but they remain close to 0. Composition in term of species are then similar in ASaiM framework communities and in mapping-based communities.

ASaiM framework gives taxonomic results which are accurate, complete, precise and statistically supported. Moreover, the community structure found with the ASaiM framework is close to the expected community structure of the mock community.

## Functional analyses

Contrary to taxonomic results, no expected results are available as a framework to help comparison.

### ASaiM functional results

ASaiM framework uses [*HUMAnN*2](http://huttenhower.sph.harvard.edu/humann2) [@abubucker_metabolic_2012] for functional analyses. This tool profiles presence/absence and abundance of UniRef50 gene families [@suzek_uniref_2015] and MetaCyc pathways [@caspi_metacyc_2014]. The metabolic profile of a microbial community is described in three outputs: abundances of UniRef50 gene families, coverage and abundance of MetaCyc pathways.

More than 50,000 UniRef50 gene families and 480 MetaCyc pathways (Table \ref{humann2_informations}) are reconstructed from > 1,100,000 non rDNA sequences of both samples (Table \ref{pretreatment_stats}).

\begin{table}[h!]
\centering
\begin{tabular}{lrrrr}
\hline
& \multicolumn{2}{c}{UniRef50 gene families} & \multicolumn{2}{c}{MetaCyc pathways}\\
& SRR072232 & SRR072233 & SRR072232 & SRR072233 \\
\hline
Number & 50,700 & 69,357 & 473 & 481\\
Similar & \multicolumn{2}{c}{26,354} & \multicolumn{2}{c}{466} \\
\% of similar inside all & 51.98\% & 39\% & 98.52\% & 96.88\% \\
Relative abundance (\%) & 91.78\% & 63.76\% & 99.98\% & 99.94\%\\
\hline
\end{tabular}
\caption{Global information about UniRef50 gene families and MetaCyc pathways obtained with \textit{HUMAnN2} for both samples (SRR072233 and SRR072233). For each characteristics (gene families and pathways), several information is extracted: all number, number percentage and relative abundance (\%) of similar characteristics.}
\label{humann2_informations}
\end{table}

Both datasets come from a genomic mixture of 22 identical microbial strains (Table \ref{expected_species}). Same species of both datasets are implied in same metabolic functions. The same metabolic functions are then supposed to be found in both datasets, but with different abundances in both datasets (Table \ref{expected_species}),

The sets of gene families are slightly different between both datasets: < 52\% identical gene families (26,354) are found in both samples (Table \ref{humann2_informations}). These identical gene families correspond to the most abundant ones (> 63\% of relative abundance of gene families for each dataset, Table \ref{humann2_informations}). The non similar gene families may correspond to gene families which are in low abundance, are differentially or partially sequenced or made by species which are in small abundance.

Global metabolism information in pathways are highly similar in both datasets: > 96\% of similar pathways representing > 99.9\% of overall abundance (Table \ref{humann2_informations}). A pathway is identified if a high proportion of gene families involved in this pathway is found. Not all involved gene families are then needed to identify a pathway. The impact on metagenomic sequencing are then reduced and similar pathway sets are then found in both datasets.

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

The abundances of identical metabolic functions are different (Figure \ref{similar_characteristics_abundances}), as expected. The differential abundance of species involved in function metabolization lead to differential abundance of these functions.

UniRef50 gene families and MetaCyc pathways are somehow too specific to obtain a broad overview of the metabolic processes. In ASaiM framework, UniRef50 gene families and their abundances are grouped into Gene Ontology (GO) slim terms (Figure \ref{go_abundances}). We observe of similar profiles of GO slim terms for both datasets (Figure \ref{go_abundances}).

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

Both communities (with same expected strains but in different abundances) have different metabolic profiles: similar metabolic functions but in different abundances, as expected.

### Comparison of ASaiM functional results with *EBI metagenomics* results

In ASaiM framework, *HUMAnN2* computes UniRef50 gene families and their abundances. In *EBI metagenomics* pipeline (Figure \ref{ebi_pipeline}), functional analyses are based on InterPro database. We can not directly compare these functional results. As in ASaiM framework, *EBI metagenomics* pipeline groups InterPro proteins into Gene Ontology slim terms.

Barplot representations of GO slim term abundances for both samples and both workflows can be difficult to interpret (*e.g.* for cellular components, Figure \ref{cellular_components}). We compute then the Bray-Curtis dissimilarity scores on normalized relative abundance of GO slim term abundance inside each category (Table \ref{go_slim_distances}).

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
\caption{Bray-Curtis dissimilarity scores on relative abundances of families and species for both samples (SRR072232 and SRR072233)}
\label{go_slim_distances}
\end{table}

Inside each category, compositions are more similar (dissimilarity scores closer to 0) for both samples analyzed with the same method (*EBI metagenomics* or ASaiM framework) than for same sample analyzed with different methods (*e.g.* SRR072232 analyzed *EBI metagenomics* and ASaiM framework). These composition differences between *EBI metagenomics* and ASaiM framework may come from the different tools, the different databases (InterPro for *EBI metagenomics*, UniRef50 for ASaiM framework) and their way to be grouped into GO slim terms.

## Taxonomically-related functional results

*HUMAnN2* stratifies the abundances of gene families and pathways at the community level. Around 35\% of gene families (> 90\% of relative abundance) and > 80\% pathways (> 50\% of relative abundance) can be then related to the community structure (species and their abundance, Table \ref{taxo_rel_funct_results}). We can exploit this information to relate functional results to taxonomic results and answer questions such as "Which taxa contribute to which metabolic functions? And, in which proportion?".

\begin{table}[h!]
\centering
\begin{tabular}{m{9cm}rrrr}
\hline
 & \multicolumn{2}{c}{UniRef50 gene families} & \multicolumn{2}{c}{MetaCyc pathways}\\
 & SRR072232 & SRR072233 & SRR072232 & SRR072233 \\
\hline
Number & 26,219 & 41,005 & 402 & 400 \\
\% of associated to a species inside all & 26.60\% & 31.62\% & 82.56\% & 80\% \\
Relative abundance (\%) & 93.40\% & 90.24\% & 61.08\% & 51.52\%\\
Identical characteristics & \multicolumn{2}{c}{19,815} & \multicolumn{2}{c}{363} \\
\% of identical characteristics inside characteristics associated to a species  & 68.02\% & 48.32\% & 90.30\% & 90.75\% \\
Relative abundance of identical characteristics inside characteristics associated to a species (\%) & 89.17\% & 44.75\% & 91.87\% & 42.70\%\\
\hline
\end{tabular}
\caption{Global information about UniRef50 gene families and MetaCyc pathways related to species for both samples (SRR072233 and SRR072233). For each characteristics (gene families and pathways), several information is extracted: all number, number percentage and relative abundance (\%) of identical characteristics and \textit{p-value} of Wilcoxon test on relative abundance normalized by the sum of relative abundance for all identical characteristics.}
\label{taxo_rel_funct_results}
\end{table}

For both samples, we observe a significant correlation between CDS number in the species and number of gene families found for these species (Table \ref{correlation_information}). The correlation is significant (*p-value* < 5.09 $\cdot 10^{-3}$) but it is yet not perfect ($r^{2}$ < 0.71). Gene families can not be then directly mapped to CDS (*e.g.* to obtain expected results).

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

The relative abundances of the gene families and the pathways are highly correlated to the observed relative abundance of the involved species (Table \ref{correlation_information}). The sequences of an abundant species in a community are supposed to be abundant in the metagenomic sequences of the community. This relation holds for all sequences, particularly sequences corresponding to gene families. For pathways, the relation is more tricky: a pathway is identified if most of the gene families that constitute them are found. The abundance of a pathway is proportional to the number of complete "copies" of this pathway in the species. Then, a pathway is abundant if its parts are all found in numerous copies, leading to a tricky relation between species abundance and pathway abundance. But, the high correlations between species relative abundance and mean relative pathway abundance (Figure \ref{gene_family_pathway_mean}, Table \ref{correlation_information}) confirm good pathway reconstructions in our datasets, particularly for the abundant species. To confirm the previous observations and conclusion, we also observe a strong and significant correlation between species abundance difference and difference of gene family and pathway mean abundance between both samples (Figure \ref{gene_family_pathway_mean}, Table \ref{correlation_information}).

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

Hence, ASaiM framework approach based on *MetaPhlAn2* and *HUMAnN2* results gives accurate and relevant taxonomically-related functional results.

# Conclusion

ASaiM framework quickly analyses a raw metagenomic dataset (in few hours in a commodity computer). Taxonomic analysis using *MetaPhlAn2* gives a great insight of the community structure with complete, accurate and statistically supported information. *HUMAnN2* and extraction of GO slim terms give a broad overview of metabolic profile of studied microbial community. Furthermore, this metabolic profile can be related to the community structure to obtain information such as which species is involved in which metabolic function. This relation between function and taxonomy is specific to the ASaiM framework and not available with solutions such as *EBI metagenomics* pipeline.

Based on Galaxy, ASaiM framework has all Galaxy's strength: accessibility, reproducibility and modularity. Numerous intermediary results can also be accessed during or after workflow execution, allowing deep investigation of taxonomic and functional analyses of microbial communities. Galaxy, the numerous tools and the workflows make ASaiM a powerful framework to analyze microbiota from shotgun raw sequence data.

# References
