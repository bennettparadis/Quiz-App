# Type hints
# Can specify data types so that functions only work with correct input
# age: int
# name: str
# height: float
# is_human: bool

# can specify the data type within a function with same syntax, also can specify the output datatype with '->'
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

