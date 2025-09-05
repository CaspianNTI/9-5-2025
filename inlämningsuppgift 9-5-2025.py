#Prompt:
#jag vill skriva ett program som använder [att spara] för att mata in två tal. 
# Programet ska sedan skriva ut summan. 
# Programet ska använda [att upprepa] för att fortsätta köra tills att användaren skriver "stopp".

while True:  # [att upprepa]
    tal1 = input("Mata in det första talet (eller skriv 'stopp' för att avsluta): ")  # [att spara]
    if tal1.lower() == "stopp": # [att välja]
        break
    tal2 = input("Mata in det andra talet (eller skriv 'stopp' för att avsluta): ")  # [att spara]
    if tal2.lower() == "stopp": # [att välja]
        break
    summa = float(tal1) + float(tal2)  # [att spara]
    print("Summan är:", summa)

#Copilots beskrivning:

#Programmet använder alla tre fraserna: [att spara], [att upprepa] och [att välja].

#[att spara] används för att ta emot två tal från användaren och spara dem i variablerna tal1 och tal2. Summan av dessa tal sparas också i variabeln summa.
#[att upprepa] används genom en while True-loop, vilket gör att programmet fortsätter att fråga efter nya tal tills användaren skriver "stopp".
#[att välja] används med hjälp av två if-satser. Programmet väljer att antingen fortsätta eller avsluta beroende på om användaren skriver "stopp".
#Varje gång två tal matas in, räknar programmet ut och skriver ut deras summa. Om användaren skriver "stopp" istället för ett tal, avslutas programmet.