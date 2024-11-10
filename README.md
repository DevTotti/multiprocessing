# API Aggregator Microservice

This microservice aggregates data from multiple external APIs and provides it through a single endpoint. Built with FastAPI, it supports parallel processing for efficient data fetching and includes a rate limiter to control the number of requests allowed per minute.

## Features

- **Data Aggregation**: Retrieves data from various APIs (food, animals, weather, countries, and sports).
- **Parallel Processing**: Fetches data from APIs concurrently to reduce latency.
- **Rate Limiting**: Limits API requests to 100 per minute to prevent excessive usage.

## Technologies

- **FastAPI** for creating the API.
- **httpx** for asynchronous HTTP requests.
- **asyncio** for managing concurrent API calls.

## Endpoints

### `/aggregate-data`
- **Method**: `GET`
- **Description**: Returns aggregated data from multiple APIs in JSON format.
- **Rate Limit**: 100 requests per minute.

## APIs Used

- **Food**: [TheMealDB](https://www.themealdb.com/api.php) - Returns random meal information.
- **Animals**: [Dog CEO](https://dog.ceo/dog-api/) - Provides a random dog image.
- **Weather**: [Open-Meteo](https://open-meteo.com/) - Retrieves current weather for NYC.
- **Countries**: [REST Countries](https://restcountries.com/) - Retrieves data on Canada.
- **Sports**: [TheSportsDB](https://www.thesportsdb.com/) - Provides recent events from the English Premier League.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/DevTotti/multiprocessing
   cd multiprocessing

2. **Activate Virtual Environment**
   ```bash
   python3 -m venv .
   source ./bin/activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   
4. **Run the API**
   ```bash
   uvicorn main:app --reload

5. **Access the API Documentation**
   ```bash
   http://127.0.0.1:8000/docs


## Testing

 **Run Tests**
   ```bash
   PYTHONPATH=. pytest tests/