from odoo import api, models, fields, _


class RoomManagement(models.Model):
    _name = 'room.management'

    name = fields.Char(string='Name')
    room_type = fields.Selection([('single', 'Single'), ('double', 'Double')],
                                 string='Room Type', default='single', required=True)
    room_price = fields.Float(string='Price', compute='_compute_room_price', store=True)
    rental_type = fields.Selection([('hour', 'Hour'), ('overnight', 'Overnight')],
                                   string='Rental Type', default='hour', required=True)
    hour_rental = fields.Integer(string="Hour rental", default=2)
    room_image = fields.Binary(string='Image', attachment=True)
    img_url = fields.Char(string='Img Url', compute='_compute_img_url', store=True)

    @api.depends('room_type')
    def _compute_room_price(self):
        for rec in self:
            if rec.room_type == 'single':
                rec.room_price = 15
            else:
                rec.room_price = 30

    # @api.depends('room_image')
    # def _compute_img_url(self):
    #     base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
    #     for rec in self:
    #         if rec.room_image:
    #             rec.img_url = base_url + f'/web/image?model=hotel.booking.management&id={rec.id}&field=room_image'
