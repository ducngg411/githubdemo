def get_message(name, is_student, age):
    message = f"Hello {name}"

    if is_student and (age <= 18 or age > 65):
        message += " - congratulations, you qualify for a 20% discount"
    elif is_student or (age <= 18 or age > 65):
        message += " - congratulations, you qualify for a 10% discount"
    else:
        message += " - sorry, you need to pay the regular price"

    return message

name = input("What is your name? ")

student_str = input("Are you a student [y/n]? ")
is_student = student_str.lower() in ("y", "yes")

age_str = input("How old are you? ")
age = int(age_str)

message = get_message(name, is_student, age)
print(message)

print()
input("Press return to continue ...")
