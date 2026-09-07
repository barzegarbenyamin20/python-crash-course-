favorite_language = {
    'benyamin': 'JavaScript',
    'taha': 'JavaScript',
    'hesam': 'C',
    'mehrsam': 'Rust'
}
print('following langs is => ')
for lang in set(favorite_language.values()):
    print(lang.title())