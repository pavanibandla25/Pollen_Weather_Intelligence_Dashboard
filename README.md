<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen">
  <img src="https://img.shields.io/badge/Data-DWD%20Pollen%20API-purple">
  <img src="https://img.shields.io/badge/Data-Meteo%20Weather%20API-blueviolet">
</p>

# 🌿 Pollen & Weather Intelligence Dashboard

⭐ Real‑time pollen and weather forecasting for allergy‑aware decision making across German cities.

# Live Demo 

click here_for app_preview : https://pollen-weather-dashboard.streamlit.app
## 🎞️ Presentation (Canva)

👉 Click here to view the full Canva presentation:(https://canva.link/sqdp0rbbevcsw2n)


# 📌 Overview

⭐The Pollen & Weather Intelligence Dashboard combines pollen forecasts and weather data into a single, interactive Streamlit application.
It helps users — especially those with allergies — understand:

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


# 🌦️ Features
✅ Today’s Pollen Overview
- Grass, Birch, Alder, and other pollen types

- Severity levels (Low / Moderate / High / Very High)

- Color‑coded indicators

# 📅 2‑Day Pollen Forecast
- Real‑time pollen predictions from DWD

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

# 🧠 Tech Stack
- Component	Technology
- Frontend	Streamlit
- Backend	Python
- Data	DWD Pollen API, Meteo Weather API
- Visualization	Matplotlib, Seaborn
- Deployment	Streamlit Cloud
- Version Control	Git & GitHub


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

- Add user‑selected city dropdown

- Add automated daily scraping with GitHub Actions

- Add machine‑learning based pollen prediction

# 👩‍💻 Author
Pavani Bandla  
Data Analyst | Python | SQL | Streamlit | APIs
👉 GitHub: pavanibandla25  
👉 LinkedIn: pavani-bandla-893a76402
