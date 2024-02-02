import numpy as np
import os

try:
    with open("Dumpfile.txt", encoding="utf8") as fh:
        res = fh.read()
except FileNotFoundError:
    print("Le fichier n'existe pas %s", os.path.abspath('fichieratraiter.txt'))

ress = res.split('\n')

tableau_evenements = np.array([])
fic = open("coco.csv", "w")

evenement = "DATE;SOURCE;PORT;DESTINATION;FLAG;SEQ;ACK;WIN;OPTIONS;LENGTH"
fic.write(evenement + "\n")

characters = ":"

for event in ress:
    if event.startswith('11:42'):
        seq = ""
        heure1 = ""
        nomip = ""
        port = ""
        flag = ""
        ack = ""
        win = ""
        options = ""
        length = ""

        # ... (rest of your code)

        # Add checks for potential issues or vulnerabilities
        if flag == "SYN" and ack == "":  # Check for SYN without ACK
            print("Potential SYN Flood Attack Detected!")

        if flag == "FIN" and ack == "":
            print("Potential FIN without ACK Detected!")

        if flag == "ACK" and seq == "":  # Check for ACK without SEQ
            print("Potential ACK without SEQ Detected!")

        # You can add more checks based on your specific requirements


fic.close()
