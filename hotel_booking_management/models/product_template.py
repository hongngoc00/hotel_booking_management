from datetime import date
from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = [
        "product.template",
        "website.seo.metadata",
        'website.published.multi.mixin',
        'website.searchable.mixin',
        'rating.mixin',
    ]
    _name = 'product.template'

    feature_facility_id = fields.Many2many('feature.facility.management')
    state = fields.Selection([('available', 'Available'), ('unavailable', 'Unavailable'), ('fixing', 'Fixing')],
                             string='Status', default='available', required=True)
    room_type = fields.Selection([('single', 'Single'), ('double', 'Double')],
                                 string='Room Type', default='single', required=True)
    room_description = fields.Html(string='Description')

    @api.constrains('state')
    def compute_ribbon(self):
        dict_val = {'available': 'Available',
                    'unavailable': 'Unavailable',
                    'fixing': 'Fixing'}
        dict_color = {'available': 'bg-success o_ribbon_left',
                      'unavailable': 'bg-danger o_ribbon_left',
                      'fixing': 'bg-warning o_ribbon_left'}
        for rec in self:
            rec.website_ribbon_id.html = dict_val[rec.state]
            rec.website_ribbon_id.html_class = dict_color[rec.state]

    def booking_room(self, name, phone, address, check_in, check_out):
        if self.state == 'available':
            if check_in and check_out:
                list_check_in = check_in.split('-')
                date_check_in = date(int(list_check_in[0]), int(list_check_in[1]), int(list_check_in[2]))
                list_check_out = check_out.split('-')
                date_check_out = date(int(list_check_out[0]), int(list_check_out[1]), int(list_check_out[2]))
            check_room = self.env['hotel.booking.management'].sudo().search([('room_id', '=', self.id), ('status', '!=', 'canceled')])
            if not check_room:
                self.env['hotel.booking.management'].sudo().create({
                    'room_id': self.id,
                    'status': 'waiting_confirm',
                    'user_id': self._uid,
                    'booking_date': fields.Datetime.now(),
                    'check_in': date_check_in,
                    'check_out': date_check_out,
                    'payment_state': 'done'
                })
            else:
                raise ValidationError('Phong nay dang trong trang thai cho duyet!')
        else:
            raise ValidationError('Unavailable!')
