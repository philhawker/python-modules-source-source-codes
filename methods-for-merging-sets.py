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