#Mit eingaben rechnen mit int() Funktion
print('Geben Sie eine zahl ein die mi sich selbst multiplizieren soll')
spam=input() #die Reihenfolge ist wichtig sonst kommt es zu einer Fehlermeldung
spam=int(spam)
print(str(int(spam)) +' mal '+ str(int(spam)) +' Ergebniss')
print(spam*spam)

#Aufrunden wenn man es müssen

zahl= int(7.7)+1
print(zahl)

#Nach dem ALter fragen

print('Wie alt bist du ?')
myAge=input()

print('Du wirst '+str(int (myAge)+1)+ ' in einem Jahr sein.')
#Man kann auch im print vor dem myAge ein int hinzufügen, damit erkennt
#das Programm das es Keine Zeichenkette ist, sonderen eine Ganzzahl
#Somit kann man gegebenfalls rechenen wie in dem Beispiel

#Wichtig in Python
# 42=='42' ist FALSCH
# 42=42,0 ist WAHR
# 42,0 == 0.042,000 ist WAHR