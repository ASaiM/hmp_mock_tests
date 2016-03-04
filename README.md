Test of ASaiM workflow on HMP Mock Community samples
====================================================

To test ASaiM workflow, we use mock samples from HMP. These datasets have a controlled community content. Moreover, these datasets were analyzed using EBI metagenomic workflow and the corresponding results are [available](https://www.ebi.ac.uk/metagenomics/projects/SRP004311).

# Requirements

- `wget`
- `bioblend`
- [ASaiM Galaxy instance](https://github.com/ASaiM/framework), launched and populated with tools and databases (Check also [ASaiM documentation](http://asaim.readthedocs.org/en/latest/framework/index.html))

# Usage

Get the input datasets and EBI result data and format them:

```
./src/download_EBI_data.sh
```

Launch ASaiM workflow on both datasets (this task takes several hours):

```
./src/launch_asaim_workflow.sh <asaim_galaxy_instance_url> <your_api_key_on_asaim_galaxy_instance>
```

Concatenate results (EBI one and ASaiM one) to compare them:

```
./src/concatenate_results.sh 
```
