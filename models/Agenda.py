from odoo import fields, models

class Agenda(models.Model):

    _name = "agenda"

    date_start=fields.Datetime(string="Start time")
    date_stop = fields.Datetime(string="Finish time")
    room = fields.Char(string="Room")

    cours_id=fields.Many2one("cours")