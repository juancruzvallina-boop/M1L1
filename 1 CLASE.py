meme_dict = {
            "EFIMERO": "algo que dura muy poco tiempo",
            "INEFABLE": "algo tan increibel o especial que no se puede explicar con palabras",
            "RANDOM":"una palabra que describe algo alatorio",
            "INERTE":"que no tiene movimiento ni vida",
            "MELANCOLIA":"tristeza suave o sensacion de nostalgia"
            }
word=input("escribe una palabra que quieras buscar,en mayusculas")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabr
    print("no eh encontrado su palabra,pero trabajare en eso")
