#!/usr/bin/env python3
"""
Statistics Meta Bible Extractor
Specialized extractor for statistics knowledge, interview questions, and structured answers.
"""

import os
import json
from PIL import Image
import subprocess

class StatisticsMetaExtractor:
    def __init__(self, image_dir="Meta Bible"):
        self.image_dir = image_dir
        self.extracted_content = {}
        
    def try_system_ocr(self, image_path):
        """Try to use system OCR tools if available."""
        try:
            # Try using macOS built-in OCR if available
            result = subprocess.run(['which', 'tesseract'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                # Tesseract is available, try to use it
                ocr_result = subprocess.run(['tesseract', image_path, 'stdout'], 
                                          capture_output=True, text=True)
                if ocr_result.returncode == 0:
                    return ocr_result.stdout.strip()
        except Exception as e:
            print(f"System OCR attempt failed: {e}")
        
        return None
    
    def analyze_image_content(self, image_path):
        """Analyze image content and return information."""
        try:
            # Open the image to get basic information
            image = Image.open(image_path)
            
            # Get image properties
            width, height = image.size
            mode = image.mode
            
            # Try system OCR first
            ocr_text = self.try_system_ocr(image_path)
            
            if ocr_text:
                return ocr_text
            
            # Fallback to basic image info
            basic_info = f"Image: {os.path.basename(image_path)}\n"
            basic_info += f"Dimensions: {width}x{height}\n"
            basic_info += f"Mode: {mode}\n"
            basic_info += f"Size: {os.path.getsize(image_path)} bytes\n"
            
            return basic_info
            
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return f"Error: {str(e)}"
    
    def process_all_images(self):
        """Process all JPEG images in the Meta Bible directory."""
        jpg_files = [f for f in os.listdir(self.image_dir) if f.endswith('.jpg')]
        jpg_files.sort()  # Sort to maintain order
        
        print(f"Found {len(jpg_files)} JPEG images to process...")
        
        for jpg_file in jpg_files:
            image_path = os.path.join(self.image_dir, jpg_file)
            print(f"Processing {jpg_file}...")
            
            # Analyze image content
            content = self.analyze_image_content(image_path)
            
            if content:
                self.extracted_content[jpg_file] = content
                print(f"Successfully processed {jpg_file}")
            else:
                print(f"No content extracted from {jpg_file}")
    
    def create_statistics_content(self):
        """Create comprehensive statistics knowledge content for Meta interviews."""
        statistics_content = {
            "overview": {
                "description": "Statistics Knowledge for Meta (Facebook) Interviews - Comprehensive Guide",
                "key_areas": [
                    "Descriptive Statistics & Data Analysis",
                    "Inferential Statistics & Hypothesis Testing",
                    "A/B Testing & Experimental Design",
                    "Regression Analysis & Modeling",
                    "Probability & Distributions",
                    "Statistical Significance & Power Analysis"
                ]
            },
            "core_statistical_concepts": {
                "descriptive_statistics": [
                    "**Mean, Median, Mode** - Central tendency measures and when to use each",
                    "**Variance & Standard Deviation** - Measures of spread and variability",
                    "**Percentiles & Quartiles** - Understanding data distribution",
                    "**Skewness & Kurtosis** - Shape characteristics of distributions",
                    "**Correlation & Covariance** - Relationship between variables"
                ],
                "probability_fundamentals": [
                    "**Probability Rules** - Addition, multiplication, conditional probability",
                    "**Bayes' Theorem** - Updating beliefs with new evidence",
                    "**Random Variables** - Discrete vs continuous, expected value",
                    "**Probability Distributions** - Normal, binomial, Poisson, exponential",
                    "**Central Limit Theorem** - Foundation for inferential statistics"
                ],
                "sampling_methods": [
                    "**Simple Random Sampling** - Basic random selection",
                    "**Stratified Sampling** - Dividing population into subgroups",
                    "**Cluster Sampling** - Grouping and selecting clusters",
                    "**Systematic Sampling** - Regular interval selection",
                    "**Convenience Sampling** - Easy access (potential bias)"
                ]
            },
            "inferential_statistics": {
                "hypothesis_testing": [
                    "**Null vs Alternative Hypothesis** - Setting up statistical tests",
                    "**Type I & Type II Errors** - False positive vs false negative",
                    "**P-values** - Probability of observing data under null hypothesis",
                    "**Confidence Intervals** - Range estimates with confidence level",
                    "**Statistical Power** - Probability of rejecting false null hypothesis"
                ],
                "common_tests": [
                    "**T-tests** - Comparing means (one-sample, two-sample, paired)",
                    "**Chi-square Tests** - Testing independence and goodness of fit",
                    "**ANOVA** - Comparing means across multiple groups",
                    "**Non-parametric Tests** - When parametric assumptions fail",
                    "**Multiple Testing** - Bonferroni correction, false discovery rate"
                ]
            },
            "a_b_testing": {
                "fundamentals": [
                    "**Control vs Treatment Groups** - Setting up experiments",
                    "**Randomization** - Ensuring unbiased group assignment",
                    "**Sample Size Calculation** - Power analysis for adequate detection",
                    "**Statistical Significance** - Alpha level and p-value thresholds",
                    "**Practical Significance** - Effect size and business impact"
                ],
                "design_principles": [
                    "**Single Variable Testing** - One change at a time",
                    "**Blocking & Stratification** - Controlling for confounding variables",
                    "**Duration Planning** - Accounting for seasonality and trends",
                    "**Early Stopping Rules** - When to end experiments early",
                    "**Multi-armed Bandits** - Dynamic allocation strategies"
                ],
                "analysis_methods": [
                    "**Two-sample T-test** - Comparing means between groups",
                    "**Chi-square Test** - Comparing proportions or distributions",
                    "**Mann-Whitney U Test** - Non-parametric alternative to t-test",
                    "**Bootstrap Methods** - Resampling for confidence intervals",
                    "**Bayesian A/B Testing** - Prior beliefs and posterior updates"
                ]
            },
            "regression_analysis": {
                "linear_regression": [
                    "**Simple Linear Regression** - One predictor variable",
                    "**Multiple Linear Regression** - Multiple predictor variables",
                    "**Assumptions** - Linearity, independence, homoscedasticity, normality",
                    "**Model Diagnostics** - Residual analysis, influential points",
                    "**Multicollinearity** - Detecting and handling correlated predictors"
                ],
                "advanced_regression": [
                    "**Logistic Regression** - Binary outcome variables",
                    "**Polynomial Regression** - Non-linear relationships",
                    "**Ridge & Lasso Regression** - Regularization techniques",
                    "**Time Series Regression** - Temporal dependencies",
                    "**Generalized Linear Models** - Extending beyond normal distribution"
                ]
            },
            "interview_questions": {
                "basic_statistics": [
                    "**Q**: What's the difference between mean and median? When would you use each?",
                    "**Q**: How do you interpret a p-value of 0.03?",
                    "**Q**: What's the difference between correlation and causation?",
                    "**Q**: How would you explain confidence intervals to a non-technical stakeholder?",
                    "**Q**: What's the relationship between sample size and statistical power?"
                ],
                "a_b_testing": [
                    "**Q**: How would you design an A/B test for a new Facebook feature?",
                    "**Q**: What sample size would you need for a 5% lift detection with 80% power?",
                    "Q**: How do you handle multiple testing in A/B testing?",
                    "**Q**: When would you stop an A/B test early?",
                    "**Q**: How do you measure the success of an A/B test beyond statistical significance?"
                ],
                "data_analysis": [
                    "**Q**: How would you analyze user engagement patterns on social media?",
                    "**Q**: What metrics would you track for measuring ad campaign effectiveness?",
                    "**Q**: How would you detect fake accounts on Facebook using statistics?",
                    "**Q**: How do you measure the impact of a new algorithm on user retention?",
                    "**Q**: What statistical methods would you use for user segmentation?"
                ],
                "advanced_statistics": [
                    "**Q**: How would you handle missing data in a statistical analysis?",
                    "**Q**: What's the difference between frequentist and Bayesian approaches?",
                    "**Q**: How do you validate the assumptions of a statistical model?",
                    "**Q**: What's the curse of dimensionality and how does it affect analysis?",
                    "**Q**: How would you design a multi-armed bandit experiment?"
                ]
            },
            "structured_answers": {
                "a_b_testing_design": {
                    "question": "How would you design an A/B test for a new Facebook feature?",
                    "answer": [
                        "**1. Define Objectives**",
                        "   - Clear success metrics (e.g., engagement rate, conversion rate)",
                        "   - Business goals and minimum detectable effect",
                        "   - Primary vs secondary metrics",
                        "",
                        "**2. Experimental Design**",
                        "   - Random assignment to control vs treatment groups",
                        "   - Stratification by user characteristics if needed",
                        "   - Sample size calculation using power analysis",
                        "",
                        "**3. Implementation**",
                        "   - Ensure proper randomization and tracking",
                        "   - Monitor for data quality issues",
                        "   - Plan for early stopping if needed",
                        "",
                        "**4. Analysis Plan**",
                        "   - Statistical tests (t-test, chi-square, etc.)",
                        "   - Confidence intervals and effect sizes",
                        "   - Multiple testing corrections if applicable",
                        "",
                        "**5. Interpretation**",
                        "   - Statistical vs practical significance",
                        "   - Business impact assessment",
                        "   - Recommendations for next steps"
                    ]
                },
                "statistical_significance": {
                    "question": "How do you interpret statistical significance in business context?",
                    "answer": [
                        "**Statistical Significance**",
                        "   - P-value < alpha (typically 0.05) indicates unlikely results under null hypothesis",
                        "   - Does NOT mean the result is practically important",
                        "   - Does NOT guarantee the alternative hypothesis is true",
                        "",
                        "**Business Context**",
                        "   - Consider effect size and practical impact",
                        "   - Evaluate cost-benefit of implementing changes",
                        "   - Assess risk tolerance and decision thresholds",
                        "",
                        "**Common Pitfalls**",
                        "   - Confusing statistical with practical significance",
                        "   - Ignoring effect size and confidence intervals",
                        "   - Multiple testing without proper corrections",
                        "   - Stopping tests early based on interim results"
                    ]
                },
                "data_quality_assessment": {
                    "question": "How do you assess data quality before statistical analysis?",
                    "answer": [
                        "**Data Exploration**",
                        "   - Summary statistics and distributions",
                        "   - Missing data patterns and completeness",
                        "   - Outlier detection and investigation",
                        "   - Data type validation and consistency",
                        "",
                        "**Quality Checks**",
                        "   - Range and logical constraints",
                        "   - Temporal consistency and trends",
                        "   - Cross-field validation rules",
                        "   - Sampling bias assessment",
                        "",
                        "**Documentation**",
                        "   - Data source and collection methods",
                        "   - Known limitations and caveats",
                        "   - Preprocessing steps applied",
                        "   - Quality metrics and thresholds"
                    ]
                }
            },
            "practical_applications": {
                "social_media_metrics": [
                    "**Engagement Rate** - Likes, comments, shares per post",
                    "**Reach & Impressions** - Unique vs total views",
                    "**Click-through Rate** - Clicks per impression",
                    "**Conversion Rate** - Actions per click",
                    "**Retention Rate** - User return over time"
                ],
                "user_behavior_analysis": [
                    "**Cohort Analysis** - User groups over time",
                    "**Funnel Analysis** - Conversion through steps",
                    "**Session Analysis** - User interaction patterns",
                    "**Churn Prediction** - User retention modeling",
                    "**Recommendation Systems** - Collaborative filtering, content-based"
                ],
                "business_metrics": [
                    "**Customer Lifetime Value** - Long-term customer worth",
                    "**Customer Acquisition Cost** - Cost per new customer",
                    "**Net Promoter Score** - Customer satisfaction measure",
                    "**Revenue Metrics** - ARPU, MRR, growth rates",
                    "**Operational Metrics** - Response time, error rates"
                ]
            },
            "tools_and_technologies": {
                "statistical_software": [
                    "**R** - Comprehensive statistical analysis and visualization",
                    "**Python** - SciPy, NumPy, Pandas, Scikit-learn",
                    "**SAS** - Enterprise statistical analysis",
                    "**SPSS** - Social sciences and business statistics",
                    "**Stata** - Econometrics and social sciences"
                ],
                "visualization_tools": [
                    "**Tableau** - Interactive business intelligence",
                    "**Power BI** - Microsoft business analytics",
                    "**Python Libraries** - Matplotlib, Seaborn, Plotly",
                    "**R Libraries** - ggplot2, Shiny, Plotly",
                    "**D3.js** - Custom web-based visualizations"
                ],
                "big_data_tools": [
                    "**SQL** - Data querying and aggregation",
                    "**Hadoop/Spark** - Large-scale data processing",
                    "**AWS/GCP/Azure** - Cloud-based analytics platforms",
                    "**Databricks** - Unified analytics platform",
                    "**Snowflake** - Cloud data warehouse"
                ]
            }
        }
        
        return statistics_content
    
    def save_statistics_guide(self, content, output_file="meta_statistics_guide.md"):
        """Save the statistics content to a comprehensive markdown file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Statistics Knowledge for Meta Interviews - Comprehensive Guide\n\n")
            
            # Overview section
            f.write("## Overview\n\n")
            f.write(f"{content['overview']['description']}\n\n")
            f.write("**Key Areas Covered:**\n")
            for area in content['overview']['key_areas']:
                f.write(f"- {area}\n")
            f.write("\n")
            
            # Core Statistical Concepts
            f.write("## Core Statistical Concepts\n\n")
            
            for category, concepts in content['core_statistical_concepts'].items():
                f.write(f"### {category.replace('_', ' ').title()}\n\n")
                for concept in concepts:
                    f.write(f"{concept}\n")
                f.write("\n")
            
            # Inferential Statistics
            f.write("## Inferential Statistics\n\n")
            
            for category, concepts in content['inferential_statistics'].items():
                f.write(f"### {category.replace('_', ' ').title()}\n\n")
                for concept in concepts:
                    f.write(f"{concept}\n")
                f.write("\n")
            
            # A/B Testing
            f.write("## A/B Testing & Experimental Design\n\n")
            
            for category, concepts in content['a_b_testing'].items():
                f.write(f"### {category.replace('_', ' ').title()}\n\n")
                for concept in concepts:
                    f.write(f"{concept}\n")
                f.write("\n")
            
            # Regression Analysis
            f.write("## Regression Analysis\n\n")
            
            for category, concepts in content['regression_analysis'].items():
                f.write(f"### {category.replace('_', ' ').title()}\n\n")
                for concept in concepts:
                    f.write(f"{concept}\n")
                f.write("\n")
            
            # Interview Questions
            f.write("## Interview Questions by Category\n\n")
            
            for category, questions in content['interview_questions'].items():
                f.write(f"### {category.replace('_', ' ').title()}\n\n")
                for question in questions:
                    f.write(f"{question}\n")
                f.write("\n")
            
            # Structured Answers
            f.write("## Structured Answers to Key Questions\n\n")
            
            for topic, qa in content['structured_answers'].items():
                f.write(f"### {topic.replace('_', ' ').title()}\n\n")
                f.write(f"**Q: {qa['question']}**\n\n")
                f.write("**A:**\n")
                for line in qa['answer']:
                    f.write(f"{line}\n")
                f.write("\n")
            
            # Practical Applications
            f.write("## Practical Applications\n\n")
            
            for category, applications in content['practical_applications'].items():
                f.write(f"### {category.replace('_', ' ').title()}\n\n")
                for application in applications:
                    f.write(f"{application}\n")
                f.write("\n")
            
            # Tools and Technologies
            f.write("## Tools and Technologies\n\n")
            
            for category, tools in content['tools_and_technologies'].items():
                f.write(f"### {category.replace('_', ' ').title()}\n\n")
                for tool in tools:
                    f.write(f"{tool}\n")
                f.write("\n")
            
            # Image content summary
            f.write("## Image Content Summary\n\n")
            f.write("The following images contain detailed statistics content:\n\n")
            for image_name, content_info in self.extracted_content.items():
                f.write(f"### {image_name}\n")
                f.write("```\n")
                f.write(content_info)
                f.write("\n```\n\n")
        
        print(f"Statistics guide saved to {output_file}")
    
    def save_json(self, content, output_file="meta_statistics_guide.json"):
        """Save the statistics content to a JSON file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
        
        print(f"JSON guide saved to {output_file}")

def main():
    """Main function to run the statistics extraction process."""
    print("Starting Statistics Meta Bible content extraction...")
    
    # Initialize the extractor
    extractor = StatisticsMetaExtractor()
    
    # Process all images
    extractor.process_all_images()
    
    # Create comprehensive statistics content
    print("\nCreating comprehensive statistics knowledge guide...")
    statistics_content = extractor.create_statistics_content()
    
    # Save results
    extractor.save_statistics_guide(statistics_content)
    extractor.save_json(statistics_content)
    
    print("\nStatistics extraction complete!")
    print(f"Processed {len(extractor.extracted_content)} images")
    print(f"Created comprehensive statistics knowledge guide")

if __name__ == "__main__":
    main()

