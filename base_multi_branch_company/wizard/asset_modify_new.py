# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from lxml import etree

from odoo import api, fields, models, _
from odoo.osv.orm import setup_modifiers


class AssetModifyNew(models.TransientModel):
    _name = 'asset.modify.new'

    account_asset_id = fields.Many2one('account.asset.asset',string='Depreciation Name', required=True)
    method_number = fields.Integer(string='Number of Depreciations')
    method_period = fields.Integer(string='Period Length')
    category_id = fields.Many2one('account.asset.category', string='Category', required=True)
    branch_id = fields.Many2one(
        comodel_name="res.branch", string="Branch"
    )
    analytic_id = fields.Many2one(
        comodel_name="account.analytic.account", string="Analytic Accounts"
    )

    method_numbers = fields.Integer(string='Number of Depreciations')
    method_periods = fields.Integer(string='Period Length')
    category_ids = fields.Many2one('account.asset.category', string='Category', required=True)
    branch_ids = fields.Many2one(
        comodel_name="res.branch", string="Branch"
    )
    analytic_ids = fields.Many2one(
        comodel_name="account.analytic.account", string="Analytic Accounts"
    )
    value_residuala = fields.Float(string="Residual Value")
    value_residuals = fields.Float(string="Residual Value New")
        
    @api.onchange('account_asset_id')
    def _onchange_account_asset_id(self):
        for record in self:
            
            if record.account_asset_id:
                record.category_id = record.account_asset_id.category_id
                record.branch_id = record.account_asset_id.branch_id
                record.analytic_id = record.account_asset_id.analytic_id
                record.method_number = record.account_asset_id.method_number
                record.method_period = record.account_asset_id.method_period

    @api.onchange('category_ids')
    def _onchange_category_ids(self):
        for record in self:
            if record.category_ids:

                record.branch_ids = record.category_ids.branch_id
                record.analytic_ids = record.category_ids.account_analytic_id
                record.method_numbers = record.category_ids.method_number
                record.method_periods = record.category_ids.method_period



    @api.multi
    def modify(self): 
        asset = self.env['account.asset.asset'].browse(self.account_asset_id.id)
        
        asset_vals = {
            'method_number': self.method_numbers,
            'method_period': self.method_periods,
            'branch_id': self.branch_ids.id,
            'analytic_id': self.analytic_ids.id,
            'category_id': self.category_ids.id,
            'name': asset.name,
            'value': asset.value_residual,
        }

        asset.write({'state':'close'})
        asset.create(asset_vals)
        for i in self.env['account.asset.asset'].search([]):
            if i.name == asset.name and i.id != asset.id:
                i.write({'state': 'open'})
       
        return {'type': 'ir.actions.act_window_close'}
