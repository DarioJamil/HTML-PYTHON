import requests

# divisas = {"usd" : 1.09,
#            "mxn": 21.62,
#            "gbp": 0.83,
#            "mad": 10.73
#            }

# currencies api
url = "https://api.exchangeratesapi.io/v1/latest?access_key=ff5eb8a884445d69456c3ffa12ffd952&base="

base = input("Introduce divisa base (por ejemplo, USD): ").upper()
cant = float(input("Cantidad: "))
div = input("Introduce la divisa a convertir (por ejemplo, EUR): ").upper()

# try:
#     resp = requests.get(url + base)
#     data = resp.json()
#     divisas = data["rates"]
# except:
#     print("Ha habido un error")

# if div in divisas.keys():
#     result = divisas[div] * cant 
#     print (f"Resultado: {result}")

try:
    # Realizamos la solicitud a la API
    resp = requests.get(url + base)

    # Verificamos si la respuesta es exitosa
    if resp.status_code == 200:
        data = resp.json()
        divisas = data.get("rates")

        # Verificamos si la divisa solicitada está disponible
        if div in divisas:
            result = divisas[div] * cant
            print(f"Resultado: {cant} {base} = {result:.2f} {div}")
        else:
            print(f"La divisa '{div}' no está disponible.")
    else:
        print(f"Error al realizar la solicitud. Código de estado: {resp.status_code}")

except Exception as e:
    print(f"Ha habido un error: {e}")