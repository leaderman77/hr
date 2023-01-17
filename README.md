## Cradle HR system
- [minicondani](https://docs.conda.io/en/latest/miniconda.html) o'rnating
- Repo boshidan (root) quyidagilarni qiling:
    ```shell
    conda install -c conda-forge mamba
    mamba env create -f environment.yml
    conda activate cradle_hr
    pip install -e .
    pre-commit install
    ```

### Repo strukturasi
Quyidagicha

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


### data haqida: [link](data/DATA.md)

### PR ochish qoidasi
- Biz main branchda ishlamaymiz. Hamma o'zi ishlaydigan branchni ochadi.
Branch nomi proyektga mos bo'lishi kerak.
Masalan, bu yerda: [link](https://github.com/orgs/cradle-uz/projects/2/views/1?layout=board)

- `hr-#1 repo strukturalash` topshiriq bo'lsa, quyidagicha branch qilinadi:

  ```shell
  git checkout -b "hr-1-repo-strukturalash"
  ```
- PR qilgan kishi albatta o'sha PRni tugatishga masul.
- Python kodlar dokumentatsiyasi numpy-style da bo'lish kerak. Misol uchun [link](https://python.plainenglish.io/how-to-write-numpy-style-docstrings-a092121403ba)
- commitga komment yozgada ham `"hr-1-komment"` qiling. Masalan: `git commit -m 'hr-1-komment'`
