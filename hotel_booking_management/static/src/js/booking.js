odoo.define('hotel_booking_management.process_checkout', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
var core = require('web.core');
var _t = core._t;

publicWidget.registry.hotelBookingRoom = publicWidget.Widget.extend({
    selector: '.oe_website_sale',
    events: {
        'click #hotel_booking_checkout': 'async _onClick'
    },
    /**
     *
     * @override
     */
    init: function () {
        this._super.apply(this, arguments);
        // hide cart
        document.getElementsByClassName('o_wsale_my_cart')[0].style.display = 'none';
    },

    /**
     * @private
     * @param {Event} ev
     */
    _onClick: async function(ev) {
        var self = this;
        ev.preventDefault();
        debugger
        this._rpc({
            model: 'product.template',
            method: 'booking_room',
            args: [JSON.parse(this.el.dataset.productTrackingInfo).item_id],
        })
        .then(function (result) {
            window.location.href = '/booking/checkout';
        });
    },
});
});
