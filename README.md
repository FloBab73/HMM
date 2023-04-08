# HMM
Gruppe: Florian Babel, Johannes Welsch, Tom Witzel

## Benutzung
- __main.py__ in src/ ausführen und Ergebnisse anschauen
- Die Dateien __hmm_observation.json__ und __hmm_simple.json__ müssen dafür in res/ liegen
- Die Ausgabe besteht aus folgenden Punkten:
  - __probability__ gibt die Wahrscheinlichkeit für die Beobachtung an
  - __best states__ gibt die Zustände an, die den wahrscheinlichsten Weg für die Beobachtung ausmachen
  - __absolute maximum probability__ gibt die absolute Wahrscheinlichkeit dieses Wegs an
  - __relative maximum probability__ gibt die Wahrscheinlichkeit an, unter Wahrscheinlichkeit, dass die Beobachtung gemacht wurde

## Funktion
Die Main ruft alle Bestandteile des Programms auf. Die Read ist nur fürs einlesen der JSON Dateien zuständig. Die Daten werden im Model gespeichert. Die States und Observations bekommen eigene Datenstrukturen, um leichter sowohl auf die Namen, als auch die Indices zuzugreifen.
In Evaluate ist der Forward implementiert, der die Wahrscheinlichkeit für die gegebene Observation ausrechnet. Die Funktion hat die drei Abschnitte Initialization, Recursion und Termination. Das Programm arbeitet sich Rückwärts bis zu Rekursionsbasis (Initialization), von der es sich wieder Hocharbeitet und alle Werte berechnet.
In Decode ist der Viterbi Algorithmus implementiert, der die wahrscheinlichste Zustandskette für die gegebene Beobachtung berechnet. Dafür wird der Forward Algorithmus so abgeändert, dass statt den Summe das Maximum gesucht wird. Zusätzlich wird eine Liste der Zustände übergeben, um am Ende nicht nur die Wahrscheinlichkeit für den Wahrscheinlichsten Weg zu sehen, sondern als die Zustände, die diesen Weg ausmachen.