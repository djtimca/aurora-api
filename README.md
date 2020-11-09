# Aurora API (auroranoaa)

PyPi integration to support the Home Assistant Aurora integration.

## Available Methods

### get_forecast_data(longitude:float, latitude:float)

Request the NOAA Aurora forecast for the given longitude and latitude.

Return value will be an integer of the forecast % chance of there being an Aurora event at the given coordinates.