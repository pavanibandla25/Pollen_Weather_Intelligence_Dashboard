<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen">
  <img src="https://img.shields.io/badge/Data-DWD%20Pollen%20API-purple">
  <img src="https://img.shields.io/badge/Data-Meteo%20Weather%20API-blueviolet">
</p>

# 🌿 Pollen & Weather Intelligence Dashboard

⭐Real‑time pollen + weather insights for allergy‑aware decisions across German cities

# Live Demo :

🔗 Live App : https://pollen-weather-dashboard.streamlit.app

## 🎞️ Project Presentation (Canva):(https://canva.link/sqdp0rbbevcsw2n)


# 📌 Overview

⭐The Pollen & Weather Intelligence Dashboard is an interactive Streamlit application that brings together real‑time pollen forecasts, 5–7 day weather predictions, and historical correlation analysis for major German cities.

It is designed for:

- People with pollen allergies

- Families planning outdoor activities

- Anyone who wants clear, data‑driven environmental insights

  # The dashboard provides:
  
# city selection
  
👉 [Cities Dropdown](assets/cities_drop_down.png)

# Today’s pollen severity, 5‑day pollen forecast
  
👉 [📌 Pollen Today Overview](assets/pollen_today_overview.png)

# 7‑day weather forecast
 
👉 [7‑Day Weather Forecast](assets/7%20days_weather_forecast.png)


#  Historical grass-pollen vs. weather correlations

👉 [Grass vs Rain](assets/past7_grass_vs_rain.png)

👉 [Grass vs Wind](assets/passt7-grasspollen-vs-wind.png)

👉 [Grass vs Temperature](assets/past7_grass%20pollen-VS-temparature.png)

This dashboard is built using Python, Streamlit, Pandas, and API‑based data scraping.


# 🌦️ Key Features
✅ Today’s Pollen Overview
- Grass, Birch, Alder, and other pollen types

- Severity levels: Low → Very High

- Color‑coded indicators for quick understanding

# 📅 2‑Day Pollen Forecast
- Real‑time predictions from DWD Pollen API

- City‑wise comparison

- Clean, structured table view

# 🌤️ 5‑Day Weather Forecast
- Temperature (min/max)

- Rain probability

- Humidity

- Wind speed

# 📊 Historical Correlation Analysis
- Grass pollen vs. temperature

- Grass pollen vs. rain

- Grass pollen vs. wind

- 7‑day combined dataset

# 🏙️ Multi‑City Support
- Mannheim

- Heidelberg

- Karlsruhe

- Frankfurt

- Stuttgart

- Munich

- Berlin

# 🧠 Why This Project Matters
Pollen allergies affect millions across Europe — yet pollen and weather data are rarely shown together.
This dashboard solves that gap by offering a single, unified view that helps users make informed decisions about outdoor plans, health, and daily routines.

# 🧰 Tech Stack
| Component | Technology |
| --- | --- |
| **Frontend** | Streamlit |
| **Backend** | Python |
| **Data Sources** | DWD Pollen API, Meteo Weather API |
| **Visualization** | Matplotlib, Seaborn |
| **Deployment** | Streamlit Cloud |
| **Version Control** | Git & GitHub |


# 📁 Project Structure
Code
```
Pollen_Weather_Intelligence_Dashboard/
│
├── app/
│   └── app.py
│
├── data/
│   ├── combined_7days.csv
│   ├── dwd_pollen_5day.csv
│   └── meteo_weather_5day.csv
│
├── assets/
│   ├── pollen_today_overview.png
│   ├── past7_grass_vs_rain.png
│   ├── past7_grasspollen-vs-wind.png
│   ├── past7_grasspollen-vs-temperature.png
│   └── 7_days_weather_forecast.png
│
├── Notebooks/
│   ├── pollen_and_weather_scraping.ipynb
│   └── scraping_pollen_weather_History.ipynb
│
├── requirements.txt
└── README.md
````
# 🚀 How to Run Locally
1️⃣ Clone the repository
Code
👉 git clone https://github.com/pavanibandla25/Pollen_Weather_Intelligence_Dashboard.git

2️⃣ Install dependencies
Code
- pip install -r requirements.txt
 
3️⃣ Run the Streamlit app
Code
- streamlit run app/app.py
  
# 📡 Data Sources
- DWD (Deutscher Wetterdienst) – Pollen Forecast API

- Meteo API – Weather Forecast API

# 🎯 Future Enhancements

- Add AQI (Air Quality Index)

- Add more German cities

- Add automated daily scraping with GitHub Actions

- Add machine‑learning based pollen prediction

# 👩‍💻 Author
Pavani Bandla  
Data Analyst | Python | SQL | Streamlit | APIs

🔗 GitHub: https://github.com/pavanibandla25 (github.com in Bing)  
🔗 LinkedIn: https://www.linkedin.com/in/pavani-bandla-893a76402 (linkedin.com in Bing)
