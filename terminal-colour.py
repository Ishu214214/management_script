"""  terminal colour    """
"""
Regular Colors: 30-37
[30: Black , 31: Red , 32: Green ,33: Yellow ,34: Blue ,35: Magenta ,36: Cyan ,37: White]
Bright Colors: 90-97 
[90: Bright Black (Gray) ,91: Bright Red ,92: Bright Green ,93: Bright Yellow ,94: Bright Blue ,95: Bright Magenta ,96: Bright Cyan ,97: Bright White]

"""
def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


a = "ishu"
print(color_text(a, "32"))

