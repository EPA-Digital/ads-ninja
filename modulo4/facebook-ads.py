from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from dotenv import load_dotenv
import polars as pl
import os


# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Inicializar API
FacebookAdsApi.init(
    access_token=os.getenv('FB_ACCESS_TOKEN')
)

# Obtener cuenta
account_id = "1741832612768307"
fb_account = AdAccount(f"act_{account_id}")

# Definir campos y parámetros
# Para saber más sobre la API de insights de Facebook: https://developers.facebook.com/docs/marketing-api/insights
# Para concer los campos disponibles: https://developers.facebook.com/docs/marketing-api/reference/ad-account#campos
fields = [
    'campaign_name',
    'spend',
    'impressions',
    'clicks'
]
params = {
    'level': 'campaign',
    ## En caso de requerir filtros introducirlos usando el siguiente formato:
    ## {field:"ad.impressions",operator:"GREATER_THAN",value:0}
    # 'filtering': [],
    ## En caso de requerir breakdowns: https://developers.facebook.com/docs/marketing-api/insights/breakdowns
    # 'breakdowns': [],
    'time_range': {
        'since': '2025-01-01',
        'until': '2025-01-05'
        },
    'time_increment': '1'
}

# Obtener insights
insights = fb_account.get_insights(
    fields=fields,
    params=params
)

# Convertir a un DataFrame de polars
df = pl.DataFrame([insight.export_all_data() for insight in insights])
print(df)