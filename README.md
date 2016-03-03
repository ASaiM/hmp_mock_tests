Test of ASaiM workflow on HMP Mock Community samples
====================================================

To test ASaiM workflow, we use mock samples from HMP. These datasets have a controlled community content. Moreover, these datasets were analyzed using EBI metagenomic workflow and the corresponding results are [available](https://www.ebi.ac.uk/metagenomics/projects/SRP004311).

# Requirements

- `wget`
- `bioblend`
- [ASaiM Galaxy instance](https://github.com/ASaiM/framework), launched and populated with tools and databases (Check also [ASaiM documentation](http://asaim.readthedocs.org/en/latest/framework/index.html))

# Usage

Get the input datasets and EBI data:

```
./src/download_EBI_data.sh
```


