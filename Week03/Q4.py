monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)

print("Attended both class:", monday_class & wednesday_class)
print("Attended either class:", monday_class | wednesday_class)
print("Only attended Monday class:", monday_class - wednesday_class)
print("Only attended one class (not both):", monday_class ^ wednesday_class)

all_classes = monday_class | wednesday_class
print("Is Monday subset of all students?", monday_class <= all_classes)
