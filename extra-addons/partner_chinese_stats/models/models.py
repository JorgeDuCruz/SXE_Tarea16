import datetime  #-*- coding: utf-8 -*-

from odoo import models, fields, api


class partner_chinese_stats(models.Model):
     _inherit = 'res.partner'


     f_nac = fields.Date("Fecha de nacimiento")
     edad = fields.Integer(string = "Edad", readonly = True, compute = "_calcular_edad", store = True)
     signo_chino = fields.Char(string = "Signo Chino",readonly = True, compute="_calcular_chinada", store=True)

     @api.depends('f_nac')
     def _calcular_edad(self):
         for record in self:
             if record.f_nac:
                 fecha_actual = datetime.datetime.now().year
                 tiempo_vivido = fecha_actual - record.f_nac.year
                 record.edad = tiempo_vivido
                 
     @api.depends('f_nac')
     def _calcular_chinada(self):
         for record in self:
             if record.f_nac:
                 ano = record.f_nac.year
                 signoNum = ano%12
                 signo = "Sin signo"

                 match(signoNum):
                     case 0:
                         signo = "Mono"
                     case 1:
                         signo = "Gallo"
                     case 2:
                         signo = "Perro"
                     case 3:
                         signo = "Cerdo"
                     case 4:
                         signo = "Rata"
                     case 5:
                         signo = "Buey"
                     case 6:
                         signo = "Tigre"
                     case 7:
                         signo = "Conejo"
                     case 8:
                         signo = "Dragón"
                     case 9:
                         signo = "Serpiente"
                     case 10:
                         signo = "Caballo"
                     case 11:
                         signo = "Cabra"

                 record.signo_chino = signo
