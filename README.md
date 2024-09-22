# Data Science 

Welcome to the Data Science repository! This repository contains various experiments and analyses utilizing different datasets related to advertising, super market returns, and college data. Below, you will find an overview of the directory structure and a list of experiments conducted.

## List of Experiments

### Advertising Data Analysis
The **Advertising data** contains sales (in thousands of units) for a product as a function of advertising budgets (in thousands of dollars) across TV, radio, and newspaper media.

1. **Least Squares Regression**: Apply a least squares model to regress the number of units sold on the TV advertising budget for coefficient estimates in simple linear regression.
2. **Statistical Metrics**: Compute t-statistic, residual standard error, F-statistic, and residual sum of squares (RSS) errors.

### Stock Market Analysis
Using the **Smart data** of daily percentage returns for the S&P 500 over a 5-year period:

3. **KNN Analysis**: Perform KNN with K = 3, using `Direction` as the response and the five lag variables plus `Volume` as predictors. Determine which predictors are statistically significant.
4. **Confusion Matrix**: Compute the confusion matrix and the overall fraction of correct predictions. Explain the insights gained from the confusion matrix regarding KNN's mistakes.
5. **Model Evaluation Metrics**: Compute Mallow’s Cp, Akaike Information Criterion (AIC), Adjusted R-Squared, and Bayesian Information Criterion (BIC).

### College Data Exploration
The **College dataset** contains various variables for 777 universities and colleges in the US.

6. **Histograms**: Produce histograms with varying numbers of bins for several quantitative variables.
7. **Data Summary**: Explore the data further and provide a brief summary of findings.
8. **Correlation Analysis**: Perform Pearson product moment correlation, Spearman rho correlation, and Kendall’s tau.
9. **Hypothesis Testing**: Conduct simple hypothesis testing, including student’s t-test, paired t-test, U test, correlation, covariance, and tests for association.
10. **Eigenvalues and Eigenvectors**: Implement programming for computing eigenvalues and eigenvectors.
11. **Matrix Decomposition**: Perform QR decomposition, Singular Value Decomposition (SVD), and Principal Component Analysis (PCA).
12. **SVM Analysis**: Compute the discriminating hyperplane using Support Vector Machines (SVM) for specified objects.

## Getting Started

To run the experiments, ensure you have the necessary packages installed. You can find the required packages listed in `requirements.txt`. To set up the environment, use:

```bash
pip install -r requirements.txt
```

## Contributions

Feel free to contribute to this project by adding new experiments or improving existing analyses. For any questions or suggestions, please open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
