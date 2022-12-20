## Cradle HR system
- [minicondani](https://docs.conda.io/en/latest/miniconda.html) o'rnating
- Repo boshidan (root) quyidagilarni qiling: 
    ```shell
    conda env create -f environment.yml
    conda activate neo-mutational-library
    pip install -e .
    pre-commit install
    ```

### Repo strukturasi    
.. code-block:: none

    ├── .gitignore
    ├── README.md
    ├── LICENSE.md
    ├── environment.yml
    ├── setup.py
    ├── src
    │   └── utils.py
    ├── models
    ├── docs
    ├── tests
    ├── scripts
        └── notebooks
    ├── client-api
    └── data
