from odoo import fields, models

class Professeur(models.Model):

    #Héritage
    _inherit = "res.partner"

    #"professeur"
    _name = "res.partner"

    #class_ids = fields.Integer(related="classe.teacher_ids")
