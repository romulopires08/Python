import requests
import pandas as pd

def get_coordinates_bing(address, api_key):
    base_url = "http://dev.virtualearth.net/REST/v1/Locations"
    params = {
        "q": address,
        "key": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get("resourceSets") and data["resourceSets"][0].get("resources"):
            resource = data["resourceSets"][0]["resources"][0]
            coordinates = resource["point"]["coordinates"]
            longitude, latitude = coordinates
            return latitude, longitude
    else:
        print("Error:", response.status_code)
    return None

# Ler endereço a partir do excel 
excel_file = "moradas_teste_python.xlsx"  
df = pd.read_excel(excel_file)

# Key do Bing Maps
bing_api_key = "USER_API"  #Insert here the correct API

# Guarda resultados
results = []

# Iteração colunas com o Bing Maps API
for index, row in df.iterrows():
    nome = row ['nome']
    morada = row['morada']
    cod_postal = row['cod. postal']
    #pais = row['pais']

    full_address = f"{nome}, {morada}, {cod_postal}"
    coordinates = get_coordinates_bing(full_address, bing_api_key)

    if coordinates:
        latitude, longitude = coordinates
        results.append({
            "Address": full_address,
            "Longitude": longitude,
            "Latitude": latitude
        })

# Criar a DataFrame a partir dos resutados
results_df = pd.DataFrame(results)

# Escrever em um arquivo de excel
output_excel = "geocoded_results_bing4.xlsx"
results_df.to_excel(output_excel, index=False)

print("Geocoded results saved to:", output_excel)
print (results_df)
