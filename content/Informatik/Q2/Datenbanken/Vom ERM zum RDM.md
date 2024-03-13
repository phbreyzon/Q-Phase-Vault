### Grundregeln 

- Jeder Entitätstyp wird zu einer eigenen Relation (Tabelle) 
- Jeder Beziehungstyp (relationship) wird ebenfalls zu einer Relation. 
- Bei den Beziehungstypen werden die beiden Primärschlüssel der beteiligten Entitätstypen zu Fremdschlüsseln und Primätschlüssel im Relationschema des Beziehungstypen.
  
  ![[misc/Media/Pasted image 20240312202234.png|misc/Media/Pasted image 20240312202234.png]]
![[misc/Media/Pasted image 20240312202341.png|misc/Media/Pasted image 20240312202341.png]]

Wenn der Beziehungstyp $R$ und die beiden beteiligten Entytätstypen $A$ und $B$ gegeben sind, dann gilt
#### m:n Beziehung: 
Muss $R(\uparrow{\underline{a},\uparrow\underline{b}})$ wenn $A(\underline{a},\text{c})$ , $B(\underline{b},\text{d})$

#### 1:1 Beziehung:
$a$ oder $b$ können ein Primärschlüssel sein, da für beide Attribute gilt, dass ein Wert einmal in der Relation vorkommt. Es ist also kontextabhängig, was am geeignetsten ist 

#### 1:n Beziehung: 
Das selbe gilt bei 1:1, nämlich, dass die Beziehungstabelle oder sogar eine der beiden Entitätstabellen ganz wegfallen kann. Bei dem Fall, dass eine Entitätstabelle wegfällt werden alle Attribute auf die andere Seite “importiert”.
Ansonsten gilt bei 1:n, wenn $A$ die 1-Seite ist und $B$ die n-Seite ist:  $A(\underline{a},c)$, $B(\uparrow \text{a}, \underline{b},d, \text{"Weitere Attribute des Beziehungsstypen",...})$ 

 