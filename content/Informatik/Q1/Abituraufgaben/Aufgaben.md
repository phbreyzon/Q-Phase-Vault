### Beschreiben Sie die Klasse Route des UML-Diagramms

![[misc/Media/LA23-INF-LK-AJ-AUFG.pdf|misc/Media/LA23-INF-LK-AJ-AUFG.pdf]]

Die Klasse Route besitzt die Argumente:
- dieAdresse (Adresse[])
- Entfernung (double[][])
- optionalRoute ( int[])
- Länge (double)
Und die Methoden:
- Route(): Mit den Argumenten ...
- usw...
  
### Zeichnen Sie die Beziehungen zwischen den Klassen in das Diagramm ein und erläutern Sie diese.

![[misc/Media/Aufgaben 2023-11-22 08.50.26.excalidraw|misc/Media/Aufgaben 2023-11-22 08.50.26.excalidraw]]

Zwischen der Klasse Route und der Klasse Adresse besteht eine Aggregation in Richtung der Route, denn eine Route hat eine Adresse als Argument, sowie eine Adresse[] als Argument in seinem Konstruktor. Dementsprechend lässt sich daraus ziehen, dass mindestens eine Aggregation bestehen muss. usw...

### Die Pakete werden vor jeder Auslieferungstour gescannt und in die Packliste eingefügt. Bei der Zustellung werden die Pakete erneut gescannt und aus der Packliste entfernt. Implementieren Sie die Methoden *entferneErstesPaket()* und *entfernePaket(…)* der Klasse Packliste.

```Java
public void entferneErstesPaket(){
	Packet destination = erstesPacket.getNächstesPacket();
	erstesPacket.setNächstes(null);
	this.erstesPaket = destination;
}

public void entfernePacket( String diePacketnummer){
	Packet pointer = this.erstesPacket;
	for(int i = 0; i < this.ermittleAnzahl(); i++){
		if(pointer = this.letztesPacket()){
		break;
		}
		else if(pointer.getNächstesPacket().getPaketNr().equals(diePacketnummer)){
			Packet destination = pointer.getNächstesPacket.getNächstesPacket();
			pointer.getNächstesPacket.setNächstesPacket(null);
			pointer.setNächstesPacket(destination);
		}
		else{
			pointer = pointer.getNächstesPaket();
		}
		
	}
}
```


