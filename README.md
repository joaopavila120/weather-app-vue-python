# Weather Dashboard

A simple Vue 3 weather dashboard that fetches current weather and a 5‑day forecast from the OpenWeatherMap API. Built with Vue.

## Features

- **Proxy Server (Flask)** for OpenWeatherMap:
  - Caching: in-memory caching (10 min for weather/forecast, 5 min for search)
  - Rate Limiting: 50 requests/hour (weather & forecast), 30 requests/minute (search)
  - Modular Structure: Blueprints for routes
  - CORS Enabled: allows frontend to access backend seamlessly

## Prerequisites

- Node.js (v14+)  
- An OpenWeatherMap API key

## Setup

 **Clone the repo**  
   ```bash
   git clone https://github.com/joaopavila120/weather-app-vue-python.git
   cd weather-app-vue-python
   ```

 **frontend**  
   ```bash
   npm install
   ```

 **Start the development server**  
   ```bash
   npm run dev
   ```
   Open your localhost

## Backend
```bash
cd server
pip install -r requirements.txt
python app.py
```

Note: The API key is intentionally exposed in the .env file for testing purposes. You don’t need to hide it in this demo repo—just follow the steps, run the backend and frontend, and test away!

## Printscreen: 
<img width="1295" height="865" alt="image" src="https://github.com/user-attachments/assets/86154b81-f929-4e84-89e5-08f082723d1b" />

