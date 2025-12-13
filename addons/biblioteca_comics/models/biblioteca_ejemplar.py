# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

# Definimos el modelo Biblioteca comic ejemplar
class BibliotecaComicEjemplar(models.Model):
    # Nombre del modelo
    _name = "biblioteca.comic.ejemplar"
    # Descripcion del modelo
    _description = "Ejemplar del cómic"
    # Usamos el id_ejemplar como nombre visible del registro
    _rec_name = "id_ejemplar"

    # Identificador único para el ejemplar
    id_ejemplar = fields.Char("ID ejemplar", required=True, index=True)

    # Referencia al comic del modelo biblioteca_comic
    # Utilizamos Many2one porque un ejemplar pertenece a un único cómic
    comic_name = fields.Many2one(
        "biblioteca.comic",
        "Cómic",
        required=True
    )

    # Identificador del socio que tiene el ejemplar
    # Utilizamos Many2one porque un ejemplar solo puede estar prestado a un único socio
    socio_id = fields.Many2one(
        'biblioteca.socio',
        "Prestado a"
    )

    # Estado del ejemplar físico
    estado = fields.Selection(
        [
            ("disponible", "Disponible"),
            ("prestado", "Prestado")
        ],
        "Estado",
        default="",
        required=True
    )

    # Fecha del comienzo del prestamo
    fecha_prestamo = fields.Date("Fecha de préstamo")

    # fecha de fin del prestamo
    fecha_devolucion = fields.Date("Fecha de devolución")

    #Constraints de SQL del modelo: el identificador deber ser único
    _sql_constraints = [
        ("codigo_uniq", "UNIQUE(id_ejemplar)", "El id del ejemplar debe ser único.")
    ]

    # Restricciones para las fechas
    @api.constrains('fecha_prestamo')
    def _valid_fecha_prestamo(self):
        for record in self:
            if record.fecha_prestamo > date.today():
                raise ValidationError("La fecha de préstamo no puede ser posterior al día actual.")
                

    @api.constrains('fecha_devolucion')
    def _valid_fecha_devolucion(self):
        for record in self:
            if record.fecha_devolucion < date.today():
                raise ValidationError("La fecha prevista de devolución no puede ser anterior al día actual.")
