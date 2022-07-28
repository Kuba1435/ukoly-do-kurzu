# Zadaná proměnná
sentence = 'A speech sound that is produced by comparatively open configuration\
of the vocal tract.'

# Samohlásky
vowels = "aeiouy"

# Slovník s evidencí výskytu jednotlivých typů písmen
counts = {
    "cons": 0,
    "vows": 0
}

# Iterace přes zadanou proměnnou 'sentece'
for letter in sentence:

    # .. pokud znak není písmeno
    if not letter.isalpha():
        continue
    # .. pokud je převedený znak mezi hodnotami samohlásek
    elif letter.lower() in vowels:
        counts["vows"] += 1
    # .. pokud není převedený znak mezi hodnotami samohlásek
    else:
        counts['cons'] += 1

# Vypiš závěrečný výstup v podobě celkového počtu samohlásek a souhlásek
print( 'No. consonants: ', counts['cons'], ' | No. vowels: ', counts['vows'] )
