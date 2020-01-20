post = ('Python Basics', 'Intro Guide To Python', 'Cool content', 'published')

# remove elements from end
# post = post[:-1]

# print(post)

# remove elements from the beginning
# post = post[1:]

# removing specific element (messy/not recomended)

post = list(post)
post.remove('published')
post = tuple(post)