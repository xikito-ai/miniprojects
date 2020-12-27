source=input("Wer hat dich hier hergeleitet?: ")
user=input("Dein Name: ")
adj1=input("Gebe ein Adjektiv ein: ")
adj2=input("Gebe ein weiteres Adjektiv ein: ") +"en"
adj3=input("Gebe noch ein Adjektiv ein: ")
nom1=input("Nomen: ")
verb1=input("Verb: ")
organ1=input("Gebe ein Organ an (lol): ")
times=int(input("Gebe eine Anzahl an: "))
motivation=input("Nun gebe bitte einen kleinen Satz ein, den du mir gerne sagen willst: ")

#f method to print the text with input int {}
print(f"Hey ho! Hier ist {source}. Ich wollte dir, {user} nur sagen wie {adj1} ich bin, dass es dich gibt! \n"
      f"Während dieser {adj2} Coronazeit ist es besonders {adj3}, dass man {nom1} hält. \n"
      f"Daher wollte ich dir nur kurz meine Aufmerksamkeit hier geben und {verb1}, dass du in meinem/r {organ1} bist! \n"
      f"Love you {times}! {motivation}!")
