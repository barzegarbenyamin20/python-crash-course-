favorite_language = {
    'benyamin': ['JavaScript', 'TypeScript', 'Python', 'Java'],
    'taha': ['GoLang', 'SQL'],
    "hesam": ['C++'],
    'mehrsam': ['python', 'C#'],
}

for name, languages in favorite_language.items():
    print(f"\n{name.title()}'s favorite language is: ")
    for language in languages:
        print(f'\t{language.title()}')
print('______________________________________________________________')

for name, languages in favorite_language.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite language is: ")
        for language in languages:
            print(f'\t{language.title()}')
    else:
        print(f"\n{name.title()}'s favorite language is: {languages[0].title()}")