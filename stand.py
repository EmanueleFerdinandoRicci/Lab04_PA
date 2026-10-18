class Stand:
    # Classe base per stand Standard

    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.codice = codice
        self.superficie = float(superficie)
        self.padiglione = int(padiglione)
        self.prezzo_base = float(prezzo_base)
        self.espositore = None

    @property
    def disponibile(self):
        # Visiono disponibilità con la non presenza dell'espositore
        return self.espositore is None

    def calcola_prezzo(self):
        # Lo metto per fare override nei casi più specifici
        return self.prezzo_base

    def __eq__(self, other):
        if isinstance(other, Stand):
            return self.codice == other.codice
        return False

    def __lt__(self, other):
        # Ordinamento basato sul metodo calcola_prezzo().
        if isinstance(other, Stand):
            return self.calcola_prezzo() < other.calcola_prezzo()
        return False

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = f"Occupato da {self.espositore.codice}"
        return f"{self.codice}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}"


class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        # Estensione del costruttore genitore.
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.numero_prese = int(numero_prese)

    def calcola_prezzo(self):
        # Overriding del calcolo prezzo (sovrapprezzo 7% per presa).
        return self.prezzo_base * (1 + 0.07 * self.numero_prese)

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = f"Occupato da {self.espositore.codice}"
        return f"{self.codice}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - Prese aggiuntive: {self.numero_prese} - {stato}"

class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.posizione = posizione

    def calcola_prezzo(self):
        # Overriding del calcolo prezzo (sovrapprezzo fisso 30%).
        return self.prezzo_base * 1.30

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = f"Occupato da {self.espositore.codice}"
        return f"{self.codice}: Premium ({self.posizione}) | {self.superficie:} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}"