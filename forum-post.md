# Streamlit forum — "Show the Community" post (for Ram's account, posting 2026-11-09)

**Title:** Hostel Occupancy Dashboard — my first Streamlit app

**Body:**

Hi everyone,

I'm Ram, a web developer (mostly JavaScript/React) based in Los Angeles, and I'm new to Streamlit. I wanted to share the first app I've built and deployed on Community Cloud:

**Hostel Occupancy Dashboard**
Live app: https://hostel-occupancy-dashboard.streamlit.app/
Code: https://github.com/Ramprashadmahato/hostel-occupancy-dashboard

I previously built a hostel management system in React, so I used this app to explore the analytics side of the same problem: occupancy, revenue and room-type performance across the year. It has sidebar filters for room type and month range, headline metrics (total revenue, average occupancy, best month, revenue per available bed), revenue-by-month and occupancy-by-room-type charts, and a CSV export of the filtered data.

A note on the data: it currently runs on a small built-in sample dataset for demonstration. My next step is to move the data into Snowflake and connect the app to real SQL queries instead of the sample data, then add parameterized filters by room type and month.

I also built a small companion app while learning: a Nepal Travel Data Explorer (https://nepal-travel-data-explorer.streamlit.app/) with region/type filters, ratings and elevation charts, and a map.

I'd genuinely welcome feedback — especially on layout, and on best practices for connecting Streamlit to Snowflake. Thanks!
