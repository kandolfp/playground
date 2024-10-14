

def generate_lists(list1, list2):
    # Erstellen von list_zip
    list_zip = [val for pair in zip(list1, list2) for val in pair]
    
    # Erstellen von list_odd
    list_odd = [x for x in list1 if x % 2 != 0] + [x for x in list2 if x % 2 != 0]
    
    # Erstellen von list_zip_reverse
    list_zip_reverse = [val for pair in zip(reversed(list1), reversed(list2)) for val in pair]
    
    return list_zip, list_odd, list_zip_reverse

# Beispiel
list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]

list_zip, list_odd, list_zip_reverse = generate_lists(list1, list2)

# Ausgeben der Ergebnisse
print("list_zip:", list_zip)
print("list_odd:", list_odd)
print("list_zip_reverse:", list_zip_reverse)

