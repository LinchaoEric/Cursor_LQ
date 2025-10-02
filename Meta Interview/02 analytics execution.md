- [Analytical Execution](#analytical-execution)
  - [What can you expect?](#what-can-you-expect)
  - [How to Prep](#how-to-prep)
    - [Aspects of the Analytical Execution questions include:](#aspects-of-the-analytical-execution-questions-include)
    - [You will **NOT** be asked the following:](#you-will-not-be-asked-the-following)
- [Fake Account](#fake-account)
  - [Context](#context)
  - [Exact Questions and Model Answers](#exact-questions-and-model-answers)
    - [**Question 1**](#question-1)
    - [**Question 2**](#question-2)
    - [**Question 3**](#question-3)
    - [**Question 4**](#question-4)
  - [Why These Questions Align with Meta’s Analytical Execution](#why-these-questions-align-with-metas-analytical-execution)
  - [Key Takeaways for Candidates](#key-takeaways-for-candidates)
- [假新闻](#假新闻)
- [评论分布](#评论分布)
    - [**Comment Distribution Question**](#comment-distribution-question)
      - [**Context**](#context-1)
    - [**Question 1**](#question-1-1)
    - [**Question 2**](#question-2-1)
    - [**Question 3**](#question-3-1)
    - [**Question 4**](#question-4-1)
    - [**Question 5**](#question-5)
    - [**Bonus Question**](#bonus-question)
- [Feed里插广告](#feed里插广告)
    - [**Ads Impression Distribution Question**](#ads-impression-distribution-question)
      - [**Context**](#context-2)
    - [**Question 1**](#question-1-2)
    - [**Question 2**](#question-2-2)
    - [**Question 3**](#question-3-2)
    - [**Question 4**](#question-4-2)
    - [**Question 5**](#question-5-1)
    - [**Question 6**](#question-6)
    - [**Question 7**](#question-7)
    - [Question 8: **Probability of Users Seeing Back-to-Back Ads**](#question-8-probability-of-users-seeing-back-to-back-ads)
    - [**1. Scenario 1: Fixed Interval Ad Insertion**](#1-scenario-1-fixed-interval-ad-insertion)
    - [**2. Scenario 2: Random Ad Insertion**](#2-scenario-2-random-ad-insertion)
      - [**Probability Calculation**](#probability-calculation)
    - [**3. Example Calculation**](#3-example-calculation)
    - [**4. Summary**](#4-summary)
  - [When choosing an ad insertion strategy, balancing user experience and ad distribution fairness is crucial. Random insertion might lead to more back-to-back ads, potentially harming user experience.](#when-choosing-an-ad-insertion-strategy-balancing-user-experience-and-ad-distribution-fairness-is-crucial-random-insertion-might-lead-to-more-back-to-back-ads-potentially-harming-user-experience)
    - [**Takeaways**](#takeaways)

**[2024-10-28 Meta onsite 好像是新题](https://www.1point3acres.com/bbs/thread-1094505-1-1.html)**
AE: 视频推荐和分享，包含两道概率题。
**[【meta vo】 ](https://www.1point3acres.com/bbs/thread-1102657-1-1.html)**
ae: 一个搜索feature是不是successful有2个dimension来评估（relevancy,accuracy)，都是binary flag (1/0). 前面几问很简单，后面有一问我答的不太好（公式记错了，😢），说有两个model做的这个feature，各被100个人使用（1人1次)，一个有90人反馈说是successful，一个有85人反馈successful（数字可能记得不对，就这个意思），能不能说一个model强于另一个model？ 用已知的数据validate。
# Analytical Execution

## What can you expect?
In your Analytical Execution interview, your interviewer will assess your performance on 4 focus areas:

- **Creating Hypotheses**: Formulates assertions to test ideas that provide answers to business questions.
- **Quantitative Analysis**: Uses statistical code to carry out analyses ranging from correlations to multivariate analysis to measurement models.
- **Determining Goals & Success Metrics**: Identifies metrics that reflect operational success and inform business objectives.
- **Demonstrating Agility**: Proactively embraces change, manages through ambiguity, and is resilient in the face of challenges.

## How to Prep
In addition to reviewing the above information, these tips may be helpful as you prepare. 

### Aspects of the Analytical Execution questions include:
- Understanding hypotheses for launching new features.
- Considering and quantifying tradeoffs of a feature in terms of metrics.
- Elements of descriptive stats (mean/expected value, median, mode, percentiles).
- Common distributions such as binomial or normal distributions.
- The profile of real-world data.
- Law of Large Numbers, Central Limit Theorem, Linear Regression.
- Conditional probabilities, including Bayes’ Theorem.

### You will **NOT** be asked the following:
- Advanced stats/math concepts: calculus or advanced statistical/ML models.
- More complex distributions like the exponential, Weibull, Beta, etc.
- Contrived estimation problems (i.e., “How many golf balls fit in a 747”).

--- 
[2024-11-28 买它 VO 过经](https://www.1point3acres.com/bbs/thread-1100228-1-1.html)<br>
AE: Fake account - Straightforward Bayes' theorem questions with some questions about the metrics definition
[2024-02-22 Meta DSA VO](https://www.1point3acres.com/bbs/thread-1047008-1-1.html)  
统计问题偏多，user comment distribution长什么样（画图），然后分别标出mean, median, 和95th percentile在哪里。如果把一个app的用户分成10个小组，每个小组有10k用户，每个组分别的distribution长什么样（这题我猜是关于central limit theorem? ). 还问了standard deviation的公式。。。。

[2024-11-23 买它新鲜跪经 - DS - VO](https://www.1point3acres.com/bbs/thread-1099426-1-1.html)  
地里的老题目了，大致如下
日活用户的平均评论变多了， 因为机器人账户发了更多的评论。简单计算有多少机器人。然后讨论了怎么检测机器人。怎么去衡量是否成功，以及有什么影响。

# Fake Account 
[2024-11-20 买它 VO 新鲜出炉 细节+讨论+等结果](https://www.1point3acres.com/bbs/thread-1098942-1-1.html)  
5% 是fake account，fake account发的 friend frequent是authentic account的10倍，没别的信息了。  
1. P(fake|a friend request). Χ
2. P(at least one request is from fake account | 5 friend request)，算完面试官跟我跟我感慨了下fake的account还真是多啊！我说是啊。。。
3. 说有classifier，给了TP AND FN都是95%，然后用贝叶斯算一个数。套公式不难。算出来50%问我觉得这个classifier怎么样。我说一般，就是random的基本上。
4. 应该看什么metrics。我把跟unbalanced data set的classifier有关的知道的都说了。
本来只看了近期的题，面试前几天刷到了fake account感觉准备了，问的和地理的基本一样，数字小变了一下。感慨下自己的数学英语真是抓鸡，作为第二天的第一轮，脑子都是麻的。建议不要只看近期的常见题，最好把1-2年的题型都过一下。  

fake request是正常request10倍那个conditional probability。后来又问了fraud detect用模型95%正确率，实际由5%fraud account，算预测是fraud 前提下实际也是fraud的概率。都是原题。最后怎样再进一步validate模型预测出来的fraud真的是fraud。又是ab test问题。。


Below is a combined and reconstructed question context—plus the exact questions that were asked and detailed answers—as they might appear during a Meta Data Scientist (Analytics Execution) interview round focused on probability, statistics, and tradeoff decisions for launching new features. This synthesis is based on the shared details from the original prompts.

## Context

You are interviewing for a Data Scientist (Analytics) position at Meta. One of the interview sections focuses on **Analytical Execution** questions, which typically cover:

1. Understanding hypotheses for launching new features.
2. Considering and quantifying tradeoffs in terms of metrics.
3. Elements of descriptive stats (mean, median, mode, percentiles, expected values).
4. Common distributions such as the binomial or the normal distribution.
5. Profile of real-world data (skew, outliers, large-scale data issues).
6. Law of Large Numbers, Central Limit Theorem, Linear Regression (basic conceptual understanding).
7. Conditional probabilities, including Bayes’ Theorem.

**Note**: You will not be asked advanced math (e.g., calculus or advanced ML models), unusual distributions (e.g., exponential, Weibull, Beta), or “guesstimation” questions.

**Scenario**: You are presented with a problem regarding fake accounts on a social network:
- **5% of all accounts are fake.**
- **Fake accounts send 10× the number of friend requests compared to real (authentic) accounts.**

You are asked to compute probabilities and interpret a classifier’s performance in detecting or blocking fake accounts.

---

## Exact Questions and Model Answers

### **Question 1**  
**What is the probability that a given friend request comes from a fake account?**

**Context/Hint Provided by Interviewer**:
- 5% of users are fake (prior = 0.05).
- Fake users send friend requests at 10× the rate of real users.
- No other hidden assumptions or data.

**Answer Explanation**:
1. Define:
   - \( P(\text{Fake}) = 0.05 \): Proportion of fake users.
   - \( P(\text{Real}) = 0.95 \): Proportion of real users.
   - Let \( r \) be the baseline rate of friend requests sent by a real user.
   - Fake users send friend requests at a rate of \( 10r \).

2. Use Bayes’ Theorem:
   \[
   P(\text{Fake | Request}) = \frac{P(\text{Fake}) \cdot P(\text{Request | Fake})}{P(\text{Fake}) \cdot P(\text{Request | Fake}) + P(\text{Real}) \cdot P(\text{Request | Real})}
   \]

3. Substitute rates:
- \( P(\text{FR} \mid \text{Fake}) \propto 10 \lambda_R \).
- \( P(\text{FR} \mid \text{Real}) \propto \lambda_R \).
4. Simplify:
   \[
   P(\text{Fake | Request}) = \frac{0.05 \cdot 10r}{0.05 \cdot 10r + 0.95 \cdot r} = \frac{0.5}{0.5 + 0.95} = \frac{0.5}{1.45} \approx 0.345
   \]

**Result**: ~34.5% of friend requests are from fake accounts, despite only 5% of users being fake.

---

### **Question 2**  
**What is the probability that, out of 5 received friend requests, at least one is from a fake account?**

**Context/Hint Provided by Interviewer**:
- Builds on Question 1: \( P(\text{Fake | Request}) \approx 0.345 \).
- Each friend request is an independent trial.

**Answer Explanation**:
1. Probability of no fake requests in 5 trials:
   \[
   P(\text{No Fake}) = (1 - 0.345)^5
   \]

2. Probability of at least one fake:
   \[
   P(\text{At Least One Fake}) = 1 - P(\text{No Fake})
   \]

3. Substituting \( P(\text{Fake | Request}) \):
   \[
   P(\text{At Least One Fake}) = 1 - (1 - 0.345)^5 \approx 1 - 0.659 \approx 0.879
   \]

**Result**: ~87.9% chance that at least one of 5 friend requests is from a fake account.

---

### **Question 3**  
**假如我们开发了一个 classification model 来识别 bad account，在建模阶段我们发现它的 True Positive Rate 和 True Negative Rate 都是 95%，那么一个被模型判断为 bad 的 account 它确实是 bad 的概率是多少？（需要用贝叶斯公式）**

---

**Answer Explanation**:

1. **Clarify Metrics**:
   - \( \text{True Positive Rate (TPR)} = 95\% \): The probability the model correctly identifies a bad account as bad.
   - \( \text{True Negative Rate (TNR)} = 95\% \): The probability the model correctly identifies a good account as good.
   - \( \text{False Positive Rate (FPR)} = 1 - \text{TNR} = 5\% \): The probability the model incorrectly identifies a good account as bad.
   - Let \( P(\text{Bad}) = p \) (prior probability of bad accounts), and \( P(\text{Good}) = 1 - p \).

2. **Bayes’ Theorem**:
   To find \( P(\text{Bad} \mid \text{Model says Bad}) \):
   \[
   P(\text{Bad} \mid \text{Model says Bad}) = \frac{P(\text{Model says Bad} \mid \text{Bad}) \cdot P(\text{Bad})}{P(\text{Model says Bad})}.
   \]

   The total probability \( P(\text{Model says Bad}) \) is:
   \[
   P(\text{Model says Bad}) = P(\text{Model says Bad} \mid \text{Bad}) \cdot P(\text{Bad}) + P(\text{Model says Bad} \mid \text{Good}) \cdot P(\text{Good}).
   \]

3. **Substitute Values**:
   Substitute \( P(\text{Model says Bad} \mid \text{Bad}) = 0.95 \), \( P(\text{Model says Bad} \mid \text{Good}) = 0.05 \), and the priors:
   \[
   P(\text{Bad} \mid \text{Model says Bad}) = \frac{0.95p}{0.95p + 0.05(1 - p)}.
   \]

4. **Simplify**:
   \[
   P(\text{Bad} \mid \text{Model says Bad}) = \frac{0.95p}{0.9p + 0.05}.
   \]

5. **Example**:
   - Assume \( P(\text{Bad}) = 0.05 \) (5% of accounts are bad):
     \[
     P(\text{Bad} \mid \text{Model says Bad}) = \frac{0.95 \cdot 0.05}{0.9 \cdot 0.05 + 0.05} = \frac{0.0475}{0.045 + 0.05} = \frac{0.0475}{0.095} \approx 0.5.
     \]
   - The probability is **50%**, meaning that if the model flags an account as bad, there’s a 50% chance it’s actually bad.

6. **Interpretation**:
   - **Imbalanced Data Impact**: Despite the model's high TPR and TNR, the low prevalence of bad accounts (\( P(\text{Bad}) = 0.05 \)) leads to a high number of false positives dominating the predictions.
   - **Precision Issue**: A 50% posterior probability indicates the classifier is only slightly better than random guessing for flagged accounts.

7. **Considerations for Improvement**:
   - Adjust the decision threshold to balance the False Positive Rate (FPR) and False Negative Rate (FNR).
   - Use secondary validation steps for flagged accounts to improve overall precision.
   - Consider the cost-benefit tradeoff of false positives versus false negatives when deciding to deploy the model.

### **Question 4**  
**What metrics or approach would you look at to decide if you should launch this classifier?**

**Answer Explanation**:
- **Metrics**:
  - Confusion Matrix: TPR, FPR, FNR, Precision, Recall, F1-score.
  - Precision-Recall tradeoff, especially in unbalanced data (5% fake accounts).
- **Cost-Based Metrics**:
  - Weigh the cost of false positives (e.g., user friction) vs. false negatives.
- **A/B Testing**:
  - Evaluate user impact (e.g., appeals, user churn) vs. fake account reduction.
- **ROC/PR Curves**:
  - Identify optimal thresholds.

**Summary**: Decisions must balance precision, recall, and user experience impact.

---

## Why These Questions Align with Meta’s Analytical Execution

1. **Hypotheses**: You hypothesized friend request patterns and classifier performance.
2. **Tradeoffs**: Balanced false positives/negatives and user impact.
3. **Descriptive Stats**: Applied binomial assumptions and conditional probability.
4. **Bayes’ Theorem**: Converted priors to actionable posteriors.
5. **Real-World Data Profile**: Explained disproportionate impact of fake accounts.

---

## Key Takeaways for Candidates

- **Clarify Priors**: Understand baseline rates and their implications.
- **Apply Bayes**: Practice converting accuracy metrics into real-world probabilities.
- **Balance Tradeoffs**: Evaluate costs/impacts for large-scale user bases.
- **Communicate Clearly**: Structure your assumptions, math, and conclusions.

By demonstrating probability skills, tradeoff analysis, and real-world impact considerations, you showcase the analytical execution skills Meta values.

**I. Identifying Fake Accounts and Content**

*   **Detection Methods:**
    *   How would you identify fake accounts on a platform like Facebook or Instagram? Consider user reports, registration information analysis (IP address, email, phone number), friend request patterns, or machine learning models.
    *   What specific features would you use in a model to detect fake accounts?
    *   How would you identify fake high school information on Facebook?
    *   How can you detect fake accounts via the long tail in the distribution, high post/day, or high median interval between posts?
    *  What other methods can be used to identify fake accounts?
    * How would you differentiate between fake news that looks exactly like real news?
    *   How would you use user comments as a signal to identify fake news?
    *   How would you detect and estimate the impact of fake accounts?
    * How would you evaluate a system for detecting spam accounts?
    *   What "long tail" characteristics would you look for when analyzing a distribution to find fake accounts?
*   **Evaluation of Flags:**
    *   A user's comment was flagged as fake. How would you evaluate the validity of this flag?
    *   A news article was flagged as fake. What kind of data is used to determine if the news is indeed fake?

**II. Measuring the Impact of Fake Accounts**

*   **Impact Metrics:**
    *   How do you measure the impact of fake accounts on the platform and on real users? Consider metrics like user engagement (DAU, time spent), user churn, content prevalence, and network effects.
    *   How would you evaluate the impact of fake accounts on "send friend request" behavior?
    *   How do fake accounts affect user engagement?
*   **Quantifying Impact:**
    *   There are 5% fake accounts on the platform. If a fake account sends friend requests 10 times more frequently than a real account, how would you calculate the probability that a friend request is from a fake account?
    *   How would you estimate the impact of fake news, and how could an intern help with this process?
    *   How would you estimate the impact of fake news within an 8-hour timeframe?
    *   How do you measure the impact of fake accounts, including network effects, user churn, and content prevalence?

**III. Detection and Mitigation Strategies**

*   **Handling Evasion:**
    * How do you deal with bad actors who know how to evade detection models?
    *   How would you evaluate users who are trying to avoid spam detection?
*   **Scaling Solutions:**
    *   How would you scale your fake account detection solution?
*  **Manual Review**
   * If there are a large number of fake accounts, how do you determine which ones to manually review? What attributes would you focus on?
*   **Mitigation:**
    *  How would you minimize fake profiles, possibly using 2-step verification for risky users?
*   **General Principles**
    *  The key with fraud is that it doesn't happen only once. People who commit fraud would like to repeat it if not being caught.

**IV. Modeling and Analysis**

*   **Model-Based Approaches:**
    *   How can you use a model to measure the impact of fake accounts?
    *   What kind of features would you include in the model, and why?
    *   How would you validate your model?
    *  If you don't have a model, what approach could you use?
    *  How would you build a model to predict fake news?
*   **Bayesian Methods**
     *   How to identify bad actors using Bayesian methods?
    *   How to calculate the probability of a user being a bad actor?
*   **Thresholds & Anomaly Detection**
      *  How would you use a threshold to identify abnormal data points to find fake accounts?
*    **Model Evaluation**:
     * Given a model that predicts fraud with 95% accuracy, and 5% of accounts are fraudulent, calculate the probability that a positive prediction is correct.
     *  How would you further validate the model and ensure that the predicted fraud is actually fraud?
*   **Statistical Analysis:**
    *  What metrics should you look at in an unbalanced dataset, such as one with a low percentage of fake accounts?
    *   Given a classifier with a 95% TP and FN rate, how do you evaluate it in the context of fake account detection? What metrics would you use, and why?
    *   How do you measure the false negatives and false positives in fake account detection? What if you do not have ground truth, or cannot build a model?

**V. Experimentation and Causal Inference**

*   **A/B Testing:**
    *  How would you set up an A/B test for fake account detection?
*   **Difference-in-Differences (DiD):**
    *   How would you use a Difference-in-Differences (DiD) approach to measure the impact of fake accounts?
    *   What kind of interaction point would you use for DiD?

These questions are designed to cover a range of concepts and skills related to fake accounts, including detection, impact measurement, mitigation, and model evaluation. They also incorporate various analytical and statistical methods, and encourage you to think critically and creatively.


# 假新闻
# 评论分布
### **Comment Distribution Question**

#### **Context**
The question was asked in the **Analytics Execution** portion of the Meta Data Scientist interview. It evaluates the candidate’s understanding of data distributions, descriptive statistics, and their ability to hypothesize based on common patterns in user behavior.

The product in focus is a **newsfeed-like feature** where users can comment on posts. Candidates were asked to analyze the distribution of comments and perform statistical reasoning.

---

### **Question 1**  
**Describe the distribution of the number of comments per user in a newsfeed-like product. Draw the graph and indicate the mean, median, and the 95th percentile.**

**Answer Explanation**:
1. **Distribution Shape**:
   - The distribution is **zero-inflated and long-tailed**:
     - Most users make no comments (leading to a spike at zero).
     - Among users who do comment, the majority make few comments, but a small number of highly active users comment a lot, causing a long tail.

2. **Key Metrics**:
   - **Mean**: Positioned further toward the right, influenced by the long tail.
   - **Median**: Closer to the spike at zero, as the majority of users make no or few comments.
   - **95th Percentile**: Located further right, near the long tail, representing very active users.

3. **Visualization**:
   - The graph would show a large spike at zero, followed by a decreasing curve with a long right tail.

---

### **Question 2**  
**If users are randomly divided into groups of 10,000 users each and this process is repeated 200 times, what is the distribution of the average number of comments per group?**

**Answer Explanation**:
1. **Distribution Type**:
   - The resulting distribution is approximately **normal** due to the Central Limit Theorem (CLT), assuming the individual averages are based on sufficiently large samples (10,000 users per group).

2. **Key Characteristics**:
   - **Mean**: The mean of the distribution will be the population mean (e.g., 2 comments per user).
   - **Deviation**: The standard deviation depends on the **sample size** and the variability of the population distribution.

3. **Impact of Sample Size**:
   - Smaller group sizes lead to larger variability (wider distribution).
   - Larger group sizes reduce variability (narrower distribution).

---

### **Question 3**  
**If the average number of comments suddenly increases from 2 to 3, how would you analyze the causes?**

**Answer Explanation**:
1. **Internal Factors**:
   - **App changes**: Design updates or features that encourage commenting (e.g., engagement campaigns or incentives).
   - **Improved user experience**: Changes that make commenting easier.

2. **External Factors**:
   - **News events**: Major events prompting user discussions.
   - **Changes in user demographics**: More active users joining the platform.

3. **Additional Hypothesis**:
   - **Fake accounts**: The increase might be caused by an influx of fake accounts posting excessive comments.

---

### **Question 4**  
**If real accounts post an average of 2 comments per day and fake accounts post an average of 50 comments per day, and the platform average is 3 comments per day, what is the ratio of fake to real accounts?**

**Answer Explanation**:
1. **Equation**:
   \[
   \text{Total Comments} = 50 \cdot \text{Fake Accounts} + 2 \cdot \text{Real Accounts}
   \]
   \[
   \text{Total Accounts} = \text{Fake Accounts} + \text{Real Accounts}
   \]
   \[
   \frac{\text{Total Comments}}{\text{Total Accounts}} = 3
   \]

2. **Solve for Ratio**:
   Substitute into the equation:
   \[
   50 \cdot \text{Fake Accounts} + 2 \cdot \text{Real Accounts} = 3 \cdot (\text{Fake Accounts} + \text{Real Accounts})
   \]
   Simplify:
   \[
   47 \cdot \text{Fake Accounts} = \text{Real Accounts}
   \]

**Ratio**: \( 47:1 \).

---

### **Question 5**  
**Is it a good idea to ban accounts that post more than 50 comments daily to eliminate fake accounts?**

**Answer Explanation**:
1. **Short-term Feasibility**:
   - Effective in quickly reducing fake accounts, as most real users post far fewer than 50 comments per day.

2. **Long-term Concerns**:
   - Some real users might occasionally exceed 50 comments (e.g., during a major news event or personal activity).
   - Determined bad actors could adjust their behavior to evade detection.

3. **Recommended Approach**:
   - Combine threshold-based rules with **machine learning models** to detect fake accounts.
   - Use additional features (e.g., IP address patterns, activity timing) for robust identification.

---

### **Bonus Question**  
**If you track users from the long tail (high commenters) over time, where will their comment distribution trend?**

**Answer Explanation**:
1. **Mean Reversion**:
   - Over time, users’ activity levels tend to regress toward their personal average or the population mean.
   - Users from the long tail often include those who temporarily comment more than usual due to specific events.

2. **Assumption**:
   - Daily comment counts for each user are assumed to follow a stable distribution centered around their personal median.

3. **Conclusion**:
   - The long tail will likely shrink, and comment levels will trend toward the overall mean (e.g., 2 comments per user).

---

This set of questions comprehensively assesses the candidate’s ability to analyze distributions, apply statistical reasoning, and make data-driven decisions while considering real-world complexities like user behavior and platform integrity.
[2024-12-10 Meta DSA VO 面经](https://www.1point3acres.com/bbs/thread-1102145-1-1.html)  
印象非常深刻的一场，是一个经典问题
如果有一个聚合新闻网站，用户可以阅读新闻且发布评论，问如果X是DAU，Y是评论数，这是个什么分布？画出来
答案：这是一个典型的Zero-inflated log normal distribution，原因是大部分浏览新闻的人可能都不会留下或者很少留下评论，因此会有很多的0，然后在会评论的人里，大部分人评论比较少，少部分人评论很多，因此有一个长尾。大概如下图：  
![My Picture](images/distribution.png "My Picture")  


我给出的评论平均数大概是2，面试官说那就用这个数字。
follow up：如果现在随机给用户分桶，每个桶10K user，计算每个桶的评论平均数，然后这个平均数得到的分布是什么？.
答：sampling distribution，一个偏正态，平均值是2，但是靠近坐标原点有凸起（因为zero inflation，所以会有一定数量的0）的分布。
follow up：有一天你发现评论数大大提升了，从2到了3，请问你如何分析为什么？我从内部，外部因素进行了分析，例如app改版，engagement campaign鼓励更多评论，重点外部新闻事件发生导致评论用户增加，最后引导到了fake account。
. 1point 3 acres
. .и
follow up：一个真的account每日评论平均数是2，fake account是50，现在平台平均评论是3，fake ：real的对比是多少？
50fake + 2real = total comment
total account = fake + real
tc / ta = 3
(50fake + 2real) / (fake+real) = 3
50/3 fake + 2/3 real = fake + real. 1point3acres
47/3 fake  = 1/3 real.google  и
答案是47:1
follow up：现在PM问你，我们要解决fake account问题，所以设立一个规则，日评论大于50统统封禁，是不是个好主意？
.1point3acres
答：短期（2-3日），可以，长期，不行，需要explore其他方案，例如机器学习鉴别fake account。下面就是一系列机器学习的模型设计，feature selection，ground truth从哪里来，如何跟PM沟通做抉择，等等的产品和沟通问题。
.google  и
. 1point 3acres
bonus question：如果我们从原本评论的分布长尾上取出一批评论数量高的用户，追踪它们一段时间，一段时间后他们的分布大概率会在哪里？.
. Χ
答：偏向均值回归，对每个人来说，每日的评论概率可以假设固定且围绕个人中值分布，长尾上很有可能是例如某些人恰好某天评论数特别多+一些本来评论就很多人的聚合，长期来看会均值回归。

-----
# Feed里插广告
### **Ads Impression Distribution Question**

#### **Context**
The question was asked in the **Analytics Execution** portion of the Meta Data Scientist interview. It evaluates the candidate's understanding of **expected value**, **probability**, and **binomial distribution**, along with their ability to analyze ad impression data. The scenario involves impressions randomly distributed among users.

---

### **Question 1**  
**What is the expected number of ads seen by a user if an advertiser purchases \( A \) impressions for a target audience size of \( u \)?**

**Answer Explanation**:
1. **Probability of an impression reaching a specific user**:
   - \( P(\text{Impression for User}) = \frac{1}{u} \).

2. **Expected number of impressions for one user**:
   - \( \mathbb{E}[\text{Ads}] = A \cdot \frac{1}{u} = \frac{A}{u} \).

---

### **Question 2**  
**What is the probability of a user not seeing any ads?**

**Answer Explanation**:
1. **Binomial distribution for not seeing ads**:
   - \( P(\text{No Ads for User}) = \left(1 - \frac{1}{u}\right)^A \).


### **Question 3**  
**What is the probability of a user seeing at least one ad?**

**Answer Explanation**:
1. **Complement Rule**:
   - \( P(\text{At Least One Ad}) = 1 - P(\text{No Ads for User}) \).

2. **Substitute \( P(\text{No Ads for User}) \)**:
   - \( P(\text{At Least One Ad}) = 1 - \left(1 - \frac{1}{u}\right)^A \).

---

### **Question 4**  
**What is the expected number of users seeing at least one ad?**

**Answer Explanation**:
1. **Expected number of users**:
   - \( \mathbb{E}[\text{Users with Ads}] = u \cdot P(\text{At Least One Ad}) \).

2. **Substitute \( P(\text{At Least One Ad}) \)**:
   - \( \mathbb{E}[\text{Users with Ads}] = u \cdot \left[1 - \left(1 - \frac{1}{u}\right)^A\right] \).

---

### **Question 5**  
**If 25% of users are high-intent (90% click probability) and 75% are low-intent (10% click probability), what is the expected number of clicks for \( A \) impressions?**

**Answer Explanation**:
1. **Weighted Click Rate**:
   - \( \text{Click Rate} = 0.25 \cdot 0.9 + 0.75 \cdot 0.1 = 0.225 + 0.075 = 0.3 \).

2. **Expected Clicks**:
   - \( \mathbb{E}[\text{Clicks}] = A \cdot \text{Click Rate} \).

3. **Substitute**:
   - \( \mathbb{E}[\text{Clicks}] = 0.3 \cdot A \).

---

### **Question 6**  
**Draw a graph for the likelihood of zero clicks versus the number of impressions (\( A \)).**

**Answer Explanation**:
1. **Likelihood of Zero Clicks**:
   - For all impressions to result in no clicks:
     \[
     P(\text{Zero Clicks}) = \left(1 - \text{Click Rate}\right)^A.
     \]

2. **Substitute Click Rate**:
   - \( P(\text{Zero Clicks}) = \left(1 - 0.3\right)^A = 0.7^A \).

3. **Graph**:
   - \( x \)-axis: Number of impressions (\( A \)).
   - \( y \)-axis: \( P(\text{Zero Clicks}) = 0.7^A \), which decays exponentially.

---

### **Question 7**  
**The business wants to serve ads only to high-intent users. Is this a good idea?**

**Answer Explanation**:
1. **Short-term Feasibility**:
   - Focusing on high-intent users (\( 25\% \)) maximizes the click rate (0.9), increasing immediate returns.

2. **Long-term Concerns**:
   - Narrowing the target audience reduces overall reach and impressions, potentially leading to **saturation**.
   - Excluding low-intent users might harm brand awareness and future engagement.

3. **Recommendation**:
   - Combine targeting strategies:
     - Prioritize high-intent users for direct response campaigns.
     - Include low-intent users for broader brand awareness.
     
### Question 8: **Probability of Users Seeing Back-to-Back Ads**

The probability of users seeing back-to-back ads depends on the ad placement strategy (e.g., fixed interval vs. random insertion). Below is the calculation for both scenarios.

---

### **1. Scenario 1: Fixed Interval Ad Insertion**
If ads are inserted **every 20 users**:
- Ads are uniformly distributed across users, with no overlap between consecutive ads.
- **Probability of Back-to-Back Ads**:
  \[
  P(\text{Back-to-Back Ads}) = 0
  \]

---

### **2. Scenario 2: Random Ad Insertion**
If ads are randomly assigned with a probability \( p = 5\% \) to each user:

#### **Probability Calculation**
1. **Define Events**:
   - \( A_i \): User \( i \) is shown an ad.
   - \( A_{i+1} \): User \( i+1 \) is shown an ad.
   - Ads are assigned independently, with \( P(A_i) = 0.05 \).

2. **Back-to-Back Probability**:
   - The probability of two consecutive users seeing ads:
     \[
     P(\text{Back-to-Back Ads}) = P(A_i \cap A_{i+1}).
     \]
   - Since the events are independent:
     \[
     P(\text{Back-to-Back Ads}) = P(A_i) \cdot P(A_{i+1}) = 0.05 \cdot 0.05 = 0.0025 \, (0.25\%).
     \]

3. **For a Group of Users**:
   For \( N \) users, there are \( N-1 \) consecutive pairs. The probability of at least one pair seeing back-to-back ads is:
   \[
   P(\text{At Least One Back-to-Back Pair}) = 1 - P(\text{No Back-to-Back Pairs}),
   \]
   where:
   \[
   P(\text{No Back-to-Back Pairs}) = \left(1 - 0.0025\right)^{N-1}.
   \]

4. **Approximation for Large \( N \)**:
   Using the exponential approximation:
   \[
   P(\text{At Least One Back-to-Back Pair}) \approx 1 - e^{-0.0025 \cdot (N-1)}.
   \]

---

### **3. Example Calculation**
Suppose the total number of users \( N = 1000 \):
1. Probability of a single back-to-back pair:
   \[
   P(\text{Back-to-Back Ads for 1 Pair}) = 0.0025.
   \]

2. Probability of at least one back-to-back pair:
   \[
   P(\text{At Least One Back-to-Back Pair}) \approx 1 - e^{-0.0025 \cdot (1000-1)} = 1 - e^{-2.4975}.
   \]

3. Approximate Value:
   \[
   P(\text{At Least One Back-to-Back Pair}) \approx 1 - 0.0822 = 0.9178.
   \]

**Result**: For a group of 1000 users with ads randomly assigned at 5%, the probability of at least one pair of users seeing back-to-back ads is approximately **91.78%**.

---

### **4. Summary**

- **Fixed Interval Insertion**:
  - Ads are evenly spaced, so the probability of back-to-back ads is:
    \[
    P(\text{Back-to-Back Ads}) = 0
    \]

- **Random Insertion**:
  - For a single pair of users:
    \[
    P(\text{Back-to-Back Ads}) = 0.25\%.
    \]
  - For large groups, the probability of at least one back-to-back pair increases significantly. For \( N = 1000 \), it is approximately **91.78%**.

When choosing an ad insertion strategy, balancing user experience and ad distribution fairness is crucial. Random insertion might lead to more back-to-back ads, potentially harming user experience.
---

### **Takeaways**
This set of questions comprehensively evaluates:
1. **Probability Rules**:
   - Binomial distribution and complement rule for impressions.
2. **Expected Value**:
   - Calculating expected values for impressions, clicks, and reach.
3. **Strategic Analysis**:
   - Short-term vs. long-term impacts of targeting decisions.

Clear articulation of assumptions, precise use of formulas, and connecting mathematical insights to actionable recommendations are key to solving such problems.

[2024-3-16买它ds过经](https://www.1point3acres.com/bbs/thread-1053544-1-1.html)  
[2024-4-15 Meta DSA VO](https://www.1point3acres.com/bbs/thread-1061408-1-1.html)  
Assuming we have an advertiser purchasing ads on our platform. The target audience size is u and the advertiser purchased A impressions.
1. What is the expectation of seeing ads?  
probability of seeing ads = 1/u, expectation is np so A/u
. check 1point3acres for more.
1. What is the probability of users not seeing the ads? (1-1/u)^A
2. What is the probability of users at least seeing one ads? 1-P(not seeing ad) = 1- (1-1/u)^A
3. What is the expectation of not seeing the ads? E[X] = np = [1- (1-1/u)^A] u. 1point 3 acres
4. Probability of high intent users is 25%, low intent users is 75%, high intent user 0.9 click rate, low intent user 0.1 click rate. What is the expectation of clicking? A[0.25*0.9+0.75*0.1]
5. Please draw a graph of likelihood of 0 clicking versus number of impressions. Y = (0.25*0.1+0.75*0.9)^A draw this equation -baidu 1point3acres
6. The business only wants to place ads only to high intent users, is this a good idea?
Binomial problem needs to remember E[X] = np, Var[X] = np(1-p); . From 1point 3acres bbs
The multiplication rule of probability, the probability of occurrence of both the events A and B is equal to the product of the probability of B occurring and the conditional probability that event A occurring given that event B occurs.
Take away: remember to explain explicitly what concept you are using and what rules you are using.
.
Analyze launch a new strategy —> A/B testing

问了个comment distribution。会问到central limit theorem, expected value, population sd vs. sample sd, 95% confidence interval。以及这个帖子的原题🔗 www.1point3acres.com
其中这个帖子中我看到有人讨论expected value 是乘以A还是u。应该是u，因为面试里问的不是一个用户，而是所有用户.


好多个小题，从Central limit T 开始，问最基本的概念。

选人 - 1000个人里面有放回抽取。 1. 每个人on avg. 在多少次抽到。 2. 连续10次你没被抽到的概率。. .и

 IMPRESSIONS - X people, 一共有Y Impression随机分配。 1) expected impression per audience？2) probability of each person have at least one impression。还问了近似值是多少，多亏之前看了面经，需要泰勒展开 3) expected number of audience have at least one impression

 We’ve ran a prediction model and discovered 25\x of our audience is high intent (90\x probability of clicks) and 75\x are low intent (10\x clicks), how many clicks do we expect to see? 我的答案是0.3N。。。

   不好意思variance 我有点记不清了 但是我想复杂了 就是一道很直截了当告诉你多少个sample 你用最原始的公式算variance 就好了的 不需要说任何的distribution，最后binomial 的那个Probability of 0 impressions 你把binomial的公式写出来就会发现有可以用到taylor 来估算 这一题我在面经里看到过 假设M N 都很大那么(1-1/M)^N 可以约等于1-N/mAB test 就是告诉了我一个结果就是screen time 没有significant difference 问我可能是因为什么，貌似没有问道CI，然后就问我那可以选择别的什么metric 以及如何来设计一个更好的test

   X个audience， Y 个impression 随机分配

1. expected impression per audience？-Y/X

2. probability of each person have at least one impression - 1-(1-1/X)^Y

3. expected number of audience have impression - (1-(1-1/X)^Y)*X

quantitative 是考ads impression 还有 active user daily post 的数量分布画图

        ads impression: there are x users, y ads, each ad can reach to each user with equal probability, then for a particular user, the expected number of ads and variance。这个就是根据binomial distribution, E(X) = np = y*(1/x), Var(X) = np(1-p) = y*(1/x)*(1-1/x). .. 

       The probability that one user does see at least one ads. 也是根据binomial distribution和补集概念，P(X>=1) = 1 - P(X=0) = 1 - (1 - 1/x)^y。

N people M impression, 平均一个会收到多少个impression的期望，问你的assumption可以成立么是独立事件吗，然后给看了两个confidence interval让interpret

