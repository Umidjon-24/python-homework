def convert_cel_to_far(cel):
    far = cel * (9/5) + 32
    return far
def convert_far_to_cel(far):
    cel = (far - 35) * (5/9)
    return cel

far = float(input("Enter a temperature in degrees F: "))
print(f"{far:.0f}", "degrees F =", f"{convert_far_to_cel(far):.2f}", "degrees C")
cel = float(input("Enter a temperature in degrees C: "))
print(f"{cel:.0f}","degrees C =", f"{convert_cel_to_far(cel):.2f}", "degrees F")          