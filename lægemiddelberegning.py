"""
***VIGTIGT***: Denne fil er kun til læring. Må ikke bruges til kliniske beslutninger.

OPGAVE: Implementér funktionerne nedenfor, så alle tests i "lægemiddelberegning_test.py" består.
KRAV (generelt):
- Brug de angivne formler i kommentarerne.
- Returnér et tal (float eller int, alt efter hvad der giver mening).
- Rejs ValueError ved ugyldige input (fx hvis en værdi er <= 0, eller hvis fortynding er umulig).
- Ændr ikke funktionsnavne eller parametre.
"""

def volume_for_dose(dose_mg: float, stock_mg: float, stock_ml: float) -> float:
    """
    Beregn volumen (mL) der skal gives.
    Formel: S = stock_mg / stock_ml  (styrke i mg/mL)
            V = dose_mg / S          (volumen i mL)
    Eksempel: dose=250 mg, stock=500 mg i 10 mL → S=50 mg/mL → V=250/50=5.0 mL

    KRAV:
    - Alle input skal være > 0 ellers ValueError.
    - Returnér volumen som float.
    """
    # TODO: Implementér beregningen jævnfør formlen ovenfor.
    # 1) Tjek at dose_mg, stock_mg, stock_ml er > 0, ellers: raise ValueError
    # 2) strength = stock_mg / stock_ml
    # 3) volume = dose_mg / strength
    # 4) return volume
    pass

def convert_mg_to_g(value_mg: float) -> float:
    """
    Konverter milligram (mg) til gram (g).
    Formel: g = mg / 1000
    Eksempel: 1000 mg → 1.0 g, 500 mg → 0.5 g

    KRAV:
    - value_mg skal være > 0 ellers ValueError.
    - Returnér resultatet som float.
    """
    # TODO: Implementér beregningen.
    # 1) Tjek at value_mg > 0, ellers: raise ValueError
    # 2) return value_mg / 1000.0
    pass


def infusion_rate_mL_per_h(dose_mg_per_h: float, concentration_mg_per_mL: float) -> float:
    """
    Beregn infusionshastighed i mL/h fra mg/h og mg/mL.
    Formel: mL/h = dose_mg_per_h / concentration_mg_per_mL
    Eksempler: 20 mg/h ved 1 mg/mL → 20.0 mL/h
               50 mg/h ved 2 mg/mL → 25.0 mL/h

    KRAV:
    - Begge input skal være > 0 ellers ValueError.
    - Returnér resultatet som float.
    """
    # TODO: Implementér beregningen.
    # 1) Tjek at dose_mg_per_h > 0 og concentration_mg_per_mL > 0, ellers: raise ValueError
    # 2) return dose_mg_per_h / concentration_mg_per_mL
    pass
    try:
        assert dose_mg_per_h > 0, "input skal være større end 0"
        assert concentration_mg_per_mL > 0, "input skal være større end 0"
        return dose_mg_per_h / concentration_mg_per_mL
    except AssertionError as e:
        raise ValueError(e)


def dilution_stock_volume(C1: float, C2: float, V2: float) -> float:
    """
    Beregn V1 (mL) til fortynding, når C1 (stock-koncentration), C2 (slut-koncentration) og V2 (slutvolumen) er givet.
    Formel: C1 * V1 = C2 * V2  →  V1 = (C2 * V2) / C1
    Eksempel: C1=10 mg/mL, C2=2 mg/mL, V2=50 mL → V1=10.0 mL

    KRAV:
    - C1, C2 og V2 skal være > 0, ellers ValueError.
    - Det skal være en fortynding (C2 < C1), ellers ValueError.
    - Returnér V1 som float.
    """
    # TODO: Implementér beregningen.
    # 1) Tjek at C1 > 0, C2 > 0, V2 > 0, ellers: raise ValueError
    # 2) Tjek at C2 < C1, ellers: raise ValueError
    # 3) V1 = (C2 * V2) / C1
    # 4) return V1
    if C1 < 0 or C2 < 0 or V2 < 0:
        raise ValueError("Værdier skal være positive")
    if C2 > C1:
        raise ValueError("C2 skal være mindre end C1")
    V1 = (C2 * V2) / C1
    return float(V1)
    
