from odoo import api, models, fields, _


class FeatureFacilityManagement(models.Model):
    _name = 'feature.facility.management'

    name = fields.Char(string='Name')
    icon = fields.Image("Icon")

    def action_change_name(self):
        for rec in self:
            rec.name = 'OK'