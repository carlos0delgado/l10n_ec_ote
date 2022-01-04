# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Resinvcontac(models.Model):
    _inherit = 'res.partner'

    cedula = fields.Char('Cedula')
    f_nacimeinto = fields.Date('Fecha de Nacimeinto')
    genero = fields.Selection(selection=[('masculino', 'Masculino'), ('femenino', 'Femenino')], string="Genero")
    fcedula = fields.Binary('Foto de Cedula')
    fvacunacion = fields.Binary('Foto de Carnet de Vacunacion')
    usertalla = fields.Selection(selection=[('s', 'S'),('m', 'M'), ('l', 'L'), ('xl', 'XL')])
    nreferido = fields.Char('Nombre de quien lo refirio')
    siexp = fields.Char('Ha tenido Experiencia en Invetario?')
    detalle = fields.Char('Detalle de Experiencia')
    repersonal = fields.Char('Nombre de Referencia personal que viva con usted')
    rnpersonal = fields.Char('Numero de Referencia personal que viva con usted')
    hojacv = fields.Binary('Adjunte Hoja de Vida.')
