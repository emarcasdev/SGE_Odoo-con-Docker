# -*- coding: utf-8 -*-
from odoo import models, fields

# Definimos el modelo Biblioteca socio
class BibliotecaSocio(models.Model):
    # Nombre del modelo
    _name = "biblioteca.socio"
    # Descripcion del modelo
    _description = "Socio de la bilioteca"
    # Usamos el id_socio como nombre visible del registro
    _rec_name = "id_socio"

    # Atributos del modelo: identificador, nombre y apellido
    id_socio = fields.Char("ID socio", required=True, index=True)
    nombre = fields.Char("Nombre", required=True)
    apellido = fields.Char("Apellido", required=True)

    #Constraints de SQL del modelo: el identificador deber ser único
    _sql_constraints = [
        ("identificador_uniq", "UNIQUE(id_socio)", "El identificador del socio debe ser único.")
    ]
