from nltk import load_parser
cp = load_parser('grammars/book_grammars/sql0.fcfg')
query = 'What cities are located in India'
trees = list(cp.parse(query.split()))
print(trees)

answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
print(answer)

q = ' '.join(answer)
print(q)
