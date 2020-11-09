# Aurora API (aurora-noaa)

PyPi integration to support the Home Assistant Aurora integration.

## Available Methods

### get_forecast_data(longitude:float, latitude:float)

Request the NOAA Aurora forecast for the given longitude and latitude.

Return value will be an integer of the forecast:
- 0 - 0% Chance
- 1 ~ 20% Chance
- 2 ~ 40% Chance
- 3 ~ 60% Chance
- 4 ~ 80% Chance
- >4 ~ 90+% Chance
