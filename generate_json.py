import csv
import json

csv_file = 'musicas.csv'
json_file = 'songs.json'

songs = []

with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        songs.append({
            "id": row["codigo"],
            "artist": row["cantor"],
            "song": row["musicas"]
        })

# Salva JSON compacto
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(songs, f, ensure_ascii=False, separators=(',', ':'))

print(f"Arquivo '{json_file}' gerado com {len(songs)} músicas.")