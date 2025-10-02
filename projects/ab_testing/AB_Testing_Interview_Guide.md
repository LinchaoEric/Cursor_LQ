# AB Testing Interview Guide
*Quick Reference for Tech Company Interviews*

---

## 🎯 **CORE FRAMEWORK**

### **1. Business-First Approach**
**Always start with:**
- **Why** are you doing this experiment?
- **What problem** are you solving?
- **Who** will benefit?
- **What value** does this create?

### **2. Metrics Hierarchy**
```
Primary Metrics    → Company KPIs (Revenue, Growth, Retention)
Secondary Metrics  → Supporting metrics that lead to primary goals
Tracking Metrics   → Intermediate steps showing progress
Guardrail Metrics  → Safety metrics to prevent negative impacts
```

---

## 📊 **EXPERIMENTAL DESIGN**

### **Sample Size Factors**
- **α (Significance level)**: Usually 0.05
- **Power (1-β)**: Usually 0.8 or 0.9
- **MDE (Minimum Detectable Effect)**: Smallest effect you want to detect
- **Variance**: Higher variance = larger sample needed

### **Duration Guidelines**
- **Short experiments**: 2 weeks
- **Medium experiments**: 3-5 weeks
- **Long experiments**: 6-8 weeks

### **Population Definition**
**Good Example**: "Users who streamed at least 12 times in last 6 months"
**Avoid**: Including users who won't use the feature

### **Randomization Strategy**
- **User-level**: Most common (engagement experiments)
- **Session-level**: UI/algorithm changes
- **Market-level**: Pricing/geographic experiments
- **Stratified**: For heterogeneous populations

---

## 🔍 **STATISTICAL CONCEPTS**

### **Multiple Testing Corrections**
- **Bonferroni**: Conservative, simple
- **FDR (False Discovery Rate)**: Less conservative, practical
- **Sequential Testing**: Pre-planned stopping rules

### **Power Analysis - Common Issues & Solutions**
**Problem**: Experiments not showing significance

**Solutions**:
1. Increase sample size
2. Reduce variance (use covariates)
3. Focus on relevant population
4. Use more sensitive metrics

### **Covariate Adjustment**
**What to include**:
- Pre-period values (baseline behavior)
- Demographics (age, location, user type)
- Behavioral features (usage patterns)

**Benefits**: Reduces variance, increases power

---

## 🚀 **IMPLEMENTATION CHECKLIST**

### **Pre-Experiment**
- [ ] Write design document
- [ ] Get stakeholder buy-in
- [ ] Define success criteria
- [ ] Identify guardrails
- [ ] Plan monitoring strategy

### **During Experiment**
- [ ] Monitor key metrics daily
- [ ] Use pre-planned stopping rules
- [ ] Analyze by user segments
- [ ] Track guardrail metrics

### **Post-Experiment**
- [ ] Run statistical analysis
- [ ] Calculate business impact
- [ ] Plan gradual rollout (1% → 5% → 10% → 50%)
- [ ] Set up long-term monitoring

---

## ⚠️ **COMMON PITFALLS**

### **Statistical Issues**
- ❌ Not correcting for multiple comparisons
- ❌ Stopping early without correction
- ❌ Poor randomization
- ❌ Sample size too small

### **Business Issues**
- ❌ Wrong primary metrics
- ❌ Ignoring long-term effects
- ❌ Not monitoring guardrails
- ❌ Poor stakeholder communication

---

## 💡 **INTERVIEW FRAMEWORK**

### **6-Step Answer Structure**
1. **Business Context**: Why is this needed?
2. **Hypothesis**: What do you expect?
3. **Design**: How will you test?
4. **Metrics**: What will you measure?
5. **Analysis**: How will you interpret?
6. **Implementation**: How will you roll out?

### **Common Questions & Quick Answers**

**Q: "Design an A/B test for [feature]"**
**A**: Use the 6-step framework above

**Q: "How do you determine sample size?"**
**A**: Power analysis based on α, power, MDE, and variance

**Q: "What if experiment doesn't show significance?"**
**A**: Check power, increase sample size, use covariates, focus on relevant population

**Q: "How do you handle multiple testing?"**
**A**: Use Bonferroni (conservative) or FDR (practical) corrections

**Q: "Explain your most impactful experiment"**
**A**: Use STAR method (Situation, Task, Action, Result)

---

## 📚 **REAL-WORLD EXAMPLES**

### **Netflix**
- **Experiment**: Content recommendation algorithms
- **Metrics**: Watch time, completion rates, user retention
- **Challenge**: Isolating content effects from algorithm effects

### **YouTube**
- **Experiment**: Creator monetization features
- **Metrics**: Revenue per creator, creator retention
- **Challenge**: Small population size (creators vs viewers)

### **Uber**
- **Experiment**: Driver/rider matching algorithms
- **Metrics**: Wait times, driver earnings, rider satisfaction
- **Challenge**: Network effects between drivers and riders

### **Amazon**
- **Experiment**: Product recommendations and pricing
- **Metrics**: Conversion rates, revenue per user
- **Challenge**: Seasonal effects and external factors

---

## 🎯 **INTERVIEW TIPS**

### **Do's**
- ✅ Tell specific stories with numbers
- ✅ Show systematic thinking process
- ✅ Connect technical concepts to business impact
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

## 📖 **RESOURCES**

### **Books**
- "Trustworthy Online Controlled Experiments" by Kohavi
- "Elements of Statistical Learning"

### **Online Courses**
- EVD3S Academy
- DataCamp AB Testing courses

### **Practice**
- Build projects with real data
- Use open datasets for practice
- Simulate experiments in Python/R

---

*Use this guide as a quick reference during interview preparation. Focus on understanding the concepts rather than memorizing every detail.*
