
#validación del numero de criaturas hostiles y pasivas
def validar_c(n_activas,n_pastivas):
    if (n_activas+n_pastivas <= 50) and (n_activas != 0) and (n_pastivas != 0):
      return True
      
    else:
      return False