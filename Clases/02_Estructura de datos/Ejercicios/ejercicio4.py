#Escribe un programa en Python que muestre la hora actual con una suma de dos horas adicionales

from datetime import datetime

localTime = datetime.now()

hour = localTime.hour
minute = localTime.minute

hour += 2

print ("La hora actual es: ", localTime, " , y dentro de dos horas serán: ",hour,":",minute)