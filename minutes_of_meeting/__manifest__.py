{
    'name': 'Minutes Of Meeting',
    'summary': '',
    'version': '16.0.1.0',
    'author': 'Aswin',
    'sequence':'-5',
    'website': 'https://code-ox.com',
    'license': 'LGPL-3',
    'depends': [
        'mail','project'
    ],
    'data':[
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/mom.xml',
        'views/stages.xml',
        'reports/report.xml',
        'reports/meeting.xml',
        'reports/template_pdf.xml',
    ],
    'application':True,
    
}