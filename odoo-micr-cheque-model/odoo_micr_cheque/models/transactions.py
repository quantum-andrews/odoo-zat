from odoo import fields, models


class Transactions(models.Model):
    _name = "transactions"
    _description = " model to track the various transaction between accounts"

    date_of_transaction = fields.Date()
    customer_of_account = fields.Char(string='Deposit/Cheque by')
    deducted_account_number = fields.Integer(string='Debit Account Number')
    beneficiary_account_number = fields.Integer(string='Credit Account Number')
    account_bank = fields.Many2one(comodel_name='bank', string='Bank Deposit Issued')
    account_bank_branch = fields.Many2one(comodel_name='bank.branch', string='Bank Branch Deposit Issued')
    amount_involved = fields.Float(string='amount involved in transaction')
