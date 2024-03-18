



![[misc/Media/Pasted image 20240311150528.png|misc/Media/Pasted image 20240311150528.png]]

ERM steht für **Entity Relationship Modell**


## Begriffe 


#### Entität vs Entitätstyp 

Wird das drankommen, weil es wäre interessant zu wissen? 

#### Geschäftsregeln aufstellen 

- Entities und ihre Eigenschaften zueinander bestimmen 
- Regeln und Bedingungen beschreiben (z.B. müssen für einen Schüler jeweils ein Name oder ein Geburtsdatum exisiteren oder ist das optional)

#### Primärschlüssel 

Ein eindeutiger Indikator für eine bestimmte Tabelle. Sie kann aus einem oder mehrere Attribute bestehen und  

#### Kardinalitäten

Es gibt 3 Typen von Kardinalitäten: 

- 1-1: Bei dieser Art von Beziehung  hängt das sehr stark vom Kontext ab, wenn du vom ERM zum DRM wechselst. Du kannst eventuel hier Dinge zusammenfassen 
- 1-n: Hierbei ist es einfach was zutun ist. Der Primärschlüssel der 1er Seite wird zum Fremdschlüssel der n Seite. Bsp. kannst du bei einem Schüler den Primärschlüssel des Tutors als Fremdschlüssel für ein Schüler einfügen. 
- n-m: Die Relation wird hierbei zur Entität, wobei es die Primärschlüsseln der beiden Relationspartnern als Fremd-und Primärschlüssel gleichzeitig nimmt. 

#### Optionalitäten
Sie sind vor allem für die **Externe Ebene** wichtig und beschreiben die minimale bzw. die Maximale Anzahl einer 

Mehr Infos bei [[Informatik/Q2/Q2.1/ERM/Übungen zu ERM|Übungen zu ERM]]