# -*- coding: utf-8 -*-
import datetime

# Chemin vers le fichier ICS
ics_file_path = 'C:/Users/amand/Music/Mon projet SAE15/TP1 SAE 1.5/PREMIER TRAVAIL/evenementSAE_15.ics'

# Fonction pour extraire les événements du fichier ICS
def extract_events(file_path):
    with open(file_path, 'r') as fh:
        content = fh.read()

    events = []
    current_event = []

    for line in content.split('\n'):
        if line.startswith('BEGIN:VEVENT'):
            current_event = []
        elif line.startswith('END:VEVENT'):
            events.append('\n'.join(current_event))
        else:
            current_event.append(line)

    return events

# Appel de la fonction et impression des événements
events = extract_events(ics_file_path)
for i, event in enumerate(events, start=1):
    print(f'Événement {i}:\n{event}\n{"="*30}\n')
