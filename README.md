# Marissa Boucher - Autumn 2025 PHYS 25000 Final
This repository is forked from [Reconal/big_rays](https://github.com/philippwindischhofer/Reconal/tree/big_rays) as my submission for the PHYS 250 final project and will not be updated after December 2025. I've added a copy of my poster (`final_poster.pdf`) and a Jupyter notebook (`traveltime_example.ipynb`) so that the calculator can be run after installation without RNO-G detector files.  

This repository also includes a hard-coded refractive index model adapted from the `greenland_simple` model in NuRadioMC. Typically this model would be implemented using the `get_ior_from_nuradio` function in `defs.py`, but the work of installing NuRadioMC isn't worth it for this single application.  

Please read the installation instructions below, as this project depends on a forked version of another Python package.

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