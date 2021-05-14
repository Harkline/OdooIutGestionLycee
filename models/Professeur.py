from odoo import fields, models

class Professeur(models.Model):

    #Héritage
    _inherit = "res.partner"

    #"professeur"
    _name = "res.partner"

    name = fields.Char(string="Prénom")
    class_ids = fields.Many2many("classe", string="Classe")
