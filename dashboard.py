import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model/sentiment_pnl_model.joblib")

st.title("Trader Profitability Prediction")

sentiment = st.slider("Sentiment (-1 to 1)", -1.0, 1.0, 0.0)
size_usd = st.number_input("Trade Size USD", min_value=0.0)
direction = st.selectbox("Direction", ["Buy", "Sell"])
win_rate = st.slider("Trader Win Rate", 0.0, 1.0, 0.5)
frequency = st.selectbox("Segment Frequency", ["Frequent", "Infrequent"])
winner = st.selectbox("Segment Winner", ["Top", "Others"])

# ----- Encode exactly as model expects -----

direction_num = 1 if direction == "Buy" else 0
segment_frequency_Infrequent = 1 if frequency == "Infrequent" else 0
segment_winner_Others = 1 if winner == "Others" else 0

input_df = pd.DataFrame([{
    "sentiment_num": sentiment,
    "Size USD": size_usd,
    "direction_num": direction_num,
    "trader_win_rate": win_rate,
    "segment_frequency_Infrequent": segment_frequency_Infrequent,
    "segment_winner_Others": segment_winner_Others
}])

# ----- Prediction -----

if st.button("Predict Profitability"):
    pred = model.predict(input_df)[0]

    if pred == 1:
        st.success("✅ High Profitability Trader Likely")
    else:
        st.warning("⚠ Low Profitability Trader Likely")
