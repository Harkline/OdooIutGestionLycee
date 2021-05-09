from odoo import fields, models, api

class Classe(models.Model):
    _name="classe"

    selection_list = [
        ("1", "Seconde"),
        ("2", "Première"),
        ("3", "Terminale")
    ]

    name = fields.Char(string="Classe", required="True")
    level = fields.Selection(selection_list, string="Niveau de classe", required="True") #champs selection
    student_nb = fields.Integer(compute="compute_counting_students", store=True, string="Nombre d'étudiants") #Champ calcule

    agenda_id=fields.One2many("agenda", "class_id")
    teacher_ids = fields.Many2many("res.partner")
    eleve_id=fields.One2many("eleve", "class_id")

    #Fonction a définir pour calculer le nombre d'étudiants
    @api.depends('eleve_id')
    def compute_counting_students(self):
        #Initialisation d'un compteur
        compteurEleve = 0
        for classe in self:
            #Si la classe à au moins un élève (à la création une classe peut avoir 0 élève), on compte le nombre d'élève
            if classe.eleve_id != 0:
                #Sans cette boucle, le compteur d'élève reste à 1 malgré que la classe contient plusieurs élèves
                for eleve in classe.eleve_id:
                    compteurEleve+=1
            classe.student_nb = compteurEleve
        
        #Note : On ne peut pas utiliser self, car sinon erreur suivante : "ValueError: Expected singleton: eleve(9, 10)"
        #self contient plusieurs recordset : https://www.odoo.com/fr_FR/forum/aide-1/valueerror-expected-singleton-odoo-14-180311
        

            
            