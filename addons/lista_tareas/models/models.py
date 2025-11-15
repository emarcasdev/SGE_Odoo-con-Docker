# -*- coding: utf-8 -*-
from odoo import models, fields, api
#Definimos el modelo de datos
class lista_tareas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'

    # Nombre de la tarea
    tarea = fields.Char(string="Título", required=True)
    # Descripción de la tarea
    descripcion = fields.Text(string="Descripción")
    # Fecha de la tarea
    fecha_limite = fields.Date(string="Fecha límite")
    # Prioridad numérica de la tarea
    prioridad = fields.Integer(string="Prioridad", default=1)

    # Nivel de prioridad de nuestra tarea en texto
    prioridad_nivel = fields.Selection(
        [
            ('baja', 'Baja'),
            ('media', 'Media'),
            ('urgente', 'Urgente')
        ],
        string="Prioridad",
        compute="_value_prioridad",
        store=True
    )

    # Estado de la tarea
    estado = fields.Selection(
        [
            ('pendiente', 'Pendiente'),
            ('en_progreso', 'En curso'),
            ('realizada', 'Realizada')
        ],
        string="Estado",
        default="pendiente"
    )
    
    @api.depends('prioridad')
    #Funcion para calcular el valor de urgente
    def _value_prioridad(self):
        #Para cada registro
        for record in self:
            #Si la prioridad es mayor que 10, se considera urgente
            if record.prioridad > 10:
                record.prioridad_nivel = 'urgente'
            #Si la prioridad es igual o mayor que 5, se considera media
            elif record.prioridad >= 5:
                record.prioridad_nivel = 'media'
            #Si la prioridad es menor que 5, se considera baja
            else:
                record.prioridad_nivel = 'baja'
