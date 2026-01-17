classes_number = int(input("How many lecture will you enter?"))
total_note = 0
if classes_number <= 0 :
    print("Please enter a valid number of lecture")
else :
    for i in range(1 , classes_number + 1):
        note_value = float(input(f"{i}. enter the lecture note: "))
        total_note += note_value
    Average = total_note / classes_number

    print(f"The average note is: {Average }")

    if Average >= 50 :
        print("Result: You passes successfully")
    else :
        print("Result: Unfortunately, you stayed. You should work harder")