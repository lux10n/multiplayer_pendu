import Pyro4,unidecode
chooser_model={
    'name':'',
    'word':'',
    'pending_arr':[]
}
player_model={
    'name':'',
    'tries':3,
    'found_arr':[]
}

@Pyro4.expose
class Game(object):
    def __init__(self):
        self.Chooser=None
        self.Player=None
    def register_chooser(self,Chooser):
        self.Chooser=Chooser
    def register_player(self,Player):
        self.Player=Player
    def chooser(self):return self.Chooser
    def player(self):return self.Player
    def chooser_name(self):return self.Chooser['name']
    def player_name(self):return self.Player['name']
    def get_word(self):return self.Chooser['word']
    def get_tries(self):return self.Player['tries']
    def get_pending_array(self):return self.Chooser['pending_arr']
    def get_found_array(self):return self.Player['found_arr']
    def set_found(self,ar):self.Player['found_arr']=ar
    def set_pending(self,ar):self.Chooser['pending_arr']=ar
    def set_word(self,word):
        self.Chooser['word']=unidecode.unidecode(word.upper())
        self.set_pending(list(self.get_word()))
    def set_tries(self,tries):self.Player['tries']=tries
    def generate_pattern(self):
        wd=''
        for letter in self.get_word():
            if letter in self.get_found_array():
                wd+='{} '.format(letter)
            else:
                wd+=' _ '
        return wd[:-1]
    def check_letter(self,letter):
        if self.get_tries()!=0:
            if letter in self.get_word():
                self.reset()
                while letter in self.get_word():
                    try:
                        p_arr=self.get_pending_array()
                        p_arr.remove(letter)
                        self.set_pending(p_arr)
                    except:break
                f_arr=self.get_found_array()
                f_arr.append(letter)
                self.set_found(f_arr)
                return True
            else:
                self.fail_once()
                return False
    def reset(self):
        self.set_tries(3)
    def fail_once(self):
            if self.get_tries()>0:
                self.set_tries(self.get_tries()-1)
            else:
                self.set_tries(0)
