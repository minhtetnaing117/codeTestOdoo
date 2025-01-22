from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    branch_ids = fields.One2many(
        comodel_name="res.branch",
        inverse_name="company_id",
    )