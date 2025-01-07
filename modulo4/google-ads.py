from gaarf.report_fetcher import AdsReportFetcher
from gaarf import GoogleAdsApiClient
import polars as pl

# Inicializar el cliente desde una credencial local
client = GoogleAdsApiClient(path_to_config="google-ads.yaml")
report_fetcher = AdsReportFetcher(client)

# Para crear la consulta puedes revisar la documentación oficial de la API de Google Ads
# https://developers.google.com/google-ads/api/fields/v18/overview_query_builder
query_text = """
SELECT
    segments.date,
    campaign.name,
    metrics.cost_micros,
    metrics.impressions,
    metrics.clicks
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
"""

# Puedes especificar los id de las cuentas explicitamente
customer_ids = ['5286026647']
# O expandir sobre un MCC para iterar por cada cuenta.
# customer_ids = report_fetcher.expand_mcc('1234567890')
report = report_fetcher.fetch(query_text, customer_ids)
df = pl.from_pandas(report.to_pandas())
print(df)