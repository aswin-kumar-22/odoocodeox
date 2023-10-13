{
    'name': 'Delivery Boy',
    'summary': '',
    'version': '16.0.1.0',
    'author': 'Aswin',
    'sequence':'-10',
    'website': 'https://code-ox.com',
    'license': 'LGPL-3',
    'depends': [
        'mail','stock'
    ],
    'data':[
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'wizard/wizarddelivery.xml',
        'views/menu.xml',
        'views/delivery_boy.xml',
        'views/delivery_status.xml',
    ],
    'application':True,
    
}