
"""
Tip Calculator
Given the price of your meal and a custom tip percent, 
return an array with three tip values; 15%, 20%, and the custom amount.

Prices will be given in the format: "$N.NN".
Custom tip percents will be given in this format: "25%".
Return amounts in the same "$N.NN" format, rounded to two decimal places.
For example, given a "$10.00" meal price, and a "25%" custom tip value, 
return ["$1.50", "$2.00", "$2.50"].
"""

def calculate_tips(meal_price, custom_tip):

    meal_price = float(meal_price.replace("$", ""))
    custom_tip = float(custom_tip.replace("%", "")) / 100

    return [f"${meal_price * 0.15:.2f}", f"${meal_price * 0.2:.2f}", f"${meal_price * custom_tip:.2f}"]

print(calculate_tips("$10.00", "25%"))
