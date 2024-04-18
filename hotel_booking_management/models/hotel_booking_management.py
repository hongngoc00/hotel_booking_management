from datetime import date
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
    check_in = fields.Date(string='Check-in')
    check_out = fields.Date(string='Check-out')
    payment_state = fields.Selection([('done', 'Done'), ('pending', 'Pending'), ('fail', 'Failed')],
                                     string='Payment state')

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

    def cancel_booking(self):
        self.status = 'canceled'
