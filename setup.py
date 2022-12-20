import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cradle-hr",
    version="0.0.1",
    author="cradle",
    description="HR system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cradle-uz/ai",
    project_urls={
        "Bug Tracker": "https://github.com/cradle-uz/ai/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="workflow"),
    python_requires="==3.9",
)