import win32api

from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class HotelBookingManagement(models.Model):
    _name = 'hotel.booking.management'

    room_id = fields.Many2one('product.template', string='Room')
    status = fields.Selection([('waiting_confirm', 'Waiting for confirm'), ('booked', 'Booked'), ('canceled', 'Canceled')],
                              string='Status', default='canceled', required=True)
    room_type = fields.Selection(related='room_id.room_type', string='Type', store=True)
    user_id = fields.Many2one('res.users', string='User')
    phone_number = fields.Char(related='user_id.work_phone', store=True, string="Phone number")
    user_details = fields.Text(string="User details", compute="_compute_user_details", store=True)
    price = fields.Float(related='room_id.list_price', store=True, string='Price')
    booking_date = fields.Date(string='Booking date')

    @api.depends('user_id')
    def _compute_user_details(self):
        for rec in self:
            if rec.user_id:
                rec.user_details = f"Name: {rec.user_id.name} \n" \
                                   f"Phone no: {rec.user_id.work_phone}"

    def action_confirm_booking(self):
        for rec in self:
            rec.status = 'booked'
            rec.room_id.state = 'unavailable'

    def action_reject_booking(self):
        for rec in self:
            rec.status = 'canceled'
            rec.room_id.state = 'available'


class FeatureFacilityManagement(models.Model):
    _name = 'feature.facility.management'

    name = fields.Char(string='Name')


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
    room_description = fields.Text(string='Description')

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

    def booking_room(self):
        if self.state == 'available':
            check_room = self.env['hotel.booking.management'].sudo().search(
                [('room_id', '=', self.id), ('status', '!=', 'canceled')])
            if not check_room:
                self.env['hotel.booking.management'].sudo().create({
                    'room_id': self.id,
                    'status': 'waiting_confirm',
                    'user_id': self._uid,
                    'booking_date': fields.Datetime.now()
                })
            else:
                raise ValidationError('Phong nay dang trong trang thai cho duyet!')
        else:
            win32api.MessageBox(0, 'This room are Unavailable', 'Message box', 0x00001000)

