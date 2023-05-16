def calcola_punteggio(titoli_selezionati, punteggi):
    punteggio_totale = 0
    for titolo in titoli_selezionati:
        if titolo in punteggi:
            punteggio_totale += punteggi[titolo]
        else:
            print(f"Il titolo '{titolo}' non ha un punteggio assegnato.")
    return punteggio_totale

def main():
    punteggi = {
        #Valutazione periodo VFI/VFT (ex VFP)
        "Periodo di Servizio da 12 mesi e 1 giorno fino a 18 mesi (VFP)": 1,
        "Periodo di Servizio da 18 mesi e 1 giorno di servizio fino a 24 mesi e 15 giorni (VFP)": 1.5,
        "Periodo di Servizio da 24 mesi e 16 giorni di servizio fino a 36 mesi e 15 giorni (VFP)": 2,
        "Periodo di Servizio da 36 mesi e 16 giorni di servizio a 48 mesi e 15 giorni (VFP)": 3,
        "Periodo di Servizio oltre 48 mesi e 16 giorni di servizio (VFP)": 4,
        #Valutazione ferma biennale (VFP)
        "Periodo di rafferma biennale da 48 a 54 mesi (VFP)": 0.1,
        "Periodo di rafferma biennale da 55 a 60 mesi (VFP)": 0.2,
        "Periodo di rafferma biennale da 61 a 66 mesi (VFP)": 0.3,
        "Periodo di rafferma biennale da 67 a 72 mesi  (VFP)": 0.4,
        "Periodo di rafferma biennale oltre 72 mesi (VFP)": 0.5,
        #Valutazione missioni estere VFI/VFT (ex VFP)
        "Fino a sei mesi anche non continuativi di permanenza in teatro operativo estero (VFP)": 1,
        "Oltre sei mesi anche non continuativi di permanenza (VFP)": 2,
        #Valutazione qualità servizio VFI/VFT (ex VFP)
        "Valutazione superiore alla media o giudizio equivalente (VFP)": 1.5,
        "Valutazione eccellente o giudizio equivalente (VFP)": 3,
        #Valutazione decorazioni e benemerenze
        "Encomio o elogio (VFP)": 0.5,
        "Encomio solenne (VFP)": 1,
        "Promozione straordinaria per benemerenze d’istituto (VFP)": 6.5,
        "Croce di guerra al valor militare (VFP)": 7,
        "Medaglia di bronzo al valor militare o al valor civile (VFP)": 7.5,
        "Promozione straordinaria per merito di guerra (VFP)": 8,
        "Medaglia d’argento al valor militare o al valor civile (VFP)": 9,
        "Medaglia d’oro al valor militare o al valor civile (VFP)": 10,
        #Valutazione brevetti e qualifiche
        "Qualifica di sciatore militare o di cavaliere militare (VFP)": 1.5,
        "Brevetto di paracadutista militare (VFP)": 1.5,
        "Qualifica di sciatore militare scelto o di cavaliere militare scelto (VFP)": 2.5,
        "Brevetto di istruttore militare di sci o di istruttore militare di equitazione (VFP)": 3.5,
        #Patente
        "Patente di guida C e D ed equivalenti abilitazioni alla guida di veicoli militari (VFP)": 1.5,
        #Certificazioni Informatiche (VFP)
        "Altre certificazioni informatiche riconosciute a livello europeo ed internazionale, rilasciate negli ultimi tre anni alla data di scadenza di presentazione della domanda di partecipazione al concorso (VFP)": 1,
        "EUCIP (European Certification of Informatics Professionals) (VFP)": 2,
        "CIFI (Certified Information Forensics Investigator) o OPST (OSSTMM Professional Security Tester) o SSCP (Systems Security Certified Practitioner) (VFP)": 4,
        #Titoli di studio
        "Laurea magistrale in ARCHITETTURA DEL PAESAGGIO; BIOLOGIA; BIOTECNOLOGIE AGRARIE; BIOTECNOLOGIE INDUSTRIALI; BIOTECNOLOGIE MEDICHE; VETERINARIE E FARMACEUTICHE; CONSERVAZIONE DEI BENI ARCHITETTONICI E AMBIENTALI; CONSERVAZIONE E RESTAURO DEI BENI CULTURALI; INFORMATICA; INGEGNERIA DELLE TELECOMUNICAZIONI; INGEGNERIA PER L’AMBIENTE E IL TERRITORIO; PIANIFICAZIONE TERRITORIALE URBANISTICA E AMBIENTALE; SCIENZE DELLA NATURA; SICUREZZA INFORMATICA; SCIENZE E TECNOLOGIE AGRARIE; SCIENZE E TECNOLOGIE ALIMENTARI; SCIENZE E TECNOLOGIE FORESTALI ED AMBIENTALI; SCIENZE E TECNOLOGIE GEOLOGICHE; SCIENZE E TECNOLOGIE PER L’AMBIENTE E IL TERRITORIO; SCIENZE ZOOTECNICHE E TECNOLOGIE ANIMALI": 6,
        "Laurea magistrale o triennale in SCIENZE INFERMIERISTICHE; SCIENZE DELLE PROFESSIONI SANITARIE DELLA PREVENZIONE; PROFESSIONI SANITARIE, INFERMIERISTICHE; TECNICHE DELLA PREVENZIONE NELL’AMBIENTE E DEI LUOGHI": 6,
        "Laurea triennale di o di primo livello in BENI CULTURALI; BIOTECNOLOGIE; INGEGNERIA CIVILE E AMBIENTALE; SCIENZE BIOLOGICHE; SCIENZE DELLA PIANIFICAZIONE TERRITORIALE, URBANISTICA, PAESAGGISTICA E AMBIENTALE; SCIENZE E TECNOLOGIE AGRARIE E FORESTALI; SCIENZE E TECNOLOGIE AGRO-ALIMENTARI; SCIENZE E TECNOLOGIE FARMACEUTICHE; SCIENZE E TECNOLOGIE INFORMATICHE; SCIENZE E TECNOLOGIE PER L’AMBIENTE E LA NATURA; SCIENZE GEOLOGICHE; SCIENZE ZOOTECNICHE E TECNOLOGIE DELLE PRODUZIONI ANIMALI": 4,
        "Altre lauree magistrali": 3,
        "Altre lauree triennali ed attestati di frequenza di Corsi di Istruzione e Formazione tecnica superiore nei settori forense edella grafica ": 2,
        "Diplomi in MECCANICA, MECCATRONICA ED ENERGIA; ELETTRONICA ED ELETTROTECNICA; INFORMATICA E TELECOMUNICAZIONI; CHIMICA, MATERIALI E BIOTECNOLOGIE; AGRARIA, AGROALIMENTARE E AGROINDUSTRIA; COSTRUZIONI, AMBIENTE E TERRITORIO; SERVIZI PER L’AGRICOLTURA E LO SVILUPPO RURALE": 1.5,
        #Certificazioni Informatiche
        "Altre certificazioni informatiche riconosciute a livello europeo ed internazionale, rilasciate negli ultimi tre anni alla data di scadenza di presentazione della domanda di partecipazione al concorso": 1,
        "EUCIP (European Certification of Informatics Professionals)": 2,
        "CIFI (Certified Information Forensics Investigator) o OPST (OSSTMM Professional Security Tester) o SSCP (Systems Security Certified Practitioner)": 4,
        #Brevetto
        "Brevetto di guida alpina, osservatore meteonivometrico": 2,
        "Abilitazione all’esercizio della professione di maestro di sci alpino, in corso di validità": 5,
        "Autorizzazioni a montare di 2° grado, rilasciata dalla Federazione Italiana Sport Equestri": 5,
        "Autorizzazioni a montare di 1° grado, rilasciata dalla Federazione Italiana Sport Equestri": 3,
        "Brevetto rilasciato dalla Federazione Italiana Sport Equestri": 1,
        "Brevetto di cavaliere specialista e patente A3 rilasciato dalla Federazione Italiana Turismo Equestre (FITE) – Tecniche diRicognizione Equestre Competitive (TREC – ANTE)": 3,
        "Brevetto di cavaliere e patente A2 Junior/Senior rilasciato dalla Federazione Italiana Turismo Equestre (FITE) – Tecniche diRicognizione Equestre Competitive (TREC – ANTE)": 1,
        #Titoli Linguistici
        "Lingua inglese, araba, francese e cinese certificate con sistema STANAG/NATO con un livello di conoscenza pari a 16": 2,
        "Lingua inglese, araba, francese e cinese certificate con sistema STANAG/NATO con un livello di conoscenza da 14 a 15": 1.5,
        "Lingua inglese, araba, francese e cinese certificate con sistema STANAG/NATO con un livello di conoscenza da 12 a 13": 1,
        "Lingua inglese, araba, francese e cinese certificate con sistema STANAG/NATO con un livello di conoscenza da 8 a 11": 0.5,
        "Lingua albanese, portoghese, rumena, russa, spagnola e tedesca certificate con sistema STANAG/NATO con un livello di conoscenza pari a 16": 1,
        "Lingua albanese, portoghese, rumena, russa, spagnola e tedesca certificate con sistema STANAG/NATO con un livello di conoscenza da 14 a 15": 0.75,
        "Lingua albanese, portoghese, rumena, russa, spagnola e tedesca certificate con sistema STANAG/NATO con un livello di conoscenza da 12 a 13": 0.5,
        "Lingua inglese, araba, francese e cinese certificate con sistema CEFR con un livello di conoscenza C2": 2,
        "Lingua inglese, araba, francese e cinese certificate con sistema CEFR con un livello di conoscenza C1": 1.5,
        "Lingua inglese, araba, francese e cinese certificate con sistema CEFR con un livello di conoscenza B2": 1,
        "Lingua inglese, araba, francese e cinese certificate con sistema CEFR con un livello di conoscenza B1": 0.5,
        "Lingua albanese, portoghese, rumena, russa, spagnola e tedesca certificate con sistema CEFR con un livello di conoscenza C2": 1,
        "Lingua albanese, portoghese, rumena, russa, spagnola e tedesca certificate con sistema CEFR con un livello di conoscenza C1": 0.75,
        "Lingua albanese, portoghese, rumena, russa, spagnola e tedesca certificate con sistema CEFR con un livello di conoscenza B2": 0.5,
        #Altri titoli
        "Brevetti Subacquei": 0,
        "Brevetti APR": 0,
        "Brevetto Paracadutista Civile": 0,
        "Bagnino di Salvataggio o Assistente Bagnanti": 0,
    }

    titoli_posseduti = list(punteggi.keys())
    print("©2023 Marco Lo Giudice - All Rights Reserved")
    print("Calcolo punteggio dei titoli posseduti nei concorsi")
    print("Seleziona i titoli che possiedi:")

    selezioni = []

    for i, titolo in enumerate(titoli_posseduti, 1):
        selezione = input(f"Possiedi il titolo '{titolo}'? (S/N): ")
        if selezione.upper() == "S":
            selezioni.append(titolo)

    punteggio_totale = calcola_punteggio(selezioni, punteggi)

    print(f"Il tuo punteggio totale è {punteggio_totale}.")

if __name__ == "__main__":
    main()
