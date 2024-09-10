{
    "name": "MICR Cheque",
    "summary": "MICR model for cheque images",
    "author": "Andrews Mensah",
    "website": "https://github.com/TheQuantumGroup/odoo-account",
    "category": "Uncategorized",
    "version": "17.0.0.0.0",
    "license": "Other proprietary",
    "depends": [
        "base",
        "account",
    ],
    "assets": {
        "web.assets_backend": ["odoo_micr_cheque/static/src/css/module.scss"],
    },

    "data": [
        "security/ir.model.access.csv",
        "views/account.xml",
        "views/bank.xml",
        "views/cheque.xml",
        "views/transactions.xml",

    ],
    "application": True,
    "external_dependencies": {
        "python": [
            "inflect",
            "pytesseract",
        ],
    },
}
