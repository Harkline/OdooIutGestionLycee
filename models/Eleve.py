from odoo import fields, models, api
from datetime import date

class Eleve(models.Model):
    _name="eleve"

    firstname = fields.Char(string = "Firstname")
    lastname = fields.Char(string="Lastname")
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(compute="compute_age_student", store=True) #readOnly

    class_id = fields.Many2one("classe")

    #A définir, calcul de l'age à partir de sa date de naissance
    @api.depends('birthdate')
    def compute_age_student(self):
        todayDate = date.today()
        self.age = todayDate.year - self.birthdate.year - ((todayDate.month, todayDate.day) < (self.birthdate.month, self.birthdate.day))