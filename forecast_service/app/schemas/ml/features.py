from pydantic import BaseModel, Field


class Feature(BaseModel):
    values: list[float]
    dates: list[str]


class IPPFeatures(BaseModel):
    news:           Feature = Field(None, description="Новостной идекс ЦБ, Россия")
    cb_monitor:     Feature = Field(None, description="Оценка изменения спроса на продукцию, товары, услуги (промышленность), пункты, Россия")
    business_clim:  Feature = Field(None, description="Промышленность Индикатор бизнес-климата Банка России")
    interest_rate:  Feature = Field(None, description="Ключевая ставка ")
    rzd:            Feature = Field(None, description="Погрузка на сети РЖД")
    consumer_price: Feature = Field(None, description="Индекс цен на электроэнергию в первой ценовой зоне")
    curs:           Feature = Field(None, description="Курс рубля к доллару США")


class IPCFeatures(BaseModel):
    news:           Feature = Field(None, description="Новостной идекс ЦБ, Россия")
    cb_monitor:     Feature = Field(None, description="Оценка изменения спроса на продукцию, товары, услуги (промышленность), пункты, Россия")
    business_clim:  Feature = Field(None, description="Промышленность Индикатор бизнес-климата Банка России")
    interest_rate:  Feature = Field(None, description="Ключевая ставка ")
    rzd:            Feature = Field(None, description="Погрузка на сети РЖД")
    consumer_price: Feature = Field(None, description="Индекс цен на электроэнергию в первой ценовой зоне")
    curs:           Feature = Field(None, description="Курс рубля к доллару США")
