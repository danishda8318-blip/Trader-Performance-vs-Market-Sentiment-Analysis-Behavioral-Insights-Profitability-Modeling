# Trader Performance vs Market Sentiment Analysis — Behavioral Insights & Profitability Modeling

## 1. Project Overview

This project analyzes how market sentiment (Fear & Greed Index) influences trader behavior and profitability in cryptocurrency markets. By combining large-scale historical trade data with daily sentiment indicators, the goal is to quantify behavioral shifts, performance differences, and develop a predictive model to estimate trader profitability under varying market conditions. Understanding sentiment-driven behavior is critical in real trading environments where emotional decision-making often amplifies risk, volatility, and capital loss.

---

## 2. Dataset Description

### Market Sentiment Dataset (Fear & Greed Index)

* Daily sentiment score capturing market psychology
* Includes:

  * Sentiment score (0–100)
  * Classification (Extreme Fear → Extreme Greed)
  * Timestamp and daily date
* Represents overall crypto market mood

### Historical Trading Dataset

* Over 200,000 individual crypto trades
* Key dimensions include:

  * Trader account identifiers
  * Trade size (USD & tokens)
  * Buy/Sell direction
  * Timestamps (IST & Unix)
  * Closed profit and loss (PnL)

### Merged Analytical Dataset

* Aligned on daily level using extracted trade dates
* Each trade enriched with corresponding market sentiment

---

## 3. Business Objective

### Prediction Target

Classify each trade into a **profitability bucket** (profitable vs non-profitable outcome) using sentiment and behavioral features.

### Success Metrics

* Accuracy for overall correctness
* F1-score to balance false positives and false negatives
* Confusion matrix for risk-aware evaluation

This approach prioritizes decision quality over raw accuracy — essential in financial environments where wrong predictions have asymmetric costs.

---

## 4. Feature Engineering

| Feature            | Business Rationale                                    |
| ------------------ | ----------------------------------------------------- |
| Sentiment Encoding | Captures market psychology impact on trader decisions |
| Trade Size (USD)   | Proxy for leverage and risk appetite                  |
| Direction Encoding | Models long vs short bias                             |
| Trader Win Rate    | Measures historical skill and consistency             |
| Frequency Segment  | Distinguishes active vs occasional traders            |
| Winner Segment     | Separates consistently profitable traders from others |

These features jointly represent **market conditions + human behavior + risk exposure**.

---

## 5. Modeling Approach

### Algorithms Explored

* Baseline classifiers
* Final model: **Random Forest Classifier**

### Why Random Forest

* Handles non-linear relationships
* Robust to noise
* Interpretable via feature importance

### Training Strategy

* Stratified train-test split (80/20)
* Class balancing via oversampling
* Behavior-driven feature space

---

## 6. Model Evaluation

**Final Performance:**

* Accuracy: ~64%
* F1 Score: ~0.62

### Interpretation

* Strong improvement over random guessing
* Balanced detection of profitable vs losing trades

### Why Accuracy Alone Isn’t Enough

In trading:

* False positives = capital loss
* False negatives = missed opportunity

F1-score ensures risk-aware reliability.

---

## 7. Key Insights

### Feature Importance Highlights

1. Trader historical win rate (strongest driver)
2. Trade size / risk exposure
3. Sentiment influence

### Behavioral vs Sentiment Effects

* Skilled traders remain resilient across sentiment cycles
* Average traders depend heavily on bullish environments
* Fear phases amplify losses and emotional overtrading

### Market Behavior Patterns

* Larger trades during Fear periods increased drawdowns
* Greed phases improved win rates but raised volatility

---

## 8. Limitations

* No direct leverage column (risk approximated via trade size)
* Market microstructure not modeled
* Crypto markets are inherently noisy
* Behavioral adaptation over time not captured

Perfect prediction is unrealistic due to market efficiency and randomness.

---

## 9. Business Implications

### Practical Use Cases

* Sentiment-aware risk controls
* Trader performance monitoring
* Capital allocation strategies

### Recommended Usage

* Reduce exposure during Fear regimes
* Scale positions only for consistently profitable traders
* Use predictions as decision support — not automated trading

---

## 10. Future Improvements

* Include volatility indicators and order book data
* Use time-series models (LSTM, XGBoost)
* Predict continuous PnL instead of buckets
* Advanced trader clustering
* Real-time sentiment ingestion

---

### Final Takeaway

Market sentiment shapes trader behavior, risk appetite, and profitability — but individual skill remains the dominant driver of success. Combining behavioral analytics with sentiment intelligence enables smarter risk management and more resilient trading strategies.
