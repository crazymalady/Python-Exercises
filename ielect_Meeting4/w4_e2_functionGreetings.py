def greeting(lang):
    if lang == 'es':
        return 'Hola!'
    elif lang == 'fr':
        return 'Bonjour!'
    else:
        return 'Hello!'

print( greeting('es'), 'Jennifer' )
print( greeting('fr'), 'Jabez' )
print( greeting('en'), 'Borja' )