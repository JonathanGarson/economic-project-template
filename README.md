# economic-project-template
This a template for economics research project based on [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/). It is a free to use template, you will just have to download the license you chose.

The code is oriented toward python replication but it works for R, Stata and any economic projects. To use it you just need to do the following command line :

```
pip install cookiecutter #to install the python package
cookiecutter https://github.com/JonathanGarson/economic-project-template.git #to use the economic template
```
It will create automatically in your working directory a folder with the following structure :

------------

    ├── LICENSE            <- Download it
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── intermediate   <- Intermediate data that has been transformed.
    │   ├── final          <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── output             <- Generated outputs.
    │   ├── tables         <- Generated graphics to be used in the paper and appendix.
    │   └── figures        <- Generated graphics to be used in the paper and appendix.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └──  src               <- Source code for use in this project.
         └── __init__.py   <- Makes src a Python module
--------

