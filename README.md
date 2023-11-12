## Cradle HR system
- [minicondani](https://docs.conda.io/en/latest/miniconda.html) o'rnating
- Repo boshidan (root) quyidagilarni qiling:
    ```shell
    conda install -c conda-forge mamba
    mamba env create -f environment_fix.yml
    conda activate cradle_hr
    pip install -e .
    pre-commit install
    ```

### Repo structure
As follows

    ├── .gitignore
    ├── README.md
    ├── LICENSE.md
    ├── environment.yml
    ├── setup.py
    ├── src # funksional kodlar
    │   └── utils.py
    ├── models
    ├── docs # dokumentlar
    ├── tests # testlar
    ├── scripts # src dan foydalanib qilingan kodlar
        └── notebooks
    ├── client-api # klientga oid kodlar
    └── data # rasmlar, videolar

### Testing

From the root of the project, run it in a terminal:

```shell
pytest -vv -p no:warnings
```

For instance:

```shell
~/work/cradle/git/hr$ pytest -vv -p no:warnings
```

You should get an output similar to the following

```shell
...
collected 2 items

tests/test_detection.py::test_det PASSED                                                                                                                                                                                         [ 50%]
tests/test_embedding.py::test_embedding PASSED
...
```


`pytest` went to the `tests` folder and tested the codes.

### about data: [link](data/DATA.md)

### PR opening rule
- We do not work in the main branch. Everyone opens a branch that works for them.
The branch name must match the project.
For example, here: [link](https://github.com/orgs/cradle-uz/projects/2/views/1?layout=board)

- If `hr-#1 repo strukturalash` is a task, branch as follows:

   ```shell
   git checkout -b "hr-1-repo-structuring"
   ```
- The person who made a PR is definitely responsible for finishing that PR.
- Python code documentation should be in numpy-style. For example [link](https://python.plainenglish.io/how-to-write-numpy-style-docstrings-a092121403ba)
- When writing a comment to the commit, make `"hr-1-comment"'. For example: `git commit -m 'hr-1-comment'`
