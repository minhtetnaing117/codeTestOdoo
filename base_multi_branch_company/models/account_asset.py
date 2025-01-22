from odoo import fields, models, api, _
from datetime import date, datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF

class AccountAssetAsset(models.Model):
    _inherit = "account.asset.asset"

    branch_id = fields.Many2one(
        comodel_name="res.branch", string="Branch"
    )
    analytic_id = fields.Many2one(
        comodel_name="account.analytic.account", string="Analytic Accounts"
    )

    @api.onchange('category_id')
    def _onchange_category_id(self):
        for record in self:
            if record.category_id:
                record.branch_id = record.category_id.branch_id
                record.analytic_id = record.category_id.account_analytic_id

class AccountAnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    branch_id = fields.Many2one('res.branch', string="Branch", compute='_compute_branch')

    @api.depends('company_id')
    def _compute_branch(self):
        for record in self:
            for branch in record.company_id.branch_ids:
                if branch.analytic_id.id == record.id:
                    record.branch_id = branch.id
                    break


class AccountAssetCategory(models.Model):
    _inherit = "account.asset.category"

    branch_id = fields.Many2one('res.branch', string="Branch", compute='_compute_branch')

    @api.depends('account_analytic_id')
    def _compute_branch(self):
        for record in self:
            record.branch_id = record.account_analytic_id.branch_id
