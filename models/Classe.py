from odoo import fields, models

class Classe(models.Model):
    _name="classe"

    selection_list = [
        ("1", "Seconde"),
        ("2", "Première"),
        ("3", "Terminale")
    ]

    name = fields.Char(string="Class' name")
    level = fields.Selection(selection_list) #champs selection
    student_nb = fields.Integer(compute="compute_counting_students", store=True) #Champ calcule

    agenda_id=fields.One2many("agenda", "classe_id")
    #teacher_ids = fields.Integer(related="iut.professeur.class_ids")

    #Fonction a définir pour calculer le nombre d'étudiants
    def compute_counting_students(self):
        pass