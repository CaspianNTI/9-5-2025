# att spara: Läs in två tal och spara dem i variablerna 'tal1' och 'tal2'
tal1 = float(input("Ange det första talet: "))
tal2 = float(input("Ange det andra talet: "))

# att välja: Jämför talen och skriv ut vilket som är störst
if tal1 > tal2:
    print("Det första talet är störst:", tal1)
elif tal2 > tal1:
    print("Det andra talet är störst:", tal2)
else:
    print("Talen är lika stora.")