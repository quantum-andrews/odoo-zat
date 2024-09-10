from odoo import fields,models


class Bank(models.Model):
    _name = "bank"
    _description = "model for tracking various banks"
    _rec_name = "bank_name"

    bank_name = fields.Char(string="Bank")
    abbreviation = fields.Char(string="Abbreviation")
    code = fields.Char(string="Code")
    country = fields.Many2one(comodel_name='res.country', string="Country")


class BankBranch(models.Model):
    _name = "bank.branch"
    _description = "model to handle to various bank branches of the banks"
    _rec_name = "bank_branch"

    bank_name_branch = fields.Many2one(comodel_name='bank', string='Bank')
    bank_branch = fields.Char(string='Branch Name')
