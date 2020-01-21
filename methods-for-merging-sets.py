tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

#merged tages

merged_tags = tags_one | tags_two   # will combine both sets and NOT repeat duplicates

print(merged_tags)


# tags in tags_one but NOT in tags_two

exclusive_to_tags_two = tags_two - tags_one   #this returns tags that only exist in tags_one
exclusive_to_tags_one = tags_one - tags_two   #this returns tags that only exist in tags_two

print(exclusive_to_tags_one)
print(exclusive_to_tags_two)


# tags found in both/shared in both sets

universal_tags = tags_one & tags_two

print(universal_tags)