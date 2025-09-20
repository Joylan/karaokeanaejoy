import csv

def load_songs(file_path='musicas.csv'):
    songs = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            songs.append({
                "id": row["codigo"],
                "artist": row["cantor"],
                "song": row["musicas"]
            })
    return songs

songs = load_songs()