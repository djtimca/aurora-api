"""API Wrapper for NOAA Aurora 30 Minute Forecast."""
import logging
import aiohttp
import json

APIUrl = "https://services.swpc.noaa.gov/json/ovation_aurora_latest.json"

_LOGGER = logging.getLogger("aurora")

class AuroraForecast:
  def __init__(self, session:aiohttp.ClientSession=None):
    """Initialize and test the session"""

    self.retry = 5

    if session:
        self._session = session
    else:
        self._session = aiohttp.ClientSession()
  
  async def close(self):
    await self._session.close()

  async def get_forecast_data(self, longitude:float, latitude:float):
    """Return a dict of the requested forecast data."""
    
    forecast_dict = {}

    async with await self._session.get(APIUrl) as resp:
        forecast_data = await resp.text()

    forecast_data = json.loads(forecast_data)

    for forecast_item in forecast_data["coordinates"]:
        forecast_dict[forecast_item[0], forecast_item[1]] = forecast_item[2]

    return forecast_dict.get((int(longitude), int(latitude)),0)
    