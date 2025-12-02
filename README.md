# Marissa Boucher - Autumn 2025 PHYS 25000 Final
This repository is forked from [Reconal/big_rays](https://github.com/philippwindischhofer/Reconal/tree/big_rays) as my submission for the PHYS 250 final project and will not be updated after December 2025. I've added a Jupyter notebook (`traveltime_example.ipynb`) so that the calculator can be run after installation without RNO-G detector files.  

Typically, using the code in this repository requires installing the (NuRadioMC package)[https://github.com/nu-radio/NuRadioMC]. This has many dependencies and seems like unnecessary effort to test such a small project, so I've made a few changes to this repository that mean you don't have to install the software.

1. This repository includes a hard-coded refractive index model adapted from the `greenland_simple` model in NuRadioMC. Normally, this model would be implemented using the `get_ior_from_nuradio` function in `defs.py`.  
1. I've included files with analytic solutions to this problem that I used NuRadioMC to generate. This took a few hours to calculate, so I don't include the generation code here, but I use the solutions to test how accurate my maps are.

Please read the installation instructions below, as this project *does* depend on a forked version of another Python package.

## Installation

This software requires at least Python 3.11.

```
python -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

This submission also requires that you install my [forked version](https://github.com/mcb28/pykonal) of `pykonal`.

```
git clone https://github.com/mcb28/pykonal.git
cd pykonal
pip install .
```