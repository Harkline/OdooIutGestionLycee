from odoo import fields, models

class Eleve(models.Model):
    _name="eleve"

    firstname = fields.Char(string = "Firstname")
    lastname = fields.Char(string="Lastname")
    birthdate = fields.Datetime(string="Birthdate")
    age = fields.Integer(compute="compute_age_student", store=True)

    class_id = fields.Many2one("classe")

    #A définir, calcul de l'age à partir de sa date de naissance
    def compute_age_student(self):
        pass