from fastapi import APIRouter

from app.api.v1.schemas import (ForecastResponse, IPPRequest, FeatureRequest, FeatureResponse)
from app.domain.forecast_models import IPPForecast


forecast_router = APIRouter()


@forecast_router.get("/features_list")
async def features_list(request: FeatureRequest) -> FeatureResponse:
    """Получить список названий всех признаков необходимых для обучения модели"""
    
    

@forecast_router.get("/ipp")
async def ipp_forecast(request: IPPRequest) -> ForecastResponse:
    """Прогнозирование индекса промышленного производства

    Args:
        request (IPPRequest): необходимые параметры для запроса

    Returns:
        ForecastResponse: прогноз на 1, 2 и 3 месяца
    """
    
    model = IPPForecast(request.hparams)
    features = request.features
    
    model.set_data(
        goal=request.ipp, news=features.news, consumer_price=features.consumer_price,
        cb_monitor=features.cb_monitor, exchange_rate=features.exchange_rate, 
        bussines_clim=features.bussines_clim, curs=features.curs, rzd=features.rzd 
    )
    
    model.train()
    forecast = model.predict()
    
    forecast_response = ForecastResponse(*forecast)
    
    return forecast_response