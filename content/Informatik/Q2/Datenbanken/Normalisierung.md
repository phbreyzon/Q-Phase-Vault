Die Normalisierung ist die Änderung eines Schemas, so dass bestimmte Regeln erfüllt werden, um beispielsweise eine Datenbank für ein bestimmtes Standard zertifizieren zu lassen.

Ziele sind unteran  derem: 
- [[Anomalien|Anomalien]] zu vermeiden
- Datenredudanz vermeiden (mehrfache Speicherung der gleichen Informationen)
- eine strukturierte und übersichtliches Design zu schaffen 

## Fachbegriffe 

### Funktionelle Abhängigkeit 
Ein Attribut $B$ ist von $A$ funktional abhängig ($B \rightarrow A$), wenn $A$ eindeutig den Wert des Attributs $B$ bestimmt.

##### Beispiel für funktionale Abhängigkeit:
In einer Tabelle "Schüler" mit den Attributen "SchülerID", "Name" und "Geburtsdatum" hängt der Name des Schülers eindeutig von der SchülerID ab. Jede SchülerID hat nur einen zugehörigen Namen.

##### Beispiel für fehlende funktionale Abhängigkeit:
In einer Tabelle "Bestellungen" mit den Attributen "Bestellnummer", "Kunde" und "Produkt" hängt der Kunde nicht eindeutig von der Bestellnummer ab. Ein Kunde kann mehrere Bestellungen aufgeben.

### Transitive Abhängigkeit 
Ist ein Attribut $B$ funktional abhängig von $A$  ($B \rightarrow A$) und ein Attribut $C$ ist funktional abhängig  von $B$ ($C \rightarrow B$), dann ist auch $C$ funktional abhängig von $A$ ($C \rightarrow A$). Man sagt dann, dass $C$ transitiv abhängig von $A$ ist.

## Normalisierungsstuffen 

### Nullte Normalform 
Jede Tabelle lieht zunächst in der nullten Normalform vor. 
In dieser Normalform kann es Zellen geben mit mehreren Werten, die durch Komata gretrennt werden. 

### Erste Normalform 
Bedingung für die erste Normalform sind:  
- dass alle Werte **atomar** vorkommen, d.h.  in jeder Zelle der Tabelle gibt es nur einen einzigen Wert. 
- Desweiteren **muss der Primärschlüssel eindeutig sein**

### Zweite Normalform 
Bedingungen sind: 
- Die erste Normalform muss bereits vorhanden sein 
- Jedes Attribut (A) ist vom gesamten Primärschlüssel (P) *(also auch wenn es aus mehreren Attributen besteht)* funktionell abhängig ($A \rightarrow P$). D.h. Die Attribute $A$ sind dann funktionell abhängig von $P$, wenn jedes $P$ genau einem Wert von $A$ gehört.



### Dritte Normalform 
Bedingungen dafür sind: 
- Eine Relation befindet sich schon in der 2.NF 
- Es gibt **keine** transitiven Abhängikeiten zwischen **Nicht-Schlüssel-Attributen**. bspw. 

![[misc/Media/Pasted image 20240312223912.png|misc/Media/Pasted image 20240312223912.png]]



### Boyce-Codd-Normalform 
Sie muss sich in der 3NF befinden und es dürfen keine transitiven abhängigkeiten zwischen Schlüssel-Attribute geben. Bei einem SchlüsselAttribut ist das Zeug ziemlich schnell gegessen. 
