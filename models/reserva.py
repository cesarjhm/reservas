from odoo import models, fields, api

class Habitaciones(models.Model):
     _name = 'reserva.habitaciones'

     tipo = fields.Char(string="Tipo Habitacion", required=True)
     numero = fields.Integer(string="Numero Habitacion", required=True)
     cantidad_camas = fields.Integer(string="Cantidad Camas", required=True)
     precio = fields.Float(string="Precio", required=True)

