import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.cache_data.clear()

# ============================
# PAGE CONFIG
# ============================
st.set_page_config(page_title="Pollen & Weather", layout="wide")

# ============================
# NUMERIC MAPPING
# ============================
level_to_num = {
    "None": 0,
    "Very Low": 1,
    "Low": 2,
    "Moderate": 3,
    "High": 4,
    "Very High": 5
}

# ============================
# GLOBAL CSS
# ============================
st.markdown("""
<style>
.pollen-number {
    font-size: 26px;
    font-weight: 700;
    color: black;
    text-align: center;
    width: 100%;
    margin-bottom: -4px;
}
.green-pill {
    background-color: #E8F5E9;
    color: #1B5E20;
    padding: 3px 8px;
    border-radius: 6px;
    font-weight: 500;
    font-size: 13px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}
.green-arrow {
    color: #1B5E20;
    font-size: 16px;
    font-weight: 600;
}
.after-today-line {
    width: 100%;
    border-bottom: 1px solid #E5E7EB;
    margin-top: 20px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ============================
# LOAD CSV FILES
# ============================
pollen_df = pd.read_csv("Data/dwd_pollen_5day.csv")
weather_df = pd.read_csv("Data/meteo_weather_5day.csv")

combined_7_df = pd.read_csv("Data/combined_7days.csv")
combined_7_df["date"] = pd.to_datetime(combined_7_df["date"])

# ============================
# FIX POLLEN COLUMNS
# ============================
pollen_cols = ["Hazel", "Alder", "Birch", "Grass", "Ragweed", "Mugwort"]
pollen_df[pollen_cols] = pollen_df[pollen_cols].fillna("None").astype(str)

# ============================
# CLEAN CITY NAMES
# ============================
for df in [pollen_df, weather_df, combined_7_df]:
    df["city"] = df["city"].str.strip()

# ============================
# COMBINE CITY LISTS
# ============================
cities = sorted(list(set(pollen_df["city"].unique()) | set(combined_7_df["city"].unique())))

# ============================
# SIDEBAR
# ============================
st.sidebar.markdown("""
<div style='margin-bottom:20px; line-height:1.2;'>
    <div style='font-size:26px; font-weight:800; color:black;'>🌿 Pollen &</div>
    <div style='font-size:24px; font-weight:800; color:black; margin-left:8px;'>Weather</div>
</div>
""", unsafe_allow_html=True)

selected_city = st.sidebar.selectbox("Select a city", cities)

# ============================
# PAGE TITLE
# ============================
st.markdown(
    f"""
    <h1 style='font-weight:800; margin-bottom:10px;'>
        <span style='color:#0B8A42;'>{selected_city}</span> – Pollen & Weather Forecast
    </h1>
    """,
    unsafe_allow_html=True
)

# ============================
# FILTER DATA
# ============================
pollen_city = pollen_df[pollen_df["city"] == selected_city].reset_index(drop=True)
weather_city = weather_df[weather_df["city"] == selected_city].reset_index(drop=True)
past7_city = combined_7_df[combined_7_df["city"] == selected_city].reset_index(drop=True)

today_pollen = pollen_city.iloc[0]
today_weather = weather_city.iloc[0]

# ============================
# TODAY OVERVIEW
# ============================
st.markdown("<h2 style='font-weight:800;'>Today Overview</h2>", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

# GRASS
with col1:
    st.markdown(
        f"""
        <div style='text-align:center;'>
            <div style='font-weight:600;'>🌾 Grass pollen</div>
            <div class='pollen-number'>{level_to_num.get(today_pollen['Grass'], 0)}</div>
            <div class='green-pill'>{today_pollen['Grass']} <span class='green-arrow'>↑</span></div>
        </div>
        """,
        unsafe_allow_html=True
    )

# BIRCH
with col2:
    st.markdown(
        f"""
        <div style='text-align:center;'>
            <div style='font-weight:600;'>🌳 Birch pollen</div>
            <div class='pollen-number'>{level_to_num.get(today_pollen['Birch'], 0)}</div>
            <div class='green-pill'>{today_pollen['Birch']} <span class='green-arrow'>↑</span></div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ALDER
with col3:
    st.markdown(
        f"""
        <div style='text-align:center;'>
            <div style='font-weight:600;'>🌿 Alder pollen</div>
            <div class='pollen-number'>{level_to_num.get(today_pollen['Alder'], 0)}</div>
            <div class='green-pill'>{today_pollen['Alder']} <span class='green-arrow'>↑</span></div>
        </div>
        """,
        unsafe_allow_html=True
    )

# TEMPERATURE
with col4:
    st.markdown(
        f"""
        <div style='text-align:center;'>
            <div style='font-weight:600;'>🌡 Temperature</div>
            <div class='pollen-number'>{today_weather['temp_max']} / {today_weather['temp_min']}</div>
            <div class='green-pill'>{today_weather['temp_max']}° / {today_weather['temp_min']}° <span class='green-arrow'>↑</span></div>
        </div>
        """,
        unsafe_allow_html=True
    )

# PRECIPITATION
with col5:
    st.markdown(
        f"""
        <div style='text-align:center;'>
            <div style='font-weight:600;'>💧 Rain</div>
            <div class='pollen-number'>{today_weather['rain_sum']}</div>
            <div class='green-pill'>{today_weather['rain_sum']} mm <span class='green-arrow'>↑</span></div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<div class='after-today-line'></div>", unsafe_allow_html=True)

# ============================
# 2-DAY POLLEN TABLE
# ============================
st.markdown("<h2 style='font-weight:800;'>🌾 2‑Day Pollen Forecast</h2>", unsafe_allow_html=True)

def normalize_level(value):
    v = str(value).strip()
    return "None" if v in ["", "nan"] else v

def level_style(val):
    v = normalize_level(val)
    colors = {
        "None": "#F2F3F4; color:#555555",
        "Very Low": "#E8F5E9; color:#1B5E20",
        "Low": "#C8E6C9; color:#1B5E20",
        "Moderate": "#FFF9DB; color:#B7950B",
        "High": "#FFE6CC; color:#D35400",
        "Very High": "#FDEDEC; color:#C0392B"
    }
    return f"background-color:{colors.get(v, '')}; font-weight:600;"

pollen_table = pollen_city[["date"] + pollen_cols].copy()
for col in pollen_cols:
    pollen_table[col] = pollen_table[col].apply(normalize_level)

styled_pollen = pollen_table.style.apply(
    lambda col: col.map(level_style),
    subset=pollen_cols
)

st.dataframe(styled_pollen, use_container_width=True)

st.markdown("<div class='after-today-line'></div>", unsafe_allow_html=True)

# ============================
# 🌦️ BEAUTIFUL 7‑DAY WEATHER TABLE
# ============================
def wind_direction_label(deg):
    if deg >= 337 or deg < 22: return f"{deg}° N"
    if deg < 67: return f"{deg}° NE"
    if deg < 112: return f"{deg}° E"
    if deg < 157: return f"{deg}° SE"
    if deg < 202: return f"{deg}° S"
    if deg < 247: return f"{deg}° SW"
    if deg < 292: return f"{deg}° W"
    return f"{deg}° NW"

st.markdown("<h2 style='font-weight:800;'>🌦️ 7‑Day Weather Forecast</h2>", unsafe_allow_html=True)

weather_cols = ["date", "temp_max", "temp_min", "rain_sum", "wind_max", "wind_direction"]

weather_table = weather_city[weather_cols].copy()

# ROUND VALUES
weather_table["temp_max"] = weather_table["temp_max"].round().astype(int)
weather_table["temp_min"] = weather_table["temp_min"].round().astype(int)
weather_table["rain_sum"] = weather_table["rain_sum"].round(1)
weather_table["wind_max"] = weather_table["wind_max"].round().astype(int)

# WEATHER ICONS
def temp_icon(t):
    if t >= 28: return "🔥"
    if t >= 22: return "☀️"
    if t >= 15: return "⛅"
    if t >= 8:  return "🌥️"
    return "❄️"

def rain_icon(r):
    if r == 0: return "—"
    if r < 1: return "🌦️"
    if r < 5: return "🌧️"
    return "⛈️"

def wind_arrow(deg):
    if deg >= 337 or deg < 22: return "↑"
    if deg < 67: return "↗"
    if deg < 112: return "→"
    if deg < 157: return "↘"
    if deg < 202: return "↓"
    if deg < 247: return "↙"
    if deg < 292: return "←"
    return "↖"

# APPLY ICONS
weather_table["temp_max"] = weather_table["temp_max"].astype(str) + "°C " + weather_table["temp_max"].apply(temp_icon)
weather_table["temp_min"] = weather_table["temp_min"].astype(str) + "°C"
weather_table["rain_sum"] = weather_table["rain_sum"].astype(str) + " mm " + weather_table["rain_sum"].apply(rain_icon)
weather_table["wind_max"] = weather_table["wind_max"].astype(str) + " km/h"
weather_table["wind_direction"] = weather_table["wind_direction"].apply(wind_direction_label)


# COLOR STYLING
def weather_style(val):
    if "🔥" in str(val): return "background-color:#FFEBEE; font-weight:600;"     # hot
    if "☀️" in str(val): return "background-color:#FFF8E1; font-weight:600;"     # warm
    if "⛅" in str(val): return "background-color:#E3F2FD; font-weight:600;"     # mild
    if "❄️" in str(val): return "background-color:#E1F5FE; font-weight:600;"     # cold
    if "🌧️" in str(val) or "⛈️" in str(val): return "background-color:#E0F7FA;"  # rain
    return "background-color:#F7F9F9; font-weight:600;"

styled_weather = weather_table.style.map(weather_style)
st.dataframe(styled_weather, use_container_width=True)

st.markdown("<div class='after-today-line'></div>", unsafe_allow_html=True)


# ============================
# 7-DAY TRENDS
# ============================
st.markdown("<h2 style='font-weight:800;'>📈 Past 7‑Day Pollen & Weather Trends</h2>", unsafe_allow_html=True)

# 🌡️ Grass vs Temperature
st.markdown("### 🌡️ Grass Pollen vs Temperature")
fig = go.Figure()
fig.add_trace(go.Scatter(x=past7_city["date"], y=past7_city["grass_pollen"], mode="lines+markers", name="Grass Pollen", line=dict(color="green")))
fig.add_trace(go.Scatter(x=past7_city["date"], y=past7_city["temperature"], mode="lines+markers", name="Temperature (°C)", line=dict(color="red"), yaxis="y2"))
fig.update_layout(xaxis_title="Date", yaxis=dict(title="Grass Pollen"), yaxis2=dict(title="Temperature (°C)", overlaying="y", side="right"), template="simple_white")
st.plotly_chart(fig, use_container_width=True)

# 🌬️ Grass vs Wind
st.markdown("### 🌬️ Grass Pollen vs Wind Speed")
fig = go.Figure()
fig.add_trace(go.Scatter(x=past7_city["date"], y=past7_city["grass_pollen"], mode="lines+markers", name="Grass Pollen", line=dict(color="green")))
fig.add_trace(go.Scatter(x=past7_city["date"], y=past7_city["wind_speed"], mode="lines+markers", name="Wind Speed (km/h)", line=dict(color="blue"), yaxis="y2"))
fig.update_layout(xaxis_title="Date", yaxis=dict(title="Grass Pollen"), yaxis2=dict(title="Wind Speed (km/h)", overlaying="y", side="right"), template="simple_white")
st.plotly_chart(fig, use_container_width=True)

# 🌧️ Grass vs Rain
st.markdown("### 🌧️ Grass Pollen vs Rain")
fig = go.Figure()
fig.add_trace(go.Scatter(x=past7_city["date"], y=past7_city["grass_pollen"], mode="lines+markers", name="Grass Pollen", line=dict(color="green")))
fig.add_trace(go.Scatter(x=past7_city["date"], y=past7_city["precipitation"], name="Rain (mm)", marker_color="skyblue", yaxis="y2"))
fig.update_layout(xaxis_title="Date", yaxis=dict(title="Grass Pollen"), yaxis2=dict(title="Rain (mm)", overlaying="y", side="right"), template="simple_white")
st.plotly_chart(fig, use_container_width=True)
