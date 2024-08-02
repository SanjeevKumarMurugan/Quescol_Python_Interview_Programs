student_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}
# Initialize a set to keep track of seen records and a new dictionary for unique entries
seen = set()
unique_data = {}

# Iterate over the items in the original dictionary
for key, value in student_data.items():
    # Convert the dictionary values into a sorted tuple to make it hashable
    items = []
    for k, v in value.items():
        items.append((k, tuple(v)))
    items.sort()
    value_tuple = tuple(items)

    # Check if the tuple is in the seen set
    if value_tuple not in seen:
        seen.add(value_tuple)
        unique_data[key] = value

# Print the result
print(unique_data)
