# Challenge
author_quotes = {'Albert Einstein': 'In the middle of every difficulty lies opportunity', 
                 'Theodore Roosevelt': 'Do what you can, with what you have, where you are.', 
                 'Nelson Mandela' : "It always seems impossible until it’s done."}

for author, quote in author_quotes.items():
    print(author.title() + " says, " + '"' + quote + '"')