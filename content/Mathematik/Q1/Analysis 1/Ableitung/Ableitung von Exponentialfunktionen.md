Die Ableitung der Logarithmusfunktion lautet allgemein:

$$f(x) = \log_a(x)$$ $$f'(x) = \frac{1}{x\ln(a)}$$

Hierbei ist $a$ die Basis des Logarithmus.

Die Ableitung der Funktion des natürlichen Logarithmus lautet:
$$f(x) = \ln(x)$$ $$f'(x) = \frac{1}{x}$$
hierbei ist $e$ die Basis des Logarithmus.

## Herleitung

Die Ableitung lässt sich wie folgt mit der H-Methode berechnen:

1. Schritt: Schreibe die Funktion als $y = \ln(x)$.

2. Schritt: Ersetze $x$ durch $x + h$, wobei $h$ ein kleiner Wert ist, der gegen Null geht. Die neue Funktion lautet $y = \ln(x + h)$.

3. Schritt: Berechne die Differenz der beiden Funktionen:
$$f(x+h) - f(x) = \ln(x+h) - \ln(x)$$

4. Schritt: Wende die Logarithmusregel an, um die Differenz zu vereinfachen:
$$f(x+h) - f(x) = \ln \left(\frac{x+h}{x}\right)$$

5. Schritt: Bestimme den Grenzwert, wenn $h$ gegen Null geht. Dazu können wir den L'Hospital'schen Satz anwenden:
$$f'(x) = \lim_{h \to 0} \frac{\ln\left(\frac{x+h}{x}\right)}{h}$$

$$= \lim_{h \to 0} \frac{1}{h} \cdot \ln\left(\frac{x+h}{x}\right)$$

$$= \lim_{h \to 0} \frac{1}{h} \cdot \left(\ln(x+h) - \ln(x)\right)$$

$$= \lim_{h \to 0} \frac{1}{h} \cdot \ln\left(1 + \frac{h}{x}\right)$$

6. Schritt: Wende die Ableitungsregel für den natürlichen Logarithmus an:
$$f'(x) = \lim_{h \to 0} \frac{1}{h} \cdot \ln\left(1 + \frac{h}{x}\right)$$

$$= \lim_{h \to 0} \frac{\ln\left(1 + \frac{h}{x}\right)}{\frac{h}{x}} \cdot \frac{1}{x}$$

$$= \frac{1}{x} \cdot \lim_{h \to 0} \frac{\ln\left(1 + \frac{h}{x}\right)}{\frac{h}{x}}$$

7. Schritt: Wende erneut den L'Hospital'schen Satz an:
$$f'(x) = \frac{1}{x} \cdot \lim_{h \to 0} \frac{\frac{1}{1+\frac{h}{x}} \cdot \frac{1}{x}}{\frac{1}{x^2}}$$

$$= \frac{1}{x} \cdot \lim_{h \to 0} \frac{x}{x+h}$$

$$= \frac{1}{x}$$

Daher ist die Ableitung der natürlichen Logarithmusfunktion $f'(x) = \frac{1}{x}$.