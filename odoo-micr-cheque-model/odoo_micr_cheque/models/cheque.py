from odoo import models, fields, api


class Cheque(models.Model):
    _name = 'cheque'
    _description = 'cheque model'

    cheque_image = fields.Binary(string='Upload Cheque Image')
    cheque_number = fields.Integer(string='Cheque number')

    debit_account = fields.Many2one(comodel_name='account.details', string='Debit/Cheque account')
    debit_account_amount = fields.Float(string='Debit account balance')
    credit_check_null = fields.Integer(string='check on credit value')

    credit_account = fields.Many2one(comodel_name='account.details', string='Credit account')
    credit_account_amount = fields.Float(string='Credit account balance')
    debit_check_null = fields.Integer(string='check on debit value')

    presented_by = fields.Char(string='Presented By')
    issuing_bank_branch = fields.Many2one(comodel_name='bank.branch', string='Bank Branch')
    issuing_bank = fields.Many2one(comodel_name='bank', string='Bank')
    currency = fields.Many2one(comodel_name='res.currency', string='Currency')
    amount = fields.Float()
    date = fields.Date()
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('applied', 'Applied'),
        ('cancelled', 'Cancelled')
    ], default='draft')

    @api.onchange('debit_account')
    def _onchange_debit(self):
        # function triggered when an account is a debit
        if self.debit_account:
            self.credit_check_null = 1

    @api.onchange('credit_account')
    def _onchange_credit(self):
        # function triggered when an account is a credit
        if self.credit_account:
            self.debit_check_null = 2

    def draft_to_confirmed(self):
        self.state = 'confirmed'

    def confirmed_to_applied(self):
        self.state = 'applied'

        if self.credit_check_null == 1 and self.debit_account:
            self.debit_account_amount = self.debit_account_amount - self.amount

            related_debit_models = self.env['account.details'].browse([(self.debit_account.id)])

            for related_d_models in related_debit_models:
                related_d_models.debit_account_amount_final = (
                    related_d_models.debit_account_amount_final + self.debit_account_amount
                )

        if self.debit_check_null == 2 and self.credit_account:
            self.credit_account_amount = self.amount + self.credit_account_amount

            related_credit_models = self.env['account.details'].search([('id', '=', self.credit_account.id)])
            #
            for related_c_models in related_credit_models:
                related_c_models.credit_account_amount_final = (
                    self.credit_account_amount + related_c_models.credit_account_amount_final
                )

        self.env['transactions'].create({
            'date_of_transaction': self.date,
            'deducted_account_number': self.debit_account.account_number,
            'beneficiary_account_number': self.credit_account.account_number,
            'amount_involved': self.amount
        })

    def reverse_confirm_to_draft(self):
        self.state = 'draft'

    def applied_to_cancelled(self):
        self.state = 'cancelled'
