import streamlit as st

# 1. Title
st.title("💰 BudgetBuddy")

# 2. Monthly Limit Input
limit = st.number_input("Monthly Budget (Rs)", value=10000)

# 3. Daily Spending Inputs (using a simple row)
st.write("Enter last 7 days of spending:")
cols = st.columns(7)
spent = [cols[i].number_input(f"D{i+1}", value=100, key=i) for i in range(7)]

# 4. Calculation and Result
if st.button("Forecast My Month"):
    prediction = (sum(spent) / 7) * 30
    gap = limit - prediction

    st.write(f"### Predicted Total: Rs {int(prediction)}")

    if prediction > limit:
        st.error(f"WARNING: Over budget by Rs {int(abs(gap))}")
    else:
        st.success(f"GOOD WORK: Saving Rs {int(gap)}")