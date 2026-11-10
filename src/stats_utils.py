import statistics

montant_ventes = [150, 200, 300, -50, 0, 100, 1200, 250]

def analyser_ventes(montant_ventes) :
    ventes_valides = []
    for mv in montant_ventes :
        if mv > 0 :
            ventes_valides.append(mv)
            
    nb_ventes = len(ventes_valides)
    total_ventes = sum(ventes_valides)
    if nb_ventes > 0 :
        moyenne_ventes = total_ventes / nb_ventes
        mediane_ventes = statistics.median(ventes_valides)
        ecart_type_ventes = statistics.pstdev(ventes_valides)
        min_ventes = min(ventes_valides)
        max_ventes = max(ventes_valides)
        
        ventes_extremes = []
        for mv in ventes_valides :
            if mv > moyenne_ventes * 2 :
                ventes_extremes.append(mv)            
        
    else :
        moyenne_ventes = 0
        mediane_ventes = None
        ecart_type_ventes = None
        min_ventes = None
        max_ventes = None
        ventes_extremes = []
    
    resultats = {
        "nombre_ventes": nb_ventes,
        "total_ventes": total_ventes,
        "moyenne_ventes": round(moyenne_ventes, 2),
        "mediane_ventes": mediane_ventes,
        "ecart_type_ventes": round(ecart_type_ventes, 2) if ecart_type_ventes is not None else None,
        "min_ventes": min_ventes,
        "max_ventes": max_ventes,
        "ventes_extremes": ventes_extremes
    }         
    
    return resultats
    
resultat = analyser_ventes(montant_ventes)
print(resultat)


# Ajout de Zoubert
def calcul_etendue(lst_nombre):
    etendue = max(lst_nombre) - min(lst_nombre)
    return etendue