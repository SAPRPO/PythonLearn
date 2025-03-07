def make_shirt( text, size='L'):
    print(f"Shirt size: '{size}' and text on shirt: '{text.title()}'\n")

make_shirt(size = 'XL', text ='Slayer')

make_shirt(size='L', text='Metallica')
make_shirt('Kreator')

groups=['burzum', 'sabaton', 'manowar']

for group in groups:
    make_shirt(group)