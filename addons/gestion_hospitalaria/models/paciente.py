# -*- coding: utf-8 -*-
from odoo import models, fields, api

# Definimos el modelo del paciente
class Paciente(models.Model):
    # Nombre del modelo
    _name = "paciente"
    # Descripcion del modelo
    _description = "Paciente de un hospital"
    # Usamos el nombre completo como nombre visible del registro
    _rec_name = "nombre_completo"

    # Atributos del modelo: identificador, nombre, apellido, sintomas y y obtenemos el nombre completo
    id_paciente = fields.Char("ID paciente", required=True, index=True)
    nombre = fields.Char("Nombre", required=True)
    apellidos = fields.Char("Apellidos", required=True)
    sintomas = fields.Text('Síntomas', required=True)
    nombre_completo = fields.Char("Paciente", compute="_compute_nombre_completo", store=True)

    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"

    #Constraints de SQL del modelo: el identificador deber ser único
    _sql_constraints = [
        ("identificador_uniq", "UNIQUE(id_paciente)", "El identificador del paciente debe ser único.")
    ]
