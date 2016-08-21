Validation of ASaiM framework on HMP Mock Community samples
==========================================================

We test ASaiM framework on mock samples from HMP which have a controlled community content. The results were compared to [EBI metagenomic pipeline results](https://www.ebi.ac.uk/metagenomics/projects/SRP004311).

# Requirements

- `conda`
- [ASaiM framework](https://github.com/ASaiM/framework) with its custom Galaxy instance launched and populated with tools and databases. You can also check [ASaiM documentation](http://asaim.readthedocs.org/en/latest/framework/index.html) for further information.

Once `conda` is installed, create the `conda` environment (with all required dependencies):

```
$ conda config --add channels biocore
$ conda config --add channels bioconda
$ conda env create -f conda_env.yml
```

# Usage

Activate `conda` environment:

```
$ source activate hmp_mock
```

Generate an API key corresponding to your account on the custom Galaxy instance (in `User` menu, on top panel) of ASaiM framework, and fill the [`config.yml`](config.yml) file:

```
asaim_galaxy_instance_url: "http://0.0.0.0:8080/"
api_key_on_asaim_galaxy_instance: "apikey"
```

Launch analyses:

```
$ ./src/launch_hmp_mock_analyses.sh
```

This script will

- Get the input datasets, EBI result data and format them
- Get reference genomes, reference rRNA sequences and mapped input datasets on them
- Launch ASaiM workflow on both datasets (this task takes several hours). You can visualize workflows running by browsing ASaiM Galaxy instance

Export results and analyze them:

```
$ ./src/export_analyze_hmp_mock_results.sh
```

This script will

- Export ASaiM workflow outputs (when the workflows are done) et generate all graphics
- Concatenate results (EBI one and ASaiM one) to compare them

# Report

A [report](doc/report/report.pdf) of this analysis is available in `doc/report` directory.

To generate the PDF from the markdown file (requiring PANDOC):

```
$ ./doc/report/build.sh
```
