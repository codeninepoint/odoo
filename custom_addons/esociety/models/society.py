
from odoo import api, fields, models

class EsocietySociety(models.Model):
    _name = 'esociety.society'
    _description = 'Society Master'

    name = fields.Char(string = "Name",required = True)
    date_of_formation = fields.Date(string = "DOB")
    registration_number = fields.Char(string="Registration Number")
    address = fields.Text(string="Address")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    zip_code = fields.Char(string="ZIP/Postal Code")
    country_id = fields.Many2one('res.country', string="Country")
    president_id = fields.Many2one('res.partner', string="President")
    secretary_id = fields.Many2one('res.partner', string="Secretary")
    total_flats = fields.Integer(string="Total Flats")
    amenities = fields.Text(string="Amenities")
    logo = fields.Binary(string="Society Logo")
    active = fields.Boolean(string="Active", default=True)