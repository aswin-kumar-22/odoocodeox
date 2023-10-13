{
    'name': 'XL Report',
    'summary': '',
    'version': '16.0.1.0',
    'author': 'Aswin',
    'sequence':'-15',
    'website': 'https://code-ox.com',
    'license': 'LGPL-3',
    'depends': [
        'sale','report_xlsx'
    ],
    'data':[
        'security/ir.model.access.csv',
        'wizard/xl_report.xml',
        'report/report.xml',
        
    ],
    'application':True,
    
}