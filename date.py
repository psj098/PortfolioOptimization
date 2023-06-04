from datetime import date

def get_date(): 
    # Date today, format it as "dd/mm/yyyy"
    date_today = date.today().strftime("%d/%m/%Y")

    # Date 10 years ago 
    date_today_split = date_today.split("/") 
    date_today_split[2] = str(int(date_today_split[2])-10)
    date_start = "/".join(date_today_split) 
    return date_start, date_today 