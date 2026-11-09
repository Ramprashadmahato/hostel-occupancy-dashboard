import pandas as pd
import streamlit as st

st.set_page_config(page_title="Hostel Occupancy Dashboard", page_icon="🛏️", layout="wide")

st.title("🛏️ Hostel Occupancy Dashboard")
st.write(
    "Sample analytics for a hostel business: occupancy, revenue, and guest mix. "
    "Use the filters to explore by month and room type. "
    "All data below is a built-in sample dataset for demonstration."
)

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# beds_available, beds_sold, avg_price_usd, international_share_pct per room type & month index
BASE = {
    "Dorm bed": (2400, 0.62, 9, 55),
    "Private double": (620, 0.71, 28, 48),
    "Family room": (310, 0.66, 42, 35),
}
SEASON = [0.92, 0.88, 1.05, 1.12, 1.08, 0.85, 0.78, 0.82, 1.02, 1.18, 1.10, 0.95]

rows = []
for room_type, (beds, occ, price, intl) in BASE.items():
    for i, month in enumerate(MONTHS):
        sold = int(beds * occ * SEASON[i])
        rows.append(
            {
                "Month": month,
                "Month #": i + 1,
                "Room type": room_type,
                "Beds available": beds,
                "Beds sold": sold,
                "Occupancy %": round(100 * sold / beds, 1),
                "Revenue (USD)": sold * price,
                "International guests %": intl,
            }
        )
df = pd.DataFrame(rows)

with st.sidebar:
    st.header("Filters")
    room_types = st.multiselect("Room type", sorted(df["Room type"].unique()), default=sorted(df["Room type"].unique()))
    month_range = st.slider("Month range", 1, 12, (1, 12))

filtered = df[
    df["Room type"].isin(room_types)
    & (df["Month #"] >= month_range[0])
    & (df["Month #"] <= month_range[1])
]

total_revenue = int(filtered["Revenue (USD)"].sum())
avg_occ = round(float((filtered["Beds sold"].sum() / filtered["Beds available"].sum()) * 100), 1) if len(filtered) else 0
best = filtered.loc[filtered["Revenue (USD)"].idxmax()] if len(filtered) else None

rev_per_bed = round(total_revenue / filtered["Beds available"].sum(), 2) if len(filtered) else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total revenue (USD)", f"{total_revenue:,}")
col2.metric("Average occupancy %", avg_occ)
col3.metric("Best month", f"{best['Month']} ({best['Room type']})" if best is not None else "-")
col4.metric("Revenue per available bed (USD)", f"{rev_per_bed:,.2f}")

monthly = filtered.groupby("Month #", as_index=False).agg({"Revenue (USD)": "sum", "Beds sold": "sum"})
monthly["Month"] = monthly["Month #"].apply(lambda n: MONTHS[n - 1])

st.subheader("Revenue by month")
st.bar_chart(monthly.set_index("Month")["Revenue (USD)"])

st.subheader("Occupancy by room type")
occ = filtered.groupby("Room type", as_index=False)["Occupancy %"].mean()
st.bar_chart(occ.set_index("Room type")["Occupancy %"])

st.subheader("Data")
st.dataframe(filtered.drop(columns=["Month #"]), use_container_width=True, hide_index=True)

csv = filtered.drop(columns=["Month #"]).to_csv(index=False).encode("utf-8")
st.download_button(
    "Download filtered data (CSV)",
    csv,
    "hostel_occupancy.csv",
    "text/csv",
)

st.caption("Sample data for demonstration only — figures are illustrative, not real business data.")
