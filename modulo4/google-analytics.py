from collections import defaultdict
from auth import ga_auth
import polars as pl

# Definimos los scopes necesarios para acceder a Google Analytics
scopes = ['https://www.googleapis.com/auth/analytics.readonly']
# Autenticamos con Google Analytics usando la función ga_auth
analytics = ga_auth(scopes)

# ID de la propiedad de Google Analytics
property_id = '274438246'
# Definimos las dimensiones que queremos obtener
dimensions = [
  'date',
  'sessionSourceMedium'
  ]
# Definimos las métricas que queremos obtener
metrics = [
  'sessions',
  'transactions',
  'purchaseRevenue'
  ]
# Creamos la solicitud para la API de Google Analytics.
# Especificamos el rango de fechas, las dimensiones, las métricas y el límite de filas.

request = {
  "requests": [
    {
      "dateRanges": [
        {
          "startDate": "2025-01-01",
          "endDate": "2025-01-05"
        }
      ],
      "dimensions": [{'name': name} for name in dimensions],
      "metrics": [{'name': name} for name in metrics],
      "limit": 250000
    }
  ]
}

# Ejecutamos la solicitud a la API de Google Analytics
response = analytics.properties().batchRunReports(property=f'properties/{property_id}', body=request).execute()
# Creamos un diccionario para almacenar los datos del reporte
report_data = defaultdict(list)
# Iteramos sobre los reportes y las filas del reporte
for report in response.get('reports', []):
    rows = report.get('rows', [])
    for row in rows:
        for i, key in enumerate(dimensions):
            report_data[key].append(row.get('dimensionValues', [])[i]['value'])  # Obtenemos las dimensiones
        for i, key in enumerate(metrics):
            report_data[key].append(row.get('metricValues', [])[i]['value'])  # Obtenemos las métricas

# Creamos un DataFrame de Polars con los datos del reporte y lo imprimimos
df = pl.DataFrame(report_data)
print(df) 
