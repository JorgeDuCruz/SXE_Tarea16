#-*- coding: utf-8 -*-

from odoo import models, fields, api


class fidelizacion__clientes(models.Model):
    _inherit = 'res.partner'

    cod_s = fields.Char("Código de Socio")
    nvl_fid = fields.Char(string="Nivel de Fidelidad",readonly=True,compute="_calcular_fidelidad")


    @api.depends('cod_s')
    def _calcular_fidelidad(self):
        for record in self:
            cos = record.cod_s

            if cos:
                if cos[0] == 'G':
                    record.nvl_fid = "Gold"
                else:
                    record.nvl_fid = "Premium"
            else:
                record.nvl_fid = "Estándar"

