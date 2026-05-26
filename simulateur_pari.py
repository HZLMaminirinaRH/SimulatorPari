import sys

solde_virtuel = 101100.0  # On reprend ton solde actuel après ta victoire

def simuler_pari_dynamique():
    global solde_virtuel
    print(f"\n--- CONFIGURATION DU MATCH (Solde : {solde_virtuel:.2f}) ---")
    
    # Saisie des informations du match réel
    equipe1 = input("Nom de l'équipe à domicile : ")
    equipe2 = input("Nom de l'équipe à l'extérieur : ")
    
    c1 = float(input(f"Cote pour {equipe1} (1) : "))
    cx = float(input(f"Cote pour le Nul (X) : "))
    c2 = float(input(f"Cote pour {equipe2} (2) : "))
    
    print(f"\nMatch : {equipe1} vs {equipe2}")
    print(f"Cotes : [1] {c1} | [X] {cx} | [2] {c2}")
    
    choix = input("Ton pronostic (1, X, ou 2) : ")
    mise = float(input(f"Mise (max {solde_virtuel}) : "))
    
    if mise > solde_virtuel:
        print("Erreur : Fonds insuffisants !")
        return

    # Calcul de la probabilité pour t'aider à décider
    cote_choisie = c1 if choix == "1" else (c2 if choix == "2" else cx)
    prob = (1 / cote_choisie) * 100
    print(f"Probabilité estimée par le site : {prob:.2f}%")

    # Simulation du résultat final
    resultat_reel = input(f"Quel a été le résultat final de {equipe1}-{equipe2} ? (1, X, 2) : ")

    if choix == resultat_reel:
        gain = mise * cote_choisie
        solde_virtuel += (gain - mise)
        print(f"VICTOIRE ! Gain : {gain:.2f}. Nouveau solde : {solde_virtuel:.2f}")
    else:
        solde_virtuel -= mise
        print(f"ÉCHEC. Nouveau solde : {solde_virtuel:.2f}")

while True:
    simuler_pari_dynamique()
    if input("\nContinuer ? (o/n) : ").lower() == 'n':
        break

