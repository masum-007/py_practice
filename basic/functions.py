def area_triangle(base, height):
    return base*height/2
def convert_seconds(seconds):
    hrs=seconds//3600
    mins=(seconds%3600)//60
    secs=(seconds%3600)%60
    return hrs, mins, secs


def cnvrt_sec(second):
    hr, remainder = divmod(second, 3600) #divmod returns qoutient and remainder
    min, sec = divmod(remainder, 60)
    #return hr, min, sec
    # The :02d tells Python to use 2 digits and pad with zero
    #return f"{hr:02d}:{minutes:02d}:{sec:02d}"
    #return f" {hr} Hour, {min} Min and {sec} Seconds"
#print("It is" +cnvrt_sec(3665))   

def format_time_text(seconds):
    hr, remainder = divmod(seconds, 3600)
    minutes, sec = divmod(remainder, 60)
    
    # Use 's' to handle the pluralization (e.g., 1 hour vs 2 hours)
    hr_str = "hour" if hr == 1 else "hours"
    min_str = "minute" if minutes == 1 else "minutes"
    sec_str = "second" if sec == 1 else "seconds"
    
    # We use :02d for seconds to get '05' instead of '5'
    return f"{hr} {hr_str} {minutes} {min_str} and {sec:02d} {sec_str}"

print(format_time_text(3665))

#code style
def area_calculator(radius):
    pi=3.1416
    area=pi*(radius ** 2)
    print(area)
area_calculator(7)
