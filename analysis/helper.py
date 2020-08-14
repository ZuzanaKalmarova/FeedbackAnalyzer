def change(val_last_week, val_prev_week, perc=1):
    val_change = round((val_last_week / val_prev_week - 1) * 100)
    if abs(val_change) < perc:
        return "flat"
    elif val_change > 0:
        return "up " + str(val_change) + "%"
    else:
        return "down " + str(abs(val_change)) + "%"

