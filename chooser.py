import Pyro4,time

from classes import *
if __name__=='__main__':
    gm=Pyro4.Proxy("PYRO:test.game@localhost:5150")
    gm.register_chooser(None)
    name=input('Nom du joueur > ')
    local_chooser=chooser_model
    local_chooser['name']=name
    gm.register_chooser(local_chooser)        
    while gm.player()==None:
        print('En attente du deuxième joueur...',end='\r')
        time.sleep(1)
    print('Joueur {} connecté !                 '.format(gm.player()['name']))
    word=input('Entrez le Mot > ')
    local_chooser['word']=word
    gm.set_word(word)
    while (gm.get_tries() >0) :
        if len(gm.get_pending_array())==0:
            print('Vous avez perdu la partie !')
            print('Le mot était : {}'.format(gm.get_word()))
            break
        print('Chances restantes de {} : {}'.format(gm.player_name(),gm.get_tries()))
        print('Progression : '+gm.generate_pattern())
        time.sleep(2)
    if gm.get_tries()==0:
        print('Vous avez gagné la partie!')
        print('Le mot était : {}'.format(gm.get_word()))
    input('Apppuyez sur une touche pour quitter...')
    gm.register_chooser(None)

