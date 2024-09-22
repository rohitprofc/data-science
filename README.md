# Data Science Experiments - README

## Project Overview

This repository contains a series of experiments and implementations related to data science tasks using various datasets. The experiments focus on different machine learning models, statistical methods, and data analysis techniques. The structure and flow of the experiments are designed to provide hands-on experience in exploring and analyzing datasets through real-world tasks.

### Datasets Used

- **`advertising.csv`**: Contains advertising budgets (TV, radio, newspaper) and the corresponding sales (in thousands of units).
- **`collegedata.csv`**: Information about 777 universities/colleges in the US with various attributes (quantitative and categorical).
- **`smarket.csv`**: Daily percentage returns for S&P 500 over a 5-year period, including lag variables and trading volume.

### Experiments

Below is a brief description of the experiments available in the repository:

#### 1. **Simple Linear Regression on Advertising Data**
   - **File**: `Exp_1.ipynb`
   - This experiment applies a **least squares model** to estimate the number of units sold based on the TV advertising budget. The regression provides the coefficient estimates for a simple linear model.

#### 2. **Statistical Measures for the Least Squares Model**
   - **File**: `Exp_2.ipynb`
   - Computes key statistical metrics: **t-statistic, Residual Standard Error (RSE), F-statistic**, and **Residual Sum of Squares (RSS)** for the simple linear regression model of Experiment 1.

#### 3. **K-Nearest Neighbors (KNN) on S&P 500 Data**
   - **File**: `Exp_3.ipynb`
   - Uses **K-Nearest Neighbors (K = 3)** with `Direction` as the response variable and the lag variables along with volume as predictors. The aim is to identify statistically significant predictors.

#### 4. **Confusion Matrix and Model Evaluation (KNN)**
   - **File**: `Exp_4.ipynb`
   - Constructs a **confusion matrix** to evaluate the KNN model's prediction performance and compute the overall accuracy. Analyzes the types of errors made by the model.

#### 5. **Model Selection and Information Criteria**
   - **File**: `Exp_5.ipynb`
   - Calculates **Mallow’s Cp, Akaike Information Criterion (AIC), Adjusted R²**, and **Bayesian Information Criterion (BIC)** for model evaluation and selection.

#### 6. **Exploratory Data Analysis on College Data**
   - **File**: `Exp_6.ipynb`
   - Performs **exploratory data analysis (EDA)** on the `collegedata.csv` dataset by generating histograms with varying bin sizes for different quantitative variables.

#### 7. **College Data Summary and Insights**
   - **File**: `Exp_7.ipynb`
   - Continues the analysis from Experiment 6 by summarizing key findings and patterns observed from the `collegedata.csv` dataset.

#### 8. **Correlation Analysis on College Data**
   - **File**: `Exp_8.ipynb`
   - Computes **Pearson, Spearman’s rho**, and **Kendall’s tau** correlation coefficients for different pairs of quantitative variables from the `collegedata.csv` dataset.

#### 9. **Hypothesis Testing**
   - **File**: `Exp_9.ipynb`
   - Conducts various hypothesis tests: **Student’s t-test, paired t-test, U-test**, and tests for **correlation** and **covariance** to assess relationships between variables in the `collegedata.csv` dataset.

#### 10. **Eigenvalues and Eigenvectors Computation**
   - **File**: `Exp_10.ipynb`
   - Demonstrates programming to compute **Eigenvalues and Eigenvectors** for matrix decomposition and analysis.

#### 11. **QR Decomposition, SVD, and PCA**
   - **File**: `Exp_11.ipynb`
   - Implements **QR decomposition, Singular Value Decomposition (SVD)**, and **Principal Component Analysis (PCA)** to perform dimensionality reduction and matrix factorizations.

#### 12. **Support Vector Machine (SVM) Classification**
   - **File**: `Exp_12.ipynb`
   - Computes the discriminating **hyperplane using Support Vector Machine (SVM)** for a set of objects in a 2D space with binary classification labels (+1, -1).

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd data-science
   ```

2. **Install Dependencies**
   You may need the following Python packages:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn
   ```

3. **Running Jupyter Notebooks**
   Launch Jupyter Notebook to explore the experiments:
   ```bash
   jupyter notebook
   ```

4. **Datasets**
   The datasets are located in the `dataset/` folder. The required datasets for each experiment are loaded within the corresponding Jupyter notebooks.

### Additional Files

- **`create_multiple_files.py`**: This script is a utility to generate multiple files dynamically.
- **Other Notebooks**: `advertising.ipynb`, `weather.ipynb` located in the `other/` directory provide additional examples of analyses on `advertising.csv` and `weather.csv` datasets.

### License

This project is open-source and available under the MIT License.

### Contact

For any issues, feel free to open a GitHub issue or reach out to the project maintainer.

---

This README file provides a comprehensive overview of the structure and purpose of the repository along with detailed explanations of each experiment.