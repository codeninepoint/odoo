from odoo import models, fields

class SocietyMember(models.Model):
    _name = 'esociety.member'
    _description = 'Society Member'

    partner_id = fields.Many2one('res.partner', string='Member Contact', required=True, help="Select the contact for this member.")
    # flat_id = fields.Many2one('esociety.flat', string='Flat', required=True)
    flat_id = fields.Many2one('stock.location', string='Flat', domain="[('is_flat','=',True)]", help="Select the flat assigned to this member.")
    # name = fields.Char(string='Name', required=True)
    # email = fields.Char(string='Email')
    # phone = fields.Char(string='Phone')
    # address = fields.Text(string='Address')
    # date_of_birth = fields.Date(string='Date of Birth')
    # flat_id = fields.Many2one('esociety.flat', string='Flat')
    join_date = fields.Date(string='Join Date')
    is_owner = fields.Boolean(string='Is Owner', default=True)
    # Add other relevant fields based on your ERD
    flat_number = fields.Char(related='flat_id.flat_number', string='Flat Number', store=True, readonly=True)

    def action_view_invoices(self):
        return {
            'name': 'Invoices',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'view_mode': 'list,form',
            'domain': [('partner_id', '=', self.partner_id.id)],
            'context': {'default_partner_id': self.partner_id.id},
        }
