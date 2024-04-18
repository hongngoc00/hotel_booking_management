from odoo import api, models, fields, _


class FeatureFacilityManagement(models.Model):
    _name = 'feature.facility.management'

    name = fields.Char(string='Name')
    icon = fields.Image("Icon")
