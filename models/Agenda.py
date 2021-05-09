from odoo import fields, models

class Agenda(models.Model):

    _name = "agenda"

    date_start=fields.Datetime(string="Heure de fin")
    date_stop = fields.Datetime(string="Heure de début")
    room = fields.Char(string="Salle")

    cours_id=fields.Many2one("cours")
    class_id=fields.Many2one("classe")