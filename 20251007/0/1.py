from decimal import Decimal
from fractions import Fraction

def multiplier(x, y, Type):       
    if Type == float:
        return float(x) * float(y)
    elif Type == Decimal:
        return Decimal(x) * Decimal(y)
    elif Type == Fraction:
        return Fraction(x) * Fraction                                                                                                                   raise ValueError(f"Неподдерживаемый тип: {Type}")
