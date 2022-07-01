from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Patient Tag"

    def test_function(self):
        return
