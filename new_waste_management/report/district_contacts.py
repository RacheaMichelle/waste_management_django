# report/district_contacts.py
DISTRICT_CONTACTS = {
    'Kampala': '256700000001',
    'Wakiso': '256700000002',
    'Masindi': '256700000003',
    'Kasese': '256700000004',
    'Iganga': '256700000005',
    'Bushenyi': '256700000006',
    'Gulu': '256700000007',
    'Lira': '256700000008',
    'Mbarara': '256700000009',
    'Jinja': '256700000010',
    'Mbale': '256700000011',
    'Arua': '256700000012',
    'Soroti': '256700000013',
    'Fort Portal': '256700000014',
    'Hoima': '256700000015',
    'Masaka': '256700000016',
    'Mukono': '256700000017',
    'Nebbi': '256700000018',
    'Tororo': '256700000019',
    'Kabale': '256700000020',
    'Mityana': '256700000021',
    'Adjumani': '256700000022',
    'Pallisa': '256700000023',
    'Kumi': '256700000024',
    'Bundibugyo': '256700000025'
}

def get_district_contact(district):
    return DISTRICT_CONTACTS.get(district, '256700000000')  # Default number