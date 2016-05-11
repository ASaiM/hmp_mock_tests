Validation of ASaiM framework on HMP Mock Community samples
==========================================================

We test ASaiM framework on mock samples from HMP which have a controlled community content. The results were compared to [EBI metagenomic pipeline results](https://www.ebi.ac.uk/metagenomics/projects/SRP004311).

# Requirements

- `wget`
- `pip` and some Python modules you can install using `pip install -r requirements.txt`
- [ASaiM framework](https://github.com/ASaiM/framework) with its custom Galaxy instance launched and populated with tools and databases. You can also check [ASaiM documentation](http://asaim.readthedocs.org/en/latest/framework/index.html) for further information.

# Usage

Generate an API key corresponding to your account on the custom Galaxy instance (in `User` menu, on top panel) of ASaiM framework, and fill the [`config.yml`](config.yml) file:

```
asaim_galaxy_instance_url: "http://0.0.0.0:8080/"
api_key_on_asaim_galaxy_instance: "apikey"
```

Get the input datasets and EBI result data and format them:

```
./src/download_format_EBI_data.sh
```

Get reference genomes and mapped input datasets on them:

```
./src/download_extract_map_reference_genomes.sh
```

Launch ASaiM workflow on both datasets (this task takes several hours):

```
./src/launch_asaim_workflow.sh
```

You can visualize workflows running by browsing ASaiM Galaxy instance. 

Export ASaiM workflow outputs (when the workflows are done):

```
./src/export_asaim_workflow_outputs.sh
``` 

Concatenate results (EBI one and ASaiM one) to compare them:

```
./src/concatenate_results.sh
```

# Report

A [report](doc/report/report.pdf) of this analysis is available in `doc/report` directory.


To generate the PDF from the markdown file (requiring PANDOC):

```
./doc/report/build.sh
```
