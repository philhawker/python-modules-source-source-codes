post = ('Python Basics', 'Intro Guide To Python', 'Cool content')

# post = post + ('published',) This is the same as below
post += ('published',)  # always add , when adding to a tuple

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)
