Die Kettenregel lautet in ihrer allgemeinen Form $f'(x) = u'(v(x)) \cdot v'(x)$. Hierbei ist die originale Funktion eine Verkettung aus einer äußeren und einer inneren Funktion $f(x) = u(v(x))$.

## Herleitung

Um die Kettenregel zu Beweisen setzt man die Funktion zuerst wie jede andere Funktion in die H-Methode ein:
$$\lim_{h \to 0} \frac{u(v(x+h)) - u(v(x))}{h}$$


dabei will man ein Ergebnis bekommen, welches der ursprünglichen Regel nahe kommt, deshalb wird hierbei ein kleiner Trick angewendet:

$$\lim_{h \to 0} \frac{u(v(x+h)) - u(v(x))}{h} \cdot \frac{v(x+h) -v(x)}{v(x+h) - v(x)}$$

Hierbei wurde der Funktion einen „weiteren“ Wert hinzugefügt, welches aber an den Term an sich nichts ändert, denn $a \cdot \frac{b}{b} = a$. Im nächsten Schritt wird ein weiterer Trick angewendet:

$$\lim_{h \to 0} \frac{u(v(x+h)) - u(v(x))}{v(x+h) - v(x)} \cdot \frac{v(x+h) -v(x)}{h}$$

In diesem Schritt wurde der folgende Trick angewendet: $\frac{a}{b} \cdot \frac{c}{d}= \frac{a}{d} \cdot \frac{c}{b}$ wobei die unteren Teile des Bruchs miteinander vertauscht wurden. Der zweiter Term ($\frac{v(x) -v(x+h)}{h}$) gibt uns mit dem Einsatz vom Limes $v'(x)$. Der erste Term bleibt bestehen. Jetzt kann man den folgenden Abschnitt abstrahieren in: 
$$ v(x) = v_{0}$$
$$v(x+h) = v_1$$

Man muss dabei bedenken, dass die Abstrahierung am Ende wieder umgekehrt werden muss, um das richtige Ergebnis zu bekommen. Zusammengefasst sieht der erste Term nun so aus: 

$$\lim_{h \to 0} \frac{u(v_1) - u(v_0)}{v_{1}- v_0}$$

Mit den vereinfachten Term lässt sich der Differenzialquotient erkennen, der wie folgt lautet: $\lim_{x \to x_{0}} \frac{f(x) - f(x_{0})}{x-x_{0}}$. Mit dieser Formel lässt sich die Ableitung (bzw. Steigung) an dem Punkt $x_0$ ausrechnen. In diesem Fall wird also folgendes berechnet: 

$$\lim_{v_{1} \to v_{0}} \frac{u(v_1) - u(v_0)}{v_{1}- v_{0}}= u'(v_{0})$$

Um mit der Rechnung abzuschließen, muss man die Abstrahierung wieder umkehren, also $v_{0}= v(x)$. Zusammenfassend erhält anschließend folgendes: 

$$ u'(v(x)) \cdot v'(x)$$
somit ist die Kettenregel beweisen