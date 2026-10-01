acronyms = ['LOL', 'BRB']

acronyms.append('BFN')
acronyms.append('OMG')
acronyms.append('TTYL')
acronyms.append('IDK') 
acronyms.append('SMH')
acronyms.append('YOLO')

acronyms.remove('BFN')

for acronym in acronyms:
  print(acronym)

word = 'BFN'
if word in acronyms:
    print(f"{word} is in the list.")
else:
    print(f"{word} is not in the list.")