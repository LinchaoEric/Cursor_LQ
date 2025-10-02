# AB Testing - Concise Summary
*From Tech Company Webinar - All Key Details*

---

## 🎯 **CORE CONCEPTS**

### **Business-First Approach**
- **Start with WHY**: Business goal, problem statement, value proposition
- **Define target users** who will actually use the feature
- **Connect everything to business impact**

### **Metrics Framework**
```
Primary Metrics    → Revenue, User Growth, Retention (company KPIs)
Secondary Metrics  → Supporting metrics that lead to primary goals  
Tracking Metrics   → Intermediate steps (clicks, engagement)
Guardrail Metrics  → Safety metrics (user satisfaction, system performance)
```

---

## 📊 **EXPERIMENTAL DESIGN**

### **Sample Size & Duration**
**Factors affecting sample size:**
- α (significance level): 0.05
- Power (1-β): 0.8 or 0.9  
- MDE (Minimum Detectable Effect): Smallest meaningful effect
- Variance: Higher variance = larger sample needed

**Duration Guidelines:**
- **Short experiments**: 2 weeks (simple UI changes)
- **Medium experiments**: 3-5 weeks (feature rollouts)
- **Long experiments**: 6-8 weeks (complex changes, seasonal effects)

**Key Insight**: Duration should be based on business needs, not just statistical requirements.

### **Population Definition**
**Good Example**: "Users who streamed at least 12 times in last 6 months"
**Avoid**: Including users who won't use the feature

**Real Example from YouTube**: 
- Problem: Creator monetization experiments had small sample sizes
- Solution: Focused on "creators who streamed 12+ times in 6 months AND in top 90% earnings"
- Result: Experiments started showing significance

### **Randomization Strategy**
- **User-level**: Most common (engagement experiments)
- **Session-level**: UI/algorithm changes  
- **Market-level**: Pricing/geographic experiments
- **Stratified**: For heterogeneous populations (creators vs viewers)

---

## 🔍 **STATISTICAL METHODS**

### **Multiple Testing Corrections**
- **Bonferroni**: Conservative, simple (divide α by number of tests)
- **FDR (False Discovery Rate)**: Less conservative, more practical
- **Sequential Testing**: Pre-planned stopping rules with corrections

### **Power Analysis - Common Problems & Solutions**
**Problem**: Experiments not showing significance

**Solutions**:
1. **Increase sample size** (most direct)
2. **Reduce variance** using covariates (pre-period values, demographics)
3. **Focus on relevant population** (remove irrelevant users)
4. **Use more sensitive metrics** (closer to user behavior)

### **Covariate Adjustment (CUPED)**
**What to include**:
- Pre-period values (baseline behavior)
- Demographics (age, location, user type)
- Behavioral features (usage patterns, preferences)

**Benefits**: Reduces variance by 20-50%, increases power significantly

**Real Example**: YouTube used regression with pre-period revenue + treatment + covariates to get individual treatment effects for every creator.

---

## 🚀 **IMPLEMENTATION PROCESS**

### **Pre-Experiment Planning**
- [ ] Write comprehensive design document
- [ ] Get stakeholder buy-in and review
- [ ] Define clear success criteria and guardrails
- [ ] Plan monitoring strategy and stopping rules

### **During Experiment**
- [ ] Monitor key metrics daily
- [ ] Use pre-planned stopping rules (not ad-hoc decisions)
- [ ] Analyze results by user segments
- [ ] Track guardrail metrics for safety

### **Post-Experiment**
- [ ] Run proper statistical analysis
- [ ] Calculate business impact and ROI
- [ ] Plan gradual rollout (1% → 5% → 10% → 20% → 50%)
- [ ] Set up long-term monitoring for sustained effects

---

## ⚠️ **COMMON PITFALLS & SOLUTIONS**

### **Statistical Issues**
- ❌ **Multiple Testing**: Not correcting for multiple comparisons
- ❌ **Early Stopping**: Stopping based on interim results without correction
- ❌ **Selection Bias**: Not properly randomizing users
- ❌ **Sample Size**: Too small to detect meaningful effects

### **Business Issues**
- ❌ **Wrong Metrics**: Focusing on secondary instead of primary metrics
- ❌ **Short-term Focus**: Not considering long-term effects
- ❌ **Ignoring Guardrails**: Not monitoring negative side effects
- ❌ **Poor Communication**: Not explaining results to stakeholders

### **Real Examples of Solutions**
**YouTube Power Problem**: All experiments were not showing significance
**Solution**: 
- Refined population (focused on relevant creators)
- Used stratified sampling (balanced creator types)
- Added covariate adjustment (pre-period revenue)
- Result: All experiments started showing significance

---

## 💡 **INTERVIEW FRAMEWORK**

### **6-Step Answer Structure**
1. **Business Context**: Why is this experiment needed?
2. **Hypothesis**: What do you expect to happen?
3. **Design**: How will you test this?
4. **Metrics**: What will you measure?
5. **Analysis**: How will you interpret results?
6. **Implementation**: How will you roll out if successful?

### **Common Questions & Answers**

**Q: "Design an A/B test for [feature]"**
**A**: Use the 6-step framework, start with business goal, define metrics hierarchy

**Q: "How do you determine sample size?"**
**A**: Power analysis based on α, power, MDE, and variance. Consider business constraints.

**Q: "What if experiment doesn't show significance?"**
**A**: Check power, increase sample size, use covariates, focus on relevant population

**Q: "How do you handle multiple testing?"**
**A**: Use Bonferroni (conservative) or FDR (practical) corrections, pre-plan stopping rules

**Q: "Explain your most impactful experiment"**
**A**: Use STAR method (Situation, Task, Action, Result) with specific numbers

---

## 📚 **REAL-WORLD EXAMPLES**

### **Netflix - Content Recommendation**
- **Experiment**: New recommendation algorithm
- **Challenge**: Isolating algorithm effects from content effects
- **Solution**: Ran for 2 months to cycle through different content themes
- **Metrics**: Watch time, completion rates, user retention

### **YouTube - Creator Monetization**
- **Experiment**: New monetization features for creators
- **Challenge**: Small population size (creators vs viewers)
- **Solution**: Focused on relevant creators, used covariate adjustment
- **Metrics**: Revenue per creator, creator retention

### **Uber - Driver/Rider Matching**
- **Experiment**: New matching algorithms
- **Challenge**: Network effects between drivers and riders
- **Metrics**: Wait times, driver earnings, rider satisfaction

### **Amazon - Pricing & Recommendations**
- **Experiment**: Dynamic pricing and product recommendations
- **Challenge**: Seasonal effects and external factors
- **Metrics**: Conversion rates, revenue per user

---

## 🎯 **KEY INSIGHTS FROM WEBINAR**

### **Duration Decisions**
- **Business-driven**: Netflix ran 2-month experiment to isolate content effects
- **Not just statistical**: Waiting longer doesn't always give more power
- **Consider seasonality**: Need enough time to cycle through different conditions

### **Population Refinement**
- **YouTube example**: Focused on "creators who streamed 12+ times in 6 months AND top 90% earnings"
- **Result**: Experiments went from not significant to significant
- **Key**: Remove irrelevant users who won't use the feature

### **Covariate Adjustment**
- **YouTube implementation**: Used regression with pre-period revenue + treatment + covariates
- **Result**: Could calculate individual treatment effects for every creator
- **Method**: Bootstrap to get confidence intervals

### **Multiple Testing**
- **Sequential Testing**: Pre-planned stopping rules with corrections
- **Different thresholds**: Day 3 vs Day 5 need different p-values
- **Avoid**: Ad-hoc stopping without corrections

### **Rollout Strategy**
- **Gradual rollout**: 1% → 5% → 10% → 20% → 30% → 50%
- **Monitor guardrails**: Watch for negative side effects
- **Holdout groups**: Use for long-term impact measurement

---

## 📖 **RESOURCES MENTIONED**

### **Books**
- "Trustworthy Online Controlled Experiments" by Kohavi
- "Elements of Statistical Learning"
- "Introduction to Statistical Learning"

### **Online Courses**
- EVD3S Academy (self-paced, ~$700)
- DataCamp AB Testing courses

### **Practice**
- Build projects with real data
- Use open datasets for practice
- Simulate experiments in Python/R

---

## 🎯 **INTERVIEW SUCCESS TIPS**

### **Do's**
- ✅ Tell specific stories with numbers and business impact
- ✅ Show systematic thinking process
- ✅ Connect technical concepts to business value
- ✅ Acknowledge limitations honestly
- ✅ Use real examples from your experience

### **Don'ts**
- ❌ Memorize formulas without understanding
- ❌ Ignore business context
- ❌ Pretend to know everything
- ❌ Focus only on technical details
- ❌ Use generic examples

### **Key Phrases to Use**
- "From a business perspective..."
- "The key metric we're optimizing for is..."
- "To ensure statistical rigor..."
- "Given the constraints..."
- "The trade-off we're considering..."

---

*This summary captures all key details from the webinar while being organized for quick reference during interview preparation.*
