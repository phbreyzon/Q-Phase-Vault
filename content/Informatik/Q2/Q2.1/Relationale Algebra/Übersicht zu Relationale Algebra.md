## Operatoren 

**Um die folgenden drei Operatoren nutzen zu können, gilt die Voraussetzung der sog *Einigungsverträglichkeit***

##### Einigungsverträglichkeit
Eine Einigungsverträglichkeit gilt, wenn die Attribute zwischen den Tabellen übereinstimmen, bzw. gleich sind. Wenn eine Relation $R$ die Attribute $A,B,C$ hat und eine Relation $S$ ebenfalls die Attribute $A,B,C$ hat, dann sind sie vereinigungsverträglich. 


### Durchschnitt 
Der Durchschnitt $N$, wobei es dann so geschrieben wird $N = R \cap S$ ist die Menge an **Tupeln**, also Zeilen, die sowohl in der Relation $R$ als auch in der Relation $S$ vorhanden sind. 

![[misc/Media/Relationale Algebra 2024-03-12 18.35.26.excalidraw|misc/Media/Relationale Algebra 2024-03-12 18.35.26.excalidraw]]
### Vereinigung 
Die Vereinigung ist im Grunde genommen ein *Natural-join*, nur mit Vereinigungsveträglichkeit, wird wie folgt aufgeschrieben $N = R \cup S$ und so in der Praxis sieht es so aus: 

![[misc/Media/Relationale Algebra 2024-03-12 18.44.16.excalidraw|misc/Media/Relationale Algebra 2024-03-12 18.44.16.excalidraw]]


### Differenz 
Die Differenz ist genau das Gegenteil des Durchschnitts. Es zeigt die Tupeln an, die zwar in R sind, aber nicht in S vorkommen. Hierbei die Reihenfolge beim Aufschreiben wichtig. $N = R \textbackslash S$.

***
**(Ab hier ist die Vereinigungsveträglichkeit nicht notwendig)**


### Kartesische Produkt 
Das kartesische Produkt bildet alle möglichen Kombinationen aller Tupeln von $R$ und $S$. 


### Division *(kann sein, dass es drankommt)*
Die Division $N = R \div S$  gibt alle Tupel aus $R$ zurück, die in jeder Kombination mit den Tupeln aus $S$ vorkommen. 
Also es schaut, welche Tupeln aus $R$ ein kartesisches Produkt mit $S$ gebildet haben und gibt dieses aus.

![[misc/Media/Relationale Algebra 2024-03-12 19.08.31.excalidraw|misc/Media/Relationale Algebra 2024-03-12 19.08.31.excalidraw]]

### Selektion und Projektion
Die *Selektion* $N = \sigma{_\text{Bedingung}}(R)$ gibt alle Tupeln aus $R$ aus, die eine bestimmte Bedingung erfüllen. 
Die *Projektion* $N = \pi{_\text{Attribut,Attribut,...}(R)}$ projeziert die unter dem Pi definierten Attribute sowie all ihre Tupeln.


### Join (nur der *Naturaljoin*)

Der Join ist eine Kombination aus Operation, nämlich der Bildung eines kartesischen Produkts, Selektion und Projektion.  Er wird so geschrieben $N = R \bowtie{_\text{Bedingung}} S$ oder man kann die Bedingung weglassen, dann hat man nämlich ein selfjoin, was in den meisten Fällen der Normalfall sein muss. 

*Bedingung für ein Join ist, dass bestimmte Spalten den gleichen Inhalt haben müssen*

![[misc/Media/Relationale Algebra 2024-03-12 19.26.14.excalidraw|misc/Media/Relationale Algebra 2024-03-12 19.26.14.excalidraw]]

### Umbenennung 
Ziemlich selbsterklärend, es ändert die Bezeichnung eines Attributes und wird wie folgt aufgeschrieben $N = \rho{_{\text{[neu} \leftarrow \text{alt]}} }(R)$


Zu Übungen ziehe [[Informatik/Q2/Q2.1/Relationale Algebra/Übungen zu RA|Übungen zu RA]]




