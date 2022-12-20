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


## PR ochish qoidasi
Biz main branchda ishlamaymiz. Hamma o'zi ishlaydigan branchni ochadi. 
Branch nomi proyektga mos bo'lishi kerak. 
Masalan, bu yerda qilyotgan topshiriqlarimiz bor:
`https://github.com/orgs/cradle-uz/projects/1`

Men `ai-#1` topshiriqni olganman, shuning uchun quyidagicha branch ochaman: 

```shell
git checkout -b "[ai-1] repo strukturalash"
```


