from odoo import fields, models

class Cours(models.Model):

    _name = "cours"

    name = fields.Char(string="Matière")
    agenda_id = fields.One2many("agenda", "cours_id")