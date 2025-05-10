
import streamlit as st

st.title("Discounted Cash Flow (DCF) Calculator 2k7")

# 假設輸入未來 5 年的自由現金流
st.header("Step 1: Enter Free Cash Flow Forecasts")
fcfs = []
for i in range(1, 6):
    fcf = st.number_input(f"Year {i} Free Cash Flow ($)", value=1000 * i)
    fcfs.append(fcf)

# 折現率 (WACC)
discount_rate = st.number_input("Discount Rate (WACC, %)", value=10.0) / 100

# 永續成長率 (g)
terminal_growth_rate = st.number_input("Terminal Growth Rate (g, %)", value=2.0) / 100

# 計算現值
present_value = 0
for year, fcf in enumerate(fcfs, start=1):
    present_value += fcf / ((1 + discount_rate) ** year)

# 終值 (Terminal Value) 折現
terminal_value = (fcfs[-1] * (1 + terminal_growth_rate)) / (discount_rate - terminal_growth_rate)
terminal_value_discounted = terminal_value / ((1 + discount_rate) ** 5)

# 加總
enterprise_value = present_value + terminal_value_discounted

# 顯示結果
st.header("Step 2: Results")
st.write(f"Present Value of Cash Flows (Years 1–5): **${present_value:,.2f}**")
st.write(f"Discounted Terminal Value: **${terminal_value_discounted:,.2f}**")
st.subheader(f"Enterprise Value: **${enterprise_value:,.2f}**")
