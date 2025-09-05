# Skrivet av gemini
# Prompts: 

# jag vill skriva ett program som använder [att spara] för att mata in två tal. 
# Programet ska sedan skriva ut summan. 
# Programet ska använda [att upprepa] för att fortsätta köra tills att användaren skriver "stopp".

# kan använda [att välja] också

while True: # [att upprepa] – fortsätter köra tills 'break' aktiveras
    print("Välkommen till min miniräknare!")
    print("Du kan välja mellan addition (+), subtraktion (-), multiplikation (*) och division (/).")
    print("Skriv 'stopp' när som helst för att avsluta programmet.")

    # [att spara] det första talet
    input1 = input("Ange det första talet: ")
    if input1.lower() == "stopp":
        break

    # [att spara] det andra talet
    input2 = input("Ange det andra talet: ")
    if input2.lower() == "stopp":
        break

    try:
        tal1 = float(input1)
        tal2 = float(input2)

        # [att välja] vilken operation som ska utföras
        operation = input("Välj operation (+, -, *, /): ")
        if operation.lower() == "stopp":
            break

        resultat = 0
        if operation == "+":
            resultat = tal1 + tal2
            print(f"Summan av {tal1} och {tal2} är: {resultat}\n")
        elif operation == "-":
            resultat = tal1 - tal2
            print(f"Differensen mellan {tal1} och {tal2} är: {resultat}\n")
        elif operation == "*":
            resultat = tal1 * tal2
            print(f"Produkten av {tal1} och {tal2} är: {resultat}\n")
        elif operation == "/":
            if tal2 != 0: # Viktigt att kontrollera division med noll!
                resultat = tal1 / tal2
                print(f"Kvoten av {tal1} och {tal2} är: {resultat}\n")
            else:
                print("Kan inte dividera med noll!\n")
        else:
            print("Ogiltig operation. Vänligen välj +, -, * eller /.\n")

    except ValueError:
        print("Ogiltig inmatning. Vänligen ange siffror eller 'stopp'.\n")

print("Programmet har avslutats.")

#Förklaring av [att välja]:
#operation = input("Välj operation (+, -, *, /): "): Här [sparar] vi användarens val av operation i variabeln operation.
#if operation == "+": ... elif operation == "-": ... else: ...: Detta är kärnan i hur vi använder [att välja]. Programmet kontrollerar värdet på operation och kör sedan den kodblock som motsvarar det valda alternativet.
#if står för "om" och kontrollerar det första villkoret.
#elif står för "else if" ("annars om") och kontrollerar efterföljande villkor om det första inte var sant.
#else står för "annars" och körs om inget av de föregående villkoren var sanna.
#if tal2 != 0:: En viktig [att välja]-kontroll vid division. Vi måste se till att användaren inte försöker dividera med noll, vilket skulle orsaka ett fel i programmet.