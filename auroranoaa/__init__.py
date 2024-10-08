"""API Wrapper for NOAA Aurora 30 Minute Forecast."""

import asyncio
import json
import logging
import time

import aiohttp
from aiohttp import ClientError

APIUrl = "https://services.swpc.noaa.gov/json/ovation_aurora_latest.json"

_LOGGER = logging.getLogger("aurora")


class AuroraForecast:
    forecast_dict = {}
    last_update_time = None
    lock = asyncio.Lock()

    def __init__(self, session: aiohttp.ClientSession = None):
        """Initialize and test the session."""

        self.retry = 5

        if session:
            self._session = session
        else:
            self._session = aiohttp.ClientSession()

    async def close(self):
        await self._session.close()

    async def get_forecast_data(self, longitude: float, latitude: float):
        """Return a forecast probability for the given coordinates."""

        # acquire the lock to ensure that only one request is processed at a time
        await AuroraForecast.lock.acquire()

        try:
            longitude = (
                longitude % 360
            )  # Convert -180 to 180 to 360 longitudinal values

            # Check if the forecast data is older than 5 minutes
            if AuroraForecast.last_update_time is None or (
                AuroraForecast.last_update_time
                and time.monotonic() - AuroraForecast.last_update_time > 5 * 60
            ):
                AuroraForecast.forecast_dict = {}

                _LOGGER.debug("Fetching forecast data from NOAA")
                try:
                    async with await self._session.get(APIUrl) as resp:
                        forecast_data = await resp.text()
                        forecast_data = json.loads(forecast_data)

                        for forecast_item in forecast_data["coordinates"]:
                            if forecast_item[2] > 0:
                                AuroraForecast.forecast_dict[
                                    forecast_item[0], forecast_item[1]
                                ] = forecast_item[2]

                        # update the time of the last update
                        AuroraForecast.last_update_time = time.monotonic()
                        _LOGGER.debug("Successfully fetched forecast data from NOAA")

                except ClientError as error:
                    _LOGGER.debug("Error fetching forecast from NOAA: %s", error)

            probability = AuroraForecast.forecast_dict.get(
                (round(longitude), round(latitude)), 0
            )
            _LOGGER.debug(
                "Forecast probability: %s at (long, lat) = (%s, %s)",
                probability,
                round(longitude),
                round(latitude),
            )
            return probability

        finally:
            # release the lock to allow other requests to be processed
            AuroraForecast.lock.release()
