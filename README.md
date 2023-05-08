# HMM
Gruppe: Florian Babel, Johannes Welsch, Tom Witzel

## Benutzung
- __main.py__ in src/ ausführen und Ergebnisse in der Konsole anschauen
- Die Dateien __hmm_observation.json__ und __hmm_simple.json__ müssen dafür in res/ liegen
- Die Ausgabe besteht aus folgenden Punkten:
  - __forward probability__ gibt die Wahrscheinlichkeit für die Beobachtung an, wie sie der Forward Algo ausgibt 
  - __viterbi states__ gibt die Zustände an, die den wahrscheinlichsten Weg für die Beobachtung ausmachen, wie sie der Viterbi Algo ausgibt
  - __absolute viterbi probability__ gibt die absolute Wahrscheinlichkeit dieses Wegs an
  - __relative viterbi probability__ gibt die Wahrscheinlichkeit für den Weg an, unter der Voraussetzung, dass die Beobachtung gemacht wurde

Die beiden letzten Ausgaben sind Nebenprodukte des Viterbi Algo und werden mit ausgegeben.

## Funktion
Die Main ruft alle Bestandteile des Programms auf. Die _read.py_ ist nur fürs Einlesen der JSON Dateien zuständig. Die Daten werden im Model gespeichert. Die States und Observations bekommen eigene Datenstrukturen, um leichter sowohl auf die Namen, als auch die Indices zuzugreifen.

In _Evaluate.py_ ist der Forward Algo implementiert, der die Wahrscheinlichkeit für die gegebene Observation ausrechnet. Die Funktion hat die drei Abschnitte Initialization, Recursion und Termination. Das Programm arbeitet sich Rückwärts bis zu Rekursionsbasis (Initialization), von der es sich wieder Hocharbeitet und alle Werte berechnet.
Die Funktion wird mit der Länge der Observations als Zeit aufgerufen. In diesem Zustand wird der Termination Teil ausgeführt, der die Methode Rekursiv aufruft. Da bei wird die Zeit um Eins dekrementiert und durch alle Zustände iteriert. Die Ergebnisse dieser Iteration werden aufaddiert und als Ergebnis zurückgegeben.
Während der rekursiven Aufrufe wird der Recursion Teil ausgeführt wenn die Zeit zwischen 0 und der Länge der Observations liegt. Dabei wird die Funktion wieder rekursiv für alle Zustände aufgerufen, mit einer dekrementierten Zeit. Die Ergebnisse werden mit den Übergangswahrscheinlichkeiten von dem aufgerufenen Zustand zu dem aktuellen Zustand multipliziert. Nach dem Aufsummieren wird der Wert mit der Ausgabewahrscheinlichkeit von dem aktuellen Zustand von der aktuellen Observation multipliziert. In diesem Teil wird damit berechnet wie wahrscheinlich der aktuelle Zustand ist und mit welcher Wahrscheinlichkeit er den aktuellen Output ausgibt. 
Wenn die Zeit 0 erreicht, gibt es keine vorherigen Zustände. Daher wird die Anfangswahrscheinlichkeit für den aktuellen Zustand mit den Outputwahrscheinlichkeit des aktuellen Zustands für die erste Observation multipliziert. 

In _Decode.py_ ist der Viterbi Algorithmus implementiert, der die wahrscheinlichste Zustandskette für die gegebene Beobachtung berechnet. Dafür wird der Forward Algorithmus so abgeändert, dass statt der Summe das Maximum gesucht wird. Zusätzlich wird eine Liste der Zustände übergeben, um am Ende nicht nur die Wahrscheinlichkeit für den wahrscheinlichsten Weg zu sehen, sondern auch die Zustände, die diesen Weg ausmachen. Dabei ist darauf zu achten, dass immer die Zustände zeitlich vor dem aktuellen Zustand verglichen werden. Da es bei der Initialization keinen Zustand vorher gibt wird nur eine leere Liste als Zustände zurückgegeben.