import functions

desired_length = functions.desired_password_length()
password = functions.random_character_picker(desired_length)

print('Here\'s your new password: ' + password)
