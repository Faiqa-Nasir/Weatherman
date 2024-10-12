from dataclasses import dataclass


@dataclass
class DailyWeatherDetails:
    pkt: str                       # PKT
    max_temperature_c: float       # Max TemperatureC
    mean_temperature_c: float      # Mean TemperatureC
    min_temperature_c: float       # Min TemperatureC
    dew_point_c: float             # Dew PointC
    mean_dew_point_c: float        # Mean Dew PointC
    min_dew_point_c: float         # Min DewpointC
    max_humidity: float            # Max Humidity
    mean_humidity: float           # Mean Humidity
    min_humidity: float            # Min Humidity
    max_sea_level_pressure_hpa: float  # Max Sea Level PressurehPa
    mean_sea_level_pressure_hpa: float  # Mean Sea Level PressurehPa
    min_sea_level_pressure_hpa: float  # Min Sea Level PressurehPa
    max_visibility_km: float       # Max VisibilityKm
    mean_visibility_km: float      # Mean VisibilityKm
    min_visibility_km: float       # Min VisibilitykM
    max_wind_speed_kmh: float      # Max Wind SpeedKm/h
    mean_wind_speed_kmh: float     # Mean Wind SpeedKm/h
    max_gust_speed_kmh: float      # Max Gust SpeedKm/h
    precipitation_mm: float         # Precipitationmm
    cloud_cover: float              # CloudCover
    events: str                    # Events
    wind_dir_degrees: float        # WindDirDegrees
