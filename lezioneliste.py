lista=[4,6]
tupla= (4,6,-5) #es. un punto nello spazio 3D
#per creare un dizionario, si usano le graffe. Questo è un dizionario di studenti con chiave la matricola e valore il nome/cognome
diz_studenti={"015675": "Mario Rossi", "123456": "Gianni Verdi"}

lista_studenti= [["015675", "Mario Rossi"],
                 ["123456","Gianni Verdi"]  #questa è una tabella, cioè una lista di liste
                 ]

lista_matricole= ["015675", "123456"]
lista_nomi_cognomi= ["Mario Rossi", "Gianni Verdi"]

nuova_lista= lista_studenti #non copia la lista, ma ne crea solamente un alias quindi in memoria i dati non sono stati duplicati

copia_della_lista= list(nuova_lista)
