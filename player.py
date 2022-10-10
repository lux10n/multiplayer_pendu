import Pyro4,time
from classes import *

if __name__=='__main__':
    gm=Pyro4.Proxy("PYRO:test.game@localhost:5150")
    gm.register_player(None)
    name=input('Nom du joueur > ')
    local_player=player_model
    local_player['name']=name
    gm.register_player(local_player)        
    while gm.chooser()==None:
        print('En attente du deuxième joueur...',end='\r')
        time.sleep(1)
    print('Joueur {} connecté !                 '.format(gm.chooser()['name']))
    while gm.get_word()=='':
        print('En attente du mot...',end='\r')
        time.sleep(1)
    while (gm.get_tries() >0) :
        if len(gm.get_pending_array())==0:
            print('Vous avez gagné la partie !')
            print('Le mot était : {}'.format(gm.get_word()))
            break
        print('Chances restantes : {}'.format(gm.get_tries()))
        print(gm.generate_pattern())
        letter=input('Entrez une lettre > ')
        while len(letter)!=1:
            letter=input('Entrez une lettre > ')
        if gm.check_letter(letter.upper()):
            print('Correct !')
        else:
            print('Incorrect !')
    if gm.get_tries()==0:
        print('Vous avez perdu la partie!\nLe mot était : {}'.format(gm.get_word()))
    input('Apppuyez sur une touche pour quitter...')
    gm.register_player(None)
