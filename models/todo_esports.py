# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Persona(models.Model):
    _name = 'todo.esports.persona'
    dni = fields.Text('DNI',required = True)
    nom = fields.Char('Nom',40,required = True)
    cognom1 = fields.Char('1er Cognom',40,required = True)
    cognom2 = fields.Char('2on Cognom',40,required = True)
    tlf1 = fields.Integer('1er Teléfon',required = True)
    tlf2 = fields.Integer('2on Teléfon')
    email = fields.Text('Correu electrònic')
    adreca = fields.Text('Adreça',required = True)
    poblacio = fields.Text('Població',required = True)
    codiPostal = fields.Integer('Codi postal',required = True)

class Jugador(models.Model):
    _name = 'todo.esports.jugador'
    sexe = fields.Selection('Home','Dona',required = True)
    dataNaix = fields.Date('Data naixement',required = True)

class Posicio(models.Model):
    _name = 'todo.esports.posicio'
    posicio = fields.Selection('Porter','Extrem','Lateral','Central','Pivot')

class Categoria(models.Model):
    _name = 'todo.esports.categoria'
    descripcio = fields.Selection('Menor M/F','Cadet M','Cadet F','Juvenil M','Juvenil F','Junior M','Junior F',
                                  'Adult M','Adult F')