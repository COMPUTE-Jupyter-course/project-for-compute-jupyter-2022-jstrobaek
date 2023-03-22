# Identification of Protective Antibodies using _in silico_ Protein Docking coupled with Targeted Chemical Cross-Linking Mass Spectrometry

## Abstract

Central to our interaction with pathogens is the relationship between antigen and antibody. Where some antibodies, through the seemingly stochastic natural process of affinity maturation, will award an individual immunity. The success is mediated by several factors—e.g. epitope selectivity and binding affinity—governed by the structural properties of the binding pocket, informed by the residues in the amino acid sequence. Elucidating this selective assembly process is of great interest for vaccine discovery. But the inherent complexity of these biological processes impose multiple challenges for both data generation and subsequent data analysis. However, recent advances in protein structure prediction present new opportunities for exploring antibody repertoires by awarding a higher precision to _in silico_ analysis. Using these advances in tandem with chemical cross-linking protein mass spectrometry could shed new light on the maturation process, and the potential formation of protective antibodies. This exploratory study tries to streamline the analysis of B-cell receptor repertoires and chemical cross-linking mass spectrometry data.

## Visualization of Targeted Cross-Linking Data

This repository hosts a Jupyter Notebook for reproducing some of the analysis and visualization pertaining to the title project. Follow the instructions below to access this Notebook.

### Clone the repository

Clone this repo either by using the command-line:

```sh
git clone https://github.com/COMPUTE-Jupyter-course/project-for-compute-jupyter-2022-jstrobaek.git
```

Or by downloading and unzipping [this archive](https://github.com/COMPUTE-Jupyter-course/project-for-compute-jupyter-2022-jstrobaek/archive/refs/heads/trunk.zip).

### Notebook dependencies

To run the Notebook it is required to have some specific python packages installed (detailed in the [environment.yml](environment.yml) file), which is easily done using Anaconda (see [below](#environment)). For full reproducibility it is also required to have some of the output data tied to the title project (detailed [below](#data)).

#### Environment

From the base directory of your cloned version of this repository, execute the following command:

```sh
conda env create -f environment.yml
```

This will create an Anaconda environment named `xl_viz` that can be activated with `conda activate xl_viz`. If you wish to rename the environment change the value assigned to the `name: ` key in the [environment file](environment.yml).

#### Data

For now, the data required to reproduce the (current) analysis can be downloaded [here](https://drive.google.com/file/d/1C6LvIg48siHp95bZ-W46otlra1EVjaTP/view?usp=share_link). Unzip in the git-repo base directory to enable Notebook execution.
