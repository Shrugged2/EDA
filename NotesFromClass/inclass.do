**************
* Exam Template
* Purpose: Load housing data, analyze structure, run regressions, and interpret results
*****************************************************

* Set up a log file to record the session (optional but recommended)
cap log close
log using exam_analysis.log, replace

*****************************************************
* Load Data
*****************************************************
* Replace 'housing_data.dta' with the actual dataset file name
use "housing_data.dta", clear

*****************************************************
* Check dataset structure
*****************************************************
* Display variable storage types and labels
describe

* Summary statistics for numerical variables
summarize

* Detailed variable descriptions (e.g., unique values, missing values, etc.)
codebook

* Check for missing values in the dataset
misstable summarize

*****************************************************
* Understand the Nature of Data
*****************************************************
* Check whether the dataset is cross-sectional, time series, or panel data
* Cross-sectional: Single observation per unit (e.g., individuals, households)
* Time series: Data varies over time (e.g., stock prices, GDP growth)
* Panel data: Multiple observations per unit over time

* If panel data, identify panel variable and time variable
xtset, clear

* Check for time trends in a time series dataset (if applicable)
tsline y

*****************************************************
* Correlation Analysis
*****************************************************
* Pairwise correlation between dependent and independent variables
pwcorr y2 x1 x2 x3, sig

* Squaring the correlation coefficient to obtain R-squared
* Interpretation: R-squared measures the proportion of variance explained
local r2 = r(rho)^2

* Visual representation of correlation matrix
corrplot y2 x1 x2 x3

*****************************************************
* Regression Analysis
*****************************************************
* Simple linear regression: Regress Y on X1
regress y x1

* Multiple regression: Regress Y on X1, X2, X3
regress y x1 x2 x3

* Check for multicollinearity using Variance Inflation Factor (VIF)
vif

*****************************************************
* Model Selection & Interpretation
*****************************************************
* R-squared: Goodness of fit in OLS regression
* Log-likelihood: Used in maximum likelihood estimation models
* Pseudo R-squared: Used in logistic/probit regression

* Display R-squared
estat ic

* T-stats and P-values: Significance of coefficients
* T-stat = Coefficient / Standard Error
* P-value < 0.05 is typically considered significant

* Check residuals for normality and heteroscedasticity
diagreg

*****************************************************
* Confidence Intervals Calculation
*****************************************************
* Formula: Lower Bound = Coefficient - (1.96 * Std Error)
*          Upper Bound = Coefficient + (1.96 * Std Error)

* Generate confidence intervals manually
matrix list e(b)   // Coefficients
matrix list e(V)   // Variance-Covariance Matrix

* Confidence Interval Calculation for first predictor (example)
dis "Lower Bound: " _b[x1] - (1.96 * _se[x1])
dis "Upper Bound: " _b[x1] + (1.96 * _se[x1])

*****************************************************
* End of Do-File
*****************************************************
log close
