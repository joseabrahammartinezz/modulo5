from django.core.exceptions import ValidationError

def validar_monto(value):
    if value >1000:
        raise ValidationError(
            '%(value)s es mayor al tope de monto a Cobrar (Bs. 1000)',
            params={'value': value}
        )

def validar_modalidad_ingreso(value):
    if not(value == 'LEVANTAMIENTO CATASTRAL'):
        raise ValidationError("MODALIDAD DE INGRESO NO PERMITIDA")


