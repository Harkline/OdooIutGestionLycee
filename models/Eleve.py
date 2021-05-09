from odoo import fields, models, api
from datetime import date

class Eleve(models.Model):
    _name="eleve"

    firstname = fields.Char(string = "Prénom", required="True")
    lastname = fields.Char(string="Nom de famille", required="True")
    birthdate = fields.Date(string="Date de naissance", required="True")
    age = fields.Integer(compute="compute_age_student", store=True, string="Age") #readOnly

    class_id = fields.Many2one("classe")

    #Calcul de l'age à partir de sa date de naissance
    @api.depends('birthdate')
    def compute_age_student(self):
        #On récupère la date d'aujourd'hui
        todayDate = date.today()
        #Obligé de boucler dans self car sinon erreur "ValueError: Expected singleton" lors de la création d'une classe avec plusieurs élèves 
        #Sinon, possible de juste utiliser self.age et self.birthdate
        for element in self:
            #On vérifie que la date de naissance n'est pas vide
            if (element.birthdate != 0):
                #On calcule la différence en année
                #La différence des deux dates est un "timedelta" : https://docs.python.org/3/library/datetime.html
                #On utilise l'un des champs possibles de timedelta (Les jours) pour retrouver le nombre d'années de différence (donc l'age)
                element.age = (todayDate - element.birthdate).days/365 