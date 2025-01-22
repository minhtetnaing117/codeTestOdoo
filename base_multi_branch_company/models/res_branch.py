from odoo import fields, models


class ResBranch(models.Model):
    _name = "res.branch"
    _description = "Company Branches"

    name = fields.Char(string="Branch", required=True)
    company_id = fields.Many2one(
        comodel_name="res.company", required=True, string="Company"
    )
    analytic_id = fields.Many2one(
        comodel_name="account.analytic.account", required=True, string="Analytic Accounts"
    )
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one(
        comodel_name="res.country.state",
        string="Fed. State",
        domain="[('country_id', '=?', country_id)]",
    )
    country_id = fields.Many2one(comodel_name="res.country")
    email = fields.Char()
    phone = fields.Char()
    active = fields.Boolean(default=True)

    _sql_constraints = [("name_uniq", "unique(name)", "Branch must be unique!")]