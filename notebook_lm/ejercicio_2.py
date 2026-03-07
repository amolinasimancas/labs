es_estudiante = True
nota_final = 80
asistencia_minima = True

if not es_estudiante:
    print("No eres estudiante! Intento de acceso al sistema")

else:

    if nota_final >= 70 and asistencia_minima:
        print("Usted ha aprobado el exámen!")
    else:
        print("Usted ha reprobado el examen!")