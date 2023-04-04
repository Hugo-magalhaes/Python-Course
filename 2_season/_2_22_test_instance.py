string = 'Hugo'

if hasattr(string, 'upper'):
    print('Exite')
    print(getattr(string, 'upper')())
