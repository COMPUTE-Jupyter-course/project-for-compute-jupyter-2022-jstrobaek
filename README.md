[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7768644.svg)](https://doi.org/10.5281/zenodo.7768644)

# Identification of Protective Antibodies using _in silico_ Protein Docking coupled with Targeted Chemical Cross-Linking Mass Spectrometry

This repository was created to complete the [project work](https://github.com/mlund/jupyter-course#project-work) assigned through [this](https://github.com/mlund/jupyter-course) Jupyter Notebook course.

## Abstract

Central to our interaction with pathogens is the relationship between antigen and antibody. Where some antibodies, through the seemingly stochastic natural process of affinity maturation, will award an individual immunity. The success is mediated by several factors—e.g. epitope selectivity and binding affinity—governed by the structural properties of the binding pocket, informed by the residues in the amino acid sequence. Elucidating this selective assembly process is of great interest for vaccine discovery. But the inherent complexity of these biological processes impose multiple challenges for both data generation and subsequent data analysis. However, recent advances in protein structure prediction present new opportunities for exploring antibody repertoires by awarding a higher precision to _in silico_ analysis. Using these advances in tandem with chemical cross-linking protein mass spectrometry could shed new light on the maturation process, and the potential formation of protective antibodies. This exploratory study tries to streamline the analysis of B-cell receptor repertoires and chemical cross-linking mass spectrometry data.

## Visualization of Targeted Cross-Linking Data

This repository hosts a Jupyter Notebook for reproducing some of the analysis and visualization pertaining to the title project. Follow the instructions below to access this Notebook.

### Clone the repository

Clone this repo either by using the command-line:

```shell
git clone https://github.com/COMPUTE-Jupyter-course/project-for-compute-jupyter-2022-jstrobaek.git
```

Or by downloading and unzipping [this archive](https://github.com/COMPUTE-Jupyter-course/project-for-compute-jupyter-2022-jstrobaek/archive/refs/heads/trunk.zip).

### Notebook dependencies

To run the Notebook it is required to have some specific python packages installed (detailed in the [environment.yml](environment.yml) file), which is easily done using Anaconda (see [below](#environment)). For full reproducibility it is also required to have some of the output data tied to the title project (detailed [below](#data)).

#### Environment

From the base directory of your cloned version of this repository, execute the following command:

```shell
conda env create -f environment.yml
```

This will create an Anaconda environment named `xl_viz` that can be activated with `conda activate xl_viz`. If you wish to rename the environment change the value assigned to the `name` key in the [environment file](environment.yml).

Before you run the Notebook you should add the new environment to the kernel list (make sure to activate it first):

```shell
conda activate xl_viz && \
python3 -m ipykernel install --prefix="$CONDA_PREFIX" --name 'xl_viz'
```

#### Data

To be able to run the Notebook and reproduce the related figures it is required to [download](https://zenodo.org/record/7768644/files/supplement_data.zip?download=1) the associated supplement data from [the Zenodo archive](https://doi.org/10.5281/zenodo.7768644). You also need to unzip it in the cloned repo base directory.
