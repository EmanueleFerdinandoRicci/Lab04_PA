import csv
from espositore import Espositore
from stand import Stand, StandPreseExtra, StandPremium


class LingottoFiere:
    def __init__(self, nome):
        self._nome = nome
        self.stand = []
        self.espositori = []

    @property
    def nome(self):
        # Getter nome
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        # Setter nome
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        # Riconosce la classe corretta in base alla lunghezza dei campi (4 o 5)
        # e al tipo di dato nel quinto campo (intero o stringa).
        try:
            with open(file_path, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for riga in reader:
                    if not riga:
                        continue

                    codice = riga[0].strip()

                    if codice.startswith("ST"):
                        superficie = riga[1].strip()
                        padiglione = riga[2].strip()
                        prezzo_base = riga[3].strip()

                        if len(riga) == 4:
                            s = Stand(codice, superficie, padiglione, prezzo_base)
                        elif len(riga) == 5:
                            valore_extra = riga[4].strip()
                            if valore_extra.isdigit():
                                s = StandPreseExtra(codice, superficie, padiglione, prezzo_base, int(valore_extra))
                            else:
                                s = StandPremium(codice, superficie, padiglione, prezzo_base, valore_extra)
                        else:
                            continue
                        self.stand.append(s)

                    elif codice.startswith("ES"):
                        if len(riga) >= 3:
                            nome = riga[1].strip()
                            cognome = riga[2].strip()
                            e = Espositore(codice, nome, cognome)
                            self.espositori.append(e)
        except FileNotFoundError:
            raise FileNotFoundError(f"Il file {file_path} non esiste.")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        # Implementazione tramite cicli for e flag booleani per verificare i vincoli
        stand_trovato = None
        for s in self.stand:
            if s.codice == codice_stand:
                stand_trovato = s
                break

        if stand_trovato is None:
            raise Exception(f"Lo stand con codice {codice_stand} non esiste.")
        if not stand_trovato.disponibile:
            raise Exception(f"Lo stand {codice_stand} è già occupato.")

        espositore_trovato = None
        for e in self.espositori:
            if e.codice == codice_espositore:
                espositore_trovato = e
                break

        if espositore_trovato is None:
            raise Exception(f"L'espositore con codice {codice_espositore} non esiste.")

        espositore_ha_gia_stand = False
        for s in self.stand:
            if s.espositore is not None and s.espositore == espositore_trovato:
                espositore_ha_gia_stand = True
                break

        if espositore_ha_gia_stand:
            raise Exception(f"L'espositore {codice_espositore} possiede già uno stand assegnato.")

        stand_trovato.espositore = espositore_trovato

    def elenca_espositori(self):
        if not self.espositori:
            print("Nessun espositore registrato.")
            return

        for e in self.espositori:
            stand_associato = None
            for s in self.stand:
                if s.espositore == e:
                    stand_associato = s
                    break

            if stand_associato is not None:
                print(f"{e} -> Stand assegnato: {stand_associato.codice} (Padiglione {stand_associato.padiglione})")
            else:
                print(f"{e} -> Nessuno stand assegnato")

    def stand_ordinati_per_prezzo(self):
        # Lista passata a sorted().
        return sorted(self.stand)