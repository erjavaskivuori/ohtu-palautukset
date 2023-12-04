class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen = 0

    def miinus(self, operandi):
        self._edellinen = self._arvo
        self._arvo -= operandi

    def plus(self, operandi):
        self._edellinen = self._arvo
        self._arvo += operandi

    def nollaa(self):
        self._edellinen = self._arvo
        self._arvo = 0

    def kumoa(self):
        self._arvo = self._edellinen

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    

class Summa():
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self, arvo):
        self.sovellus.plus(arvo)
    
class Erotus():
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self, arvo):
        self.sovellus.miinus(arvo)
    
class Nollaa():
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self, arvo):
        self.sovellus.nollaa()

class Kumoa():
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self, arvo):
        self.sovellus.kumoa()