
numero_acl = int(input("Ingrese el número de ACL: "))


if 1 <= numero_acl <= 99:
    tipo_acl = "ACL Estándar"
elif 100 <= numero_acl <= 199:
    tipo_acl = "ACL Extendida"
else:
    tipo_acl = "El número de ACL no corresponde a una ACL estándar ni extendida"


print("El número de ACL", numero_acl, "es: ", tipo_acl)
