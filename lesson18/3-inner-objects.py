users = {
    'beni': {
        'first': "benyamin",
        'last': "barzegar",
        'location': "ardabil"
    },
    'taha': {
        'first': "taha",
        'last': "barzegar",
        'location': "ardabil"
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tlocation: {location.title()}")