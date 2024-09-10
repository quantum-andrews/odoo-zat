from odoo import fields, models


class AccountDetails(models.Model):
    _name = "account.details"
    _description = " model to house the various account details"
    _rec_name = 'account_number'

    date_of_creation = fields.Date()
    customer_name = fields.Char(string='Name of Customer')
    account_number = fields.Integer(string='Account Number')
    account_bank = fields.Many2one(comodel_name='bank', string='Bank')
    account_bank_branch = fields.Many2one(comodel_name='bank.branch', string='Bank Branch')

    debit_account_final = fields.Many2one(comodel_name='account.details', string='Final Debit/Cheque account')
    debit_account_amount_final = fields.Float(string='Debit account balance')

    credit_account_final = fields.Many2one(comodel_name='account.details', string='Final Credit account')
    credit_account_amount_final = fields.Float(string='Credit account balance')

    amount = fields.Float(string='amount')

