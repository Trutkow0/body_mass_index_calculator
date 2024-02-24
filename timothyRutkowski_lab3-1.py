# Timothy Rutkowski 02/06/2024 timothyRutkowski_lab3-1.py

# This program will calculate Body Mass Index (BMI) based on weight and height
# as input by the user and output the users Body Mass Indicator and whether 
# their weight is over, under, or optimal according to the index.

# Define variables and gets user's weight in pounds and height in inches
userWeightLbs = float(input('Please enter your weight in pounds: '))
userHeightInches = float(input('Please enter your height in inches: '))

# Convert user's inputs to metric
userWeightKilos = userWeightLbs * 0.454
userHeightMeters = userHeightInches / 39.37

# Calculates user's BMI
BMI = "{:.2F}".format(userWeightKilos / (userHeightMeters * userHeightMeters))

# Output user's BMI
print('Your BMI is:',BMI)

# Outputs whether user's weight is over, under, or optimal
if float(BMI) > 25: 
    print('You are overweight')
elif float(BMI) < 18.5: 
    print('You are underweight')
else: 
    print('Your weight is optimal')
