# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, timedelta

class auditorialopd(models.Model):
     _name = 'auditorialopd.auditoria'
     _description = 'datos generales de la Auditoria'

     codigo = fields.Char(string="Codigo", required=True)
     fecha_inicio = fields.Datetime('Datetime', default=fields.datetime.now())
     fecha_final = fields.Datetime('Datetime', default=fields.datetime.now() + timedelta(hours=4))
     resumen_informe = fields.Text(string="Resumen del Informe")
     cliente = fields.Many2one('auditorialopd.cliente', string="Cliente", required=True)
     empleado = fields.Many2one('hr.employee', string="Empleado", required=True)
     cliente_names = fields.Char(string="Clientes", compute="_compute_cliente_names")
     _rec_name = 'codigo'


class cliente(models.Model):
     _name = 'auditorialopd.cliente'
     _description = 'Datos generales de la empresa cliente'
     _rec_name = 'nombre'

     nombre = fields.Char(string="Nombre", required=True)
     cif = fields.Char(string="CIF/NIE", required=True)
     direccion_fiscal = fields.Char(string="Direccion fiscal", required=True)
     direccion_social = fields.Char(string="Direccion social")
     iban = fields.Char(string="IBAN", required=True)
     tratamiento_gestoria = fields.Many2many('auditorialopd.tratamiento_gestoria', string="Tratamiento Gestoria")
     tratamiento_equipos = fields.Many2many('auditorialopd.tratamiento_equipos_informaticos', string="Tratamiento Equipos")
     tratamiento_seguridad = fields.Many2many('auditorialopd.tratamiento_seguridad', string="Tratamiento Seguridad")
     representante_id = fields.Many2one('auditorialopd.representante', string="Representante", required=True)

     #de este modo asignamos por defecto a direccion social el valor de direccion fiscal
     @api.model
     def create(self, vals):
          # Si 'direccion_social' no se ha proporcionado, copia el valor de 'direccion_fiscal'
          if 'direccion_social' not in vals and 'direccion_fiscal' in vals:
               vals['direccion_social'] = vals['direccion_fiscal']
          return super(cliente, self).create(vals)

     def write(self, vals):
          if 'direccion_social' not in vals and 'direccion_fiscal' in vals:
               vals['direccion_social'] = vals['direccion_fiscal']
          return super(cliente, self).write(vals)

     @api.onchange('direccion_fiscal')
     def _onchange_direccion_fiscal(self):
          if not self.direccion_social:
               self.direccion_social = self.direccion_fiscal

class representante(models.Model):
     _name = 'auditorialopd.representante'
     _description = 'Datos generales del representante de la empresa cliente'
     _rec_name = 'dni'

     dni = fields.Char(string="DNI", required=True)
     nombre = fields.Char(string="Nombre", required=True)
     apellidos = fields.Char(string="Apellidos", required=True)
     tlf = fields.Char(string="Telefono", required=True)
     email = fields.Char(string="Email")
     funcion = fields.Selection([('gestor', 'Gestor'), ('seguridad', 'Seguridad'), ('equipos', 'Equipos')], string="Funcion", required=True)
     cliente_id = fields.Many2one('auditorialopd.cliente', string="Cliente")
     # This inverse field should not be required and should reference the Many2one field from the Cliente model
     cliente_ids = fields.One2many('auditorialopd.cliente', 'representante_id')


class tratamiento_gestoria(models.Model):
     _name = 'auditorialopd.tratamiento_gestoria'
     _description = 'Datos generales del tratamiento de la gestoria'

     cif = fields.Char(string="CIF/NIE")
     nombre = fields.Char(string="Nombre")
     tipo = fields.Selection([('interno', 'Interno'), ('externo', 'Externo')], string="Tipo")
     cliente = fields.Many2many('auditorialopd.cliente', string="Cliente")


class tratamiento_equipos_informaticos(models.Model):
     _name = 'auditorialopd.trat_eq_inform'
     _description = 'Datos generales de la empresa de tratamientos de equipos informaticos'

     cif = fields.Char(string="CIF/NIE")
     nombre = fields.Char(string="Nombre")
     tipo = fields.Selection([('interno', 'Interno'), ('externo', 'Externo')], string="Tipo")
     cliente = fields.Many2many('auditorialopd.cliente', string="Cliente")


class tratamiento_seguridad(models.Model):
     _name = 'auditorialopd.tratamiento_seguridad'
     _description = 'Datos generales de la empresa de tratamientos de seguridad'

     cif = fields.Char(string="CIF/NIE")
     nombre = fields.Char(string="Nombre")
     tipo = fields.Selection([('interno', 'Interno'), ('externo', 'Externo')], string="Tipo")
     cliente = fields.Many2many('auditorialopd.cliente', string="Cliente")