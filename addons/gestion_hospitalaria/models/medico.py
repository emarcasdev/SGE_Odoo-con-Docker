# -*- coding: utf-8 -*-
from odoo import models, fields, api

# Definimos el modelo del medico
class Medico(models.Model):
    # Nombre del modelo
    _name = "medico"
    # Descripcion del modelo
    _description = "Médico de un hospital"
    # Usamos el nombte completo como nombre visible del registro
    _rec_name = "nombre_completo"

    # Atributos del modelo: número colegiado, nombre, apellido, sintomas y obtenemos el nombre completo
    num_colegiado = fields.Char("Número de colegiado", required=True, index=True)
    nombre = fields.Char("Nombre", required=True)
    apellidos = fields.Char("Apellidos", required=True)
    nombre_completo = fields.Char("Médico", compute="_compute_nombre_completo", store=True)

    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"

    #Constraints de SQL del modelo: el identificador deber ser único
    _sql_constraints = [
        ("identificador_uniq", "UNIQUE(num_colegiado)", "El número de colegiado debe ser único.")
    ]
