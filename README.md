# economic-project-template
This a template for economics research project based on [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) package and [Audrey Feldroy & al](https://github.com/audreyfeldroy/cookiecutter-pypackage/tree/master) work.

If the structure does not correspond to your needs do not hesitate to propose updates, this is a collaborative project which objective is to ease replication and provide a common structure to research in economics.

The code is oriented toward python replication but it works for R, Stata and any economic projects. To use it you just need to execute the following command line :

```
pip install cookiecutter #to install the python package
cookiecutter https://github.com/JonathanGarson/economic-project-template.git #to use the economic template
```
Note that you might have issues using this way on Windows, to avoid them you can use the following python code in your terminal :

```
python #to turn you terminal into python (to quit just type "quit()")
from cookiecutter.main import cookiecutter
cookiecutter("gh:JonathanGarson//economic-project-template")
```

It will create automatically in your working directory a folder with the following structure :

------------

    ├── LICENSE            <- Download it
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── data
    │   ├── temp           <- Intermediate data that has been transformed.
    │   ├── final          <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks.
    │   
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │   
    ├── output             <- Generated outputs.
    │   ├── paper
    │   │   ├── main           <- contains the main paper in pdf format.
    │   │   └── latex_files    <- contains the latex files to generate the paper.
    │   └── appendix
    │       ├── main           <- contains the appendix in pdf format.
    │       └── latex_files    <- contains the latex files to generate the appendix.
    │
    ├── src                <- Source code for use in this project.
    ├── __init__.py        <- Makes src a Python module
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    └──  setup.py          <- makes project pip installable (pip install -e .) so src can be imported
    
------------

To format it to a replication format package please use the ```prep_for_replication.py``` code. It will adopt the structure bellow.

------------

    ├── LICENSE            <- Download it
    ├── README.md          <- The top-level README for developers using this project.
    ├── paper
    │   ├── main           <- contains the main paper in pdf format.
    │   └── latex_files    <- contains the latex files to generate the paper.
    │
    ├── appendix
    │   ├── main           <- contains the appendix in pdf format.
    │   └── latex_files    <- contains the latex files to generate the appendix.
    │
    ├── code               <- contains the code, data and output.
    │   ├── data
    │   │   ├── temp           <- Intermediate data that has been transformed.
    │   │   ├── final          <- The final, canonical data sets for modeling.
    │   │   └── raw            <- The original, immutable data dump.
    │   │
    │   ├── notebooks          <- Jupyter notebooks.
    │   │
    │   ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │   │
    │   ├── output             <- Generated outputs.
    │   │   ├── tables         <- Generated graphics to be used in the paper and appendix.
    │   │   └── figures        <- Generated graphics to be used in the paper and appendix.
    │   │
    │   └──  src               <- Source code for use in this project.
    │         └── __init__.py  <- Makes src a Python module
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    └──  setup.py          <- makes project pip installable (pip install -e .) so src can be imported
    
--------