# from odoo.tests.common import TransactionCase
from odoo.tests import TransactionCase, tagged


@tagged('-standard', 'nice')
class AutoTest(TransactionCase):

    def setUp(self):
        super(AutoTest, self).setUp()
        # self.test_room = self.env['product.template'].create({'name': 'Room 1'})
        # self.test_hotel_booking = self.env['hotel.booking.management'].create({'status': 'waiting_confirm'})
        self.test_feature = self.env['feature.facility.management'].create({'name': 'abc'})

    def test_action_confirm_booking(self):
        # self.test_hotel_booking.action_confirm_booking()
        self.test_feature.action_change_name()
        self.assertEqual(self.test_feature.name, 'OK', "Room state should be changed to booked!")
