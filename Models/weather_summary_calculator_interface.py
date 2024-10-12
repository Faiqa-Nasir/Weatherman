from abc import ABC,abstractmethod

class IWeatherSummaryCalculator(ABC):
    @abstractmethod
    def yearly_min_temp(self,weather_info:list):
        pass 
    @abstractmethod
    def yearly_max_temp(self,weather_info:list):
        pass 
    @abstractmethod
    def yearly_max_humidity(self,weather_info:list):
        pass 
    @abstractmethod
    def monthly_min_temp(self,weather_info:list):
        pass 
    @abstractmethod
    def monthly_max_temp(self,weather_info:list):
        pass 
    @abstractmethod
    def monthly_max_humidity(self,weather_info:list):
        pass 
    
    
    