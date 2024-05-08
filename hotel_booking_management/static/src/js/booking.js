odoo.define('hotel_booking_management.process_checkout', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
var core = require('web.core');
var _t = core._t;

publicWidget.registry.hotelBookingRoom = publicWidget.Widget.extend({
    selector: '.oe_website_sale',
    events: {
        'click #hotel_booking_checkout': 'async _onClick',
        'click .close_confirm_booking': 'async _close_confirm_booking',
        'click #confirm-booking': 'async _confirm_booking'
    },
    /**
     *
     * @override
     */
    init: function () {
        this._super.apply(this, arguments);
        // hide cart
        //document.getElementsByClassName('o_wsale_my_cart')[0].style.display = 'none';
    },

    /**
     * @private
     * @param {Event} ev
     */
    _onClick: async function(ev) {
        var self = this;
        ev.preventDefault();
        document.getElementById("nenmodal-1").classList.toggle("active");
//        this._rpc({
//            model: 'product.template',
//            method: 'booking_room',
//            args: [JSON.parse(this.el.dataset.productTrackingInfo).item_id],
//        })
//        .then(function (result) {
//            window.location.href = '/booking/checkout';
//        });
    },
    _confirm_booking:  async function(ev) {
        var self = this;
        ev.preventDefault();
        var name = document.getElementById('name').value;
        var phone = document.getElementById('phone').value;
        var address = document.getElementById('address').value;
        var check_in = document.getElementById('check-in').value;
        var check_out = document.getElementById('check-out').value;
        debugger
        this._rpc({
            model: 'product.template',
            method: 'booking_room',
            args: [JSON.parse(this.el.dataset.productTrackingInfo).item_id, name, phone, address, check_in, check_out],
        })
        .then(function (result) {
            document.getElementById("nenmodal-1").classList.toggle("active");
            alert('Đặt phòng thành công!')
        });
    },
    _close_confirm_booking: function (){
        document.getElementById("nenmodal-1").classList.toggle("active");
    }
});
});
