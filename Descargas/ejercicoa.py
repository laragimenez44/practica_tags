def crear_pacientes(agenda_de_paciente:dict, dni: int, nombre:str, apellido: str, domicilio: str, telefono: int, mutual: str) -> None:
    agenda_de_paciente[dni]= {"nombre": nombre ,"apellido": apellido, "domicilio": domicilio, "teléfono": telefono, "mutual": mutual }

agenda_de_pacientes= {}