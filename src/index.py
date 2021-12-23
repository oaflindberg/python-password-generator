import random
from characterPicker import randomItemPicker
from characters import characters
from desiredPasswordLength import passwordLength

desiredLength = passwordLength()

password = []

randomItemPicker(password, desiredLength)

shuffledPassword= ''.join(random.sample(password, len(password)))

print('Here\'s your new password: ' + shuffledPassword)


