from odoo import models, fields

class SocietyFlat(models.Model):
    _name = 'esociety.flat'
    _description = 'Society Flat'

    name = fields.Char(string='Flat Number', required=True)
    floor = fields.Integer(string='Floor')
    # member_ids = fields.One2many('esociety.member', 'flat_id', string='Members')
    area_sqft = fields.Float(string='Area (sqft)')
    # Add other relevant fields
