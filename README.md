Test of ASaiM workflow on HMP Mock Community samples
====================================================

To test ASaiM workflow, we use mock samples from HMP. These datasets have a controlled community content. Moreover, these datasets were analyzed using EBI metagenomic workflow and the corresponding results are [available](https://www.ebi.ac.uk/metagenomics/projects/SRP004311).

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

Get 

Get the input datasets and EBI result data and format them:

```
./src/download_EBI_data.sh
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

A report of this analysis is available in `doc` directory. It is in markdown. To export it in PDF, you can use:

```
./doc/report/build.sh
```

It requires PANDOC.
