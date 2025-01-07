from collections import defaultdict
from auth import ga_auth
import polars as pl

def ga_data(property_id, start_date, end_date, dimensions, metrics, filter_expr=None):
    """
    Obtiene datos de Google Analytics 4 con la opción de filtrar resultados.
    
    Parámetros:
        property_id (str): ID de la propiedad de GA4
        start_date (str): Fecha inicial en formato 'YYYY-MM-DD'
        end_date (str): Fecha final en formato 'YYYY-MM-DD'
        dimensions (list): Lista de dimensiones a consultar
        metrics (list): Lista de métricas a consultar
        filter_expr (dict, opcional): Diccionario con la expresión de filtro
            Ejemplo de estructura:
            {
                "fieldName": "sessionSourceMedium",
                "stringFilter": {
                    "matchType": "BEGINS_WITH",
                    "value": "aw_"
                }
            }
    
    Returns:
        DataFrame: Datos obtenidos en formato Polars DataFrame
    """
    # Configuración básica
    analytics = ga_auth(['https://www.googleapis.com/auth/analytics.readonly'])
    
    # Crear solicitud base
    request = {
        "requests": [{
            "dateRanges": [{
                "startDate": start_date,
                "endDate": end_date
            }],
            "dimensions": [{"name": dim} for dim in dimensions],
            "metrics": [{"name": met} for met in metrics],
            "limit": 250000
        }]
    }
    
    # Agregar filtro si se especifica
    if filter_expr:
        request["requests"][0]["dimensionFilter"] = {
            "filter": filter_expr
        }
    
    # Obtener datos
    response = analytics.properties().batchRunReports(
        property=f'properties/{property_id}', 
        body=request
    ).execute()
    
    # Procesar respuesta
    data = defaultdict(list)
    for row in response['reports'][0]['rows']:
        # Agregar dimensiones
        for dim, value in zip(dimensions, row['dimensionValues']):
            data[dim].append(value['value'])
        # Agregar métricas
        for met, value in zip(metrics, row['metricValues']):
            data[met].append(value['value'])
            
    return pl.DataFrame(data)

# Ejemplo de uso: filtrar solo campañas que empiecen con "aw_"
# Documentación para filtros: https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/FilterExpression?hl=es-419
filtro_campanas = {
    "fieldName": "sessionCampaignName",
    "stringFilter": {
        "matchType": "PARTIAL_REGEXP",
        "value": "^aw(-|_)"
    }
}

# Obtener datos filtrados
df = ga_data(
    property_id='274438246',
    start_date='2025-01-01',
    end_date='2025-01-05',
    # Documentación dimensiones y métricas: https://ga-dev-tools.google/ga4/dimensions-metrics-explorer
    dimensions=['date', 'sessionSourceMedium', 'sessionCampaignName'],
    metrics=['sessions', 'transactions', 'purchaseRevenue'],
    filter_expr=filtro_campanas
)

print(df)