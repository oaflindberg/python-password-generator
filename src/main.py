import functions

desired_length = functions.desired_password_length()
password = functions.generate_password(desired_length)

print(f'Here\'s your new password: {password}')
