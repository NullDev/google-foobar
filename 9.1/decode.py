import base64

MESSAGE = '''
CE8SEVMUSxcWUQ5PU1UUGgQFRFACREIVQRkfFxIPFAEXVxREQhNdARYXHg0FQxxXCQEDEEEHBwFU
SFtEFx5ABxcTShwRHhZPTUQXFk0MDBNYEB4XHRxGRApXCRELGkEWGBcXT01EFwVPBgcfWgZUUklI
RhdREUtDSVYJExwdVEhbRBcARwpEUVM=
'''

KEY = 'shad0w.dev.usr'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print(''.join(result))
# {'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}
