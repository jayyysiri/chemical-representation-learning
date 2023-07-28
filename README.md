# Chemical Representation Learning

### About
This repository contains the code for experimenting with various machine learning methods for chemistry. The current focus is on predicting yield by learning representations from chemical SMILES strings.

All instances of model usage and predictions should be done under `src/analysis/`.

### Repository Structure (top-level)
    .
    ├── .github/workflows       # GitHub Actions (CI/CD)
    ├── datasets                # Datasets
    ├── src                     # Source files (utils, representations, etc.)
    ├── tests                   # Automated tests
    ├── environment.yml         # Set up environment
    ├── LICENSE
    └── README.md

### How To Contribute
To contribute, please create a pull request. Your code should be auto-tested and reviewed before merging. 

Whenever possible, make sure that:
- Your code is well documented. All methods should have docstrings indicating what the function does, input and output data types, as well as in-line comments wherever needed.
- All methods you write are well-tested. (See the `tests/` folder)
