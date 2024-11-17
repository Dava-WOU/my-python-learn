def day_of_week(day):
    match day:
        case 1:
            return "it is sunday"
        case 2:
            return "it is monday"
        case 3:
            return "it is tuesday"
        case 4:
            return "it is wednesday"
        case 5:
            return "it is thursday"
        case 6:
            return "it is friday"
        case 7:
            return "it is saturday"
        case _:
            return "invalid day"
print(day_of_week(1))

def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return True
        case "monday" | "tuesday"  | "wednesday" | "thursday" | "friday":
            return False
        case _:
            return "invalid day"
print(is_weekend("saturday"))