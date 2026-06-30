text = "Saad"

# ljust() ---> aligns text to the left & adds padding on right side
    # Syntax: str.ljust(width, fillchar)
print(text.ljust(10,"-"))

# rjust() ---> aligns text to the right & adds padding on left side
print(text.rjust(10,"-"))

''' =========== Use Cases =========== '''

# Table formatting 
print("Name".ljust(10), "Age".rjust(5))
print("Saad".ljust(10), str(20).rjust(5))

# Menu design
print("Option 1".ljust(20, ".") + "Open")
print("Option 2".ljust(20, ".") + "Exit")

# Reports Alignment
print("Marks:".ljust(10) + "85".rjust(5))
