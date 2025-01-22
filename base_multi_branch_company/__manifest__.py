{
    "name": "Base multi branch company",
    "version": "11.0.1.0.0",
    "license": "",
    "category": "base",
    "summary": "Add multi branch of company",
    "author": "Min Htet Naing",
    "website": "",
    "depends": ["base","account","analytic","account_asset"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_branch_view.xml",
        "views/res_company.xml",
        "views/account_asset.xml",
        "wizard/asset_modify_new.xml",
    ],
    "installable": True,
}