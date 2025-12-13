# -*- coding: utf-8 -*-
from odoo import models, fields, api

# Definimos el modelo de consulta
class Consulta(models.Model):
    # Nombre del modelo
    _name = "consulta"
    # Descripcion del modelo
    _description = "Registro de las consultas"
    # Usamos el id_consulta como nombre visible del registro
    _rec_name = "id_consulta"

    # Atributos del modelo: identificador, medico, paciente, diagnostico y fecha de la cita.
    id_consulta = fields.Char("ID consulta", required=True, index=True)
    medico_id = fields.Many2one(
        "medico",
        "medico",
        required=True
    )
    paciente_id = fields.Many2one(
        "paciente",
        "paciente",
        required=True
    )
    diagnostico = fields.Text('Diagnóstico', required=True)
    fecha_cita = fields.Date("Fecha de la cita", required=True)


    #Constraints de SQL del modelo: el identificador deber ser único
    _sql_constraints = [
        ("identificador_uniq", "UNIQUE(id_consulta)", "El identificador de la consulta debe ser único.")
    ]
