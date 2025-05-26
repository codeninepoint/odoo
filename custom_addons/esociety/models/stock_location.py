from odoo import models, fields

class SocietyLocation(models.Model):
    _inherit = 'stock.location'

    is_society = fields.Boolean(string="Is Society")
    is_wing = fields.Boolean(string="Is Wing")
    is_flat = fields.Boolean(string="Is Flat")
    flat_number = fields.Char(string="Flat Number")
    wing_id = fields.Many2one('stock.location', string="Wing", domain="[('is_wing','=',True)]")
    society_id = fields.Many2one('stock.location', string="Society", domain="[('is_society','=',True)]")
    society_partner_id = fields.Many2one('res.partner', string="Society Contact", domain="[('is_company','=',True)]")
    # vendor_id = fields.Many2one('res.partner', string="Vendor", domain="[('supplier_rank','>',0)]")
    flat_partner_id = fields.Many2one('res.partner', string="Flat Contact")