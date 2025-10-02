# Meta Bible - Statistics Knowledge Guide

## Overview

**Statistics Knowledge for Meta Interviews**

Essential statistics concepts and methods commonly tested in Meta data science and analytics interviews

**Why Important**: Statistics is fundamental for A/B testing, data analysis, and making data-driven decisions at Meta

## 📊 Fundamental Concepts

### Descriptive Statistics
- **Mean (Average)**: Sum of all values divided by count - sensitive to outliers
- **Median**: Middle value when data is sorted - robust to outliers
- **Mode**: Most frequent value - useful for categorical data
- **Standard Deviation**: Measure of data spread around the mean
- **Variance**: Square of standard deviation - used in calculations
- **Range**: Difference between maximum and minimum values
- **Quartiles**: 25th, 50th (median), 75th percentiles
- **IQR (Interquartile Range)**: Q3 - Q1, used to identify outliers

### Probability Basics
- **Probability**: Likelihood of an event occurring (0 to 1)
- **Independent Events**: P(A and B) = P(A) × P(B)
- **Mutually Exclusive**: P(A or B) = P(A) + P(B)
- **Conditional Probability**: P(A|B) = P(A and B) / P(B)
- **Bayes' Theorem**: P(A|B) = P(B|A) × P(A) / P(B)
- **Random Variables**: Variables with probabilistic outcomes
- **Expected Value**: Weighted average of possible outcomes
- **Variance of RV**: E[(X - μ)²] where μ is expected value

## 📈 Probability Distributions

### Normal Distribution
- **Bell-shaped curve** - symmetric around mean
- **68-95-99.7 Rule**: 68% within 1σ, 95% within 2σ, 99.7% within 3σ
- **Z-score**: (X - μ) / σ - how many standard deviations from mean
- **Central Limit Theorem**: Sample means approach normal distribution
- **Properties**: Mean = median = mode, symmetric, asymptotic tails

### Other Important Distributions
- **Binomial**: Count of successes in n independent trials
- **Poisson**: Count of events in fixed time/space interval
- **Exponential**: Time between events in Poisson process
- **Uniform**: Equal probability across range
- **Chi-square**: Sum of squared standard normal variables
- **t-distribution**: Similar to normal but heavier tails (small samples)
- **F-distribution**: Ratio of chi-square distributions

## 🔍 Hypothesis Testing

### Core Concepts
- **Null Hypothesis (H₀)**: Default assumption to be tested
- **Alternative Hypothesis (H₁)**: What we want to prove
- **Significance Level (α)**: Probability of Type I error (rejecting true H₀)
- **Power**: Probability of rejecting false H₀ (1 - β)
- **Type I Error**: Rejecting true null hypothesis (false positive)
- **Type II Error**: Failing to reject false null hypothesis (false negative)
- **P-value**: Probability of observing data as extreme as current data if H₀ is true

### Common Tests
- **t-test**: Compare means (one-sample, two-sample, paired)
- **Z-test**: Large sample size, known population variance
- **Chi-square test**: Test independence or goodness of fit
- **ANOVA**: Compare means across multiple groups
- **Mann-Whitney U**: Non-parametric alternative to t-test
- **Wilcoxon signed-rank**: Non-parametric paired test

### Interpretation
- **P < α**: Reject null hypothesis (statistically significant)
- **P ≥ α**: Fail to reject null hypothesis (not significant)
- **Effect Size**: Practical significance beyond statistical significance
- **Confidence Intervals**: Range containing true parameter with confidence level
- **Multiple Testing**: Bonferroni correction for multiple comparisons

## 🧪 A/B Testing

### Fundamentals
- **Control Group**: Baseline group (existing experience)
- **Treatment Group**: New experience being tested
- **Randomization**: Ensures groups are comparable
- **Sample Size**: Determines statistical power and significance
- **Primary Metric**: Main success measure (e.g., conversion rate)
- **Guardrail Metrics**: Safety measures to prevent negative impact

### Statistical Analysis
- **Statistical Power**: Probability of detecting true effect (typically 80%)
- **Minimum Detectable Effect (MDE)**: Smallest effect size you can reliably detect
- **Confidence Level**: Usually 95% (α = 0.05)
- **Sample Size Calculation**: Based on power, MDE, and baseline rate
- **Early Stopping**: Can lead to inflated false positive rates
- **Multiple Testing**: Test multiple variants with proper corrections

### Interpretation
- **Lift**: Percentage improvement over control
- **Confidence Interval**: Range of possible true effects
- **Practical Significance**: Is the effect large enough to matter?
- **External Validity**: Does the result generalize to other contexts?
- **Causal Inference**: Correlation vs causation considerations

## 📉 Regression Analysis

### Linear Regression
- **Simple Linear**: Y = β₀ + β₁X + ε
- **Multiple Linear**: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε
- **Coefficients**: β values represent change in Y per unit change in X
- **R-squared**: Proportion of variance explained by model
- **Adjusted R-squared**: R² adjusted for number of predictors
- **Residuals**: Differences between predicted and actual values
- **Assumptions**: Linearity, independence, homoscedasticity, normality

### Model Evaluation
- **F-test**: Overall model significance
- **t-test**: Individual coefficient significance
- **Residual Analysis**: Check model assumptions
- **Cross-validation**: Assess model generalization
- **Overfitting**: Model performs well on training but poorly on new data
- **Regularization**: Ridge, Lasso to prevent overfitting

## 🚀 Practical Applications

### Meta-Specific Examples
- **User Engagement Metrics**: DAU, WAU, MAU, session duration
- **Content Performance**: Click-through rates, engagement rates
- **Ad Effectiveness**: Conversion rates, cost per acquisition
- **Feature Impact**: Before/after analysis, cohort analysis
- **User Segmentation**: Cluster analysis, RFM analysis
- **Predictive Modeling**: User churn, content recommendation

### Common Pitfalls
- **Selection Bias**: Non-random sampling
- **Confounding Variables**: Variables that affect both cause and effect
- **Regression to Mean**: Extreme values tend to move toward average
- **Simpson's Paradox**: Trend disappears when data is grouped
- **Multiple Testing**: Increased chance of false positives
- **P-hacking**: Data dredging to find significant results

## ❓ Interview Questions

### Conceptual Questions
- What's the difference between mean and median? When would you use each?
- Explain the Central Limit Theorem and why it's important
- What is statistical power and how does it relate to sample size?
- How would you design an A/B test for a new Facebook feature?
- What's the difference between correlation and causation?
- How do you handle multiple testing in A/B testing?

### Calculation Questions
- Calculate the mean, median, and standard deviation for this dataset
- What's the probability of getting exactly 3 heads in 5 coin flips?
- Calculate the 95% confidence interval for this sample mean
- Perform a t-test to compare these two groups
- Calculate the sample size needed for this A/B test
- Interpret this regression output and identify significant variables

### Interpretation Questions
- This A/B test shows p=0.03. What does this mean?
- The confidence interval is [-2%, +5%]. How do you interpret this?
- R-squared is 0.15. Is this a good model?
- The effect size is small but statistically significant. What's your recommendation?
- How would you explain these results to a non-technical stakeholder?

## 📝 Key Formulas

### Descriptive Statistics
- **Mean**: μ = Σxᵢ/n
- **Variance**: σ² = Σ(xᵢ - μ)²/n
- **Standard Deviation**: σ = √σ²
- **Z-score**: z = (x - μ)/σ
- **Correlation**: r = Σ((xᵢ - x̄)(yᵢ - ȳ))/√(Σ(xᵢ - x̄)²Σ(yᵢ - ȳ)²)

### Inferential Statistics
- **t-statistic**: t = (x̄ - μ₀)/(s/√n)
- **Confidence Interval**: x̄ ± t₍α/2, n-1₎ × (s/√n)
- **Sample Size**: n = (2σ²(z₍α/2₎ + z₍β₎)²)/δ²
- **Chi-square**: χ² = Σ((O - E)²/E)
- **F-statistic**: F = MSB/MSW (between/within group variance)

## 📸 Image Content Summary

The following images contain detailed statistics content:

### IMG_9016.jpg
```
Image processed: 4032x3024 - Statistics content detected
```

### IMG_9017.jpg
```
Image processed: 4032x3024 - Statistics content detected
```

### IMG_9018.jpg
```
Image processed: 4032x3024 - Statistics content detected
```

### IMG_9019.jpg
```
Image processed: 4032x3024 - Statistics content detected
```

### IMG_9020.jpg
```
Image processed: 4032x3024 - Statistics content detected
```

### IMG_9021.jpg
```
Image processed: 4032x3024 - Statistics content detected
```

### IMG_9022.jpg
```
Image processed: 4032x3024 - Statistics content detected
```

### IMG_9023.jpg
```
Image processed: 4032x3024 - Statistics content detected
```

### IMG_9024.jpg
```
Image processed: 4032x3024 - Statistics content detected
```

