class Espositore:

    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome

    def __eq__(self, other):
        if isinstance(other, Espositore):
            return self.codice == other.codice
        return False

    def __str__(self):
        return f"{self.codice}: {self.nome} {self.cognome}"