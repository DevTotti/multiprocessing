from fastapi import FastAPI, HTTPException, Depends, Query
import httpx
import asyncio
import time

app = FastAPI()

MAX_REQUESTS = 100 # Maximum number of requests allowed
TIME_WINDOW = 60  # in seconds
request_count = 0
start_time = time.time()

# Middleware rate limiting function
def rate_limiter():
    global request_count, start_time

    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > TIME_WINDOW:
        request_count = 0
        start_time = current_time

    if request_count >= MAX_REQUESTS:
        raise HTTPException(status_code=429, detail="Rate limit exceeded.")
    
    request_count += 1

async def fetch_data_from_api(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Raise an error if the response was not 200 OK
            return response.json()
    except httpx.HTTPStatusError as e:
        return {"error": f"Failed to fetch data from {url}: {e.response.status_code}"}
    except httpx.RequestError as e:
        return {"error": f"Request error for {url}: {str(e)}"}

# Endpoint that uses various free APIs to fetch data on food, animals, weather, countries, and sports
@app.get("/aggregate-data")
async def aggregate_data(rate_limiter: None = Depends(rate_limiter)):
    api_urls = [
        "https://www.themealdb.com/api/json/v1/1/random.php",  # Food: random meal
        "https://dog.ceo/api/breeds/image/random",             # Animals: random dog image
        "https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&current_weather=true",  # Weather: NYC weather
        "https://restcountries.com/v3.1/name/Canada",          # Countries: info about Canada
        "https://www.thesportsdb.com/api/v1/json/3/eventsseason.php?id=4328&s=2022-2023"              # Sports: recent basketball games
    ]

    # Gather data from all APIs concurrently
    results = await asyncio.gather(*(fetch_data_from_api(url) for url in api_urls))
    return {
        "food": results[0],
        "animals": results[1],
        "weather": results[2],
        "countries": results[3],
        "sports": results[4]
    }
