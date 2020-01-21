sentence = 'the quick brown fox jumped over the lazy dog'
word = 'dog'

if word in sentence:   # can lowercase the whole sentence with: if word.lower() in sentence.lower()
  print('The word was found')
else:
  print('the word was not found')


nums = [1, 2, 3, 4, 5]

if 3 in nums:
  print('the number was found')
else:
  print('the number was NOT found')