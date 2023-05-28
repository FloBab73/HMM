# Hidden Markov Models
Prüfungsleistung für Digitale Sprachverarbeitung an der DHBW Karlsruhe

[Link zu Github](https://github.com/FloBab73/HMM)

Gruppe: Florian Babel, Johannes Welsch, Tom Witzel

## Benutzung
- __main.py__ in src/ ausführen und Ergebnisse in der Konsole anschauen
- Die Dateien __hmm_observation.json__ und __hmm_simple.json__ müssen dafür in res/ liegen
- Die Ausgabe besteht aus folgenden Punkten:
  - __forward probability__ gibt die Wahrscheinlichkeit für die Beobachtung an, wie sie der Forward Algorithmus ausgibt 
  - __viterbi states__ gibt die Zustände an, die den wahrscheinlichsten Weg für die Beobachtung ausmachen, wie sie der Viterbi Algorithmus ausgibt
  - __absolute viterbi probability__ gibt die absolute Wahrscheinlichkeit dieses Wegs an
  - __relative viterbi probability__ gibt die Wahrscheinlichkeit für den Weg an, unter der Voraussetzung, dass die Beobachtung gemacht wurde

Die beiden letzten Ausgaben sind Nebenprodukte des Viterbi Algorithmus und werden mit ausgegeben.

Für den gegebenen Input kommt folgendes Ergebnis heraus:

<img height="200" src="res\result.png" alt="Output of given observation"/>

## Funktion
Die Main ruft alle Bestandteile des Programms auf. Die _read.py_ ist nur fürs Einlesen der JSON Dateien zuständig. Die Daten werden im Model gespeichert. Die States und Observations bekommen eigene Datenstrukturen, um leichter sowohl auf die Namen, als auch die Indices zuzugreifen.

Die Funktionen wurden jeweils zweimal auf unterschiedliche Arten implementiert. Zuerst wurden die Funktionen rekursiv implementiert, wie es die Algorithmen vorgeben. Da auf dem Weg aber viele Werte mehrmals berechnet wurden, wurde der Algorithmus so geändert, dass alle Werte in einer Tabelle gespeichert werden. Außerdem hat die bisherige Implementierung des Viterbi Algorithmus nicht das korrekte Ergebnis geliefert. Daher sind im finalen Produkt die nicht rekursiven Funktion aktiv, die anderen sind aber noch im Code enthalten. Die folgenden Absätze beschreiben die rekursive Implementierung.

### Rekursive Implementierung

#### Evaluate
In _Evaluate.py_ ist der Forward Algo implementiert, der die Wahrscheinlichkeit für die gegebene Observation ausrechnet. Die Funktion hat die drei Abschnitte Initialization, Recursion und Termination. Das Programm arbeitet sich Rückwärts bis zu Rekursionsbasis (Initialization), von der es sich wieder Hocharbeitet und alle Werte berechnet.
Die Funktion wird mit der Länge der Observations als Zeit aufgerufen. In diesem Zustand wird der Termination Teil ausgeführt, der die Methode rekursiv aufruft. Dabei wird die Zeit um Eins dekrementiert und durch alle Zustände iteriert. Die Ergebnisse dieser Iteration werden aufaddiert und als Ergebnis zurückgegeben.
Während der rekursiven Aufrufe wird der Recursion Teil ausgeführt, wenn die Zeit zwischen 0 und der Länge der Observations liegt. Dabei wird die Funktion wieder rekursiv für alle Zustände aufgerufen, mit einer dekrementierten Zeit. Die Ergebnisse werden mit den Übergangswahrscheinlichkeiten von dem aufgerufenen Zustand zu dem aktuellen Zustand multipliziert. Nach dem Aufsummieren wird der Wert mit der Ausgabewahrscheinlichkeit von dem aktuellen Zustand von der aktuellen Observation multipliziert. In diesem Teil wird damit berechnet wie wahrscheinlich der aktuelle Zustand ist und mit welcher Wahrscheinlichkeit er den aktuellen Output ausgibt. 
Wenn die Zeit 0 erreicht, gibt es keine vorherigen Zustände. Daher wird die Anfangswahrscheinlichkeit für den aktuellen Zustand mit der Outputwahrscheinlichkeit des aktuellen Zustands für die erste Observation multipliziert. 

#### Decode
In _Decode.py_ ist der Viterbi Algorithmus implementiert, der die wahrscheinlichste Zustandskette für die gegebene Beobachtung berechnet. Dafür wird der Forward Algorithmus so abgeändert, dass statt der Summe das Maximum gesucht wird. Zusätzlich wird eine Liste der Zustände übergeben, um am Ende nicht nur die Wahrscheinlichkeit für den wahrscheinlichsten Weg zu sehen, sondern auch die Zustände, die diesen Weg ausmachen. Dabei ist darauf zu achten, dass immer die Zustände zeitlich vor dem aktuellen Zustand verglichen werden. Da es bei der Initialization keinen Zustand vorher gibt, wird nur eine leere Liste als Zustände zurückgegeben.

### Lineare Implementierung
Folgend wird auf die Implementierung mithilfe von Matrizen eingegangen, die Werte zwischenspeichern.

#### Evaluate
Eine Matrix speichert die bereits berechneten Werte, auf die die folgenden Berechnungen aufbauen. Die Abschnitte Initialization, Recursion und Termination bleiben erhalten. Auf jeder Stufe kommt dabei eine zusätzliche Schleife dazu, da die Iteration vor Ort und nicht über die Rekursion erfolgt. Ansonsten ist die Implementierung der Rekursiven sehr ähnlich.

#### Decode
Auch die Funktion gleicht sehr stark ihren Vorbildern. Hier gibt es eine weitere Matrix, die die States speichert, die für den jeweils aktuellen State der beste Vorgänger ist. Am Ende werden der beste Endzustand ausgewählt und da jeder Zustand einen besten Vorgänger hat, kann so die Kette ermittelt werden, die die höchste Wahrscheinlichkeit bietet.