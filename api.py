import sys, requests, json

url = "https://kawabii.github.io/Python_API/data.json"
response = requests.get(url)

try:
    data = response.json()
except Exception as e:
    print("Erreur JSON :", e)
    print("Contenu reçu :", response.text[:300])
    exit()

id_recherche = int(sys.argv[1]) if len(sys.argv) > 1 else None
film = next((item for item in data if item["id"] == id_recherche), None)

print(json.dumps(film, indent=2, ensure_ascii=False) if film else "ID non trouvé.")
