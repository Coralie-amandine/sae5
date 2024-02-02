import pandas as pd

# Fonction pour détecter les requêtes ping
def detecter_ping(row):
    if "ping" in row["requete"].lower():
        return True
    return False

# Fonction pour détecter les attaques DDoS (exemple simple basé sur la fréquence des requêtes)
def detecter_ddos(row, seuil=100):
    if row["nombre_requetes"] > seuil:
        return True
    return False

# Charger le fichier CSV
nom_fichier = "C:/Users/amand/Music/Mon projet SAE15/EXCEL/coco.csv"
donnees = pd.read_csv(nom_fichier)

# Appliquer la détection des requêtes ping
donnees["ping_detecte"] = donnees.apply(detecter_ping, axis=1)

# Appliquer la détection des attaques DDoS
donnees["ddos_detecte"] = donnees.apply(detecter_ddos, axis=1)

# Afficher les résultats
print(donnees)
