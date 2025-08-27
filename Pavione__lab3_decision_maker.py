
# Initialize an empty list to store advice
advice_list = []

# Get user input for temperature
try:
    temp = float(input("What is the current temperature (in °C)? "))
except ValueError:
    print("Invalid input. Assuming 20°C as default temperature.")
    temp = 20.0

# Get user input for raining status
raining = input("Is it raining? (yes/no): ").strip().lower()
if raining not in ['yes', 'no']:
    print("Invalid input. Assuming it is not raining.")
    raining = 'no'

# Get user input for umbrella availability
umbrella = input("Do you have an umbrella? (yes/no): ").strip().lower()
if umbrella not in ['yes', 'no']:
    print("Invalid input. Assuming you do not have an umbrella.")
    umbrella = 'no'

# Get user input for wind speed
try:
    wind_speed = float(input("What is the current wind speed (in km/h)? "))
except ValueError:
    print("Invalid input. Assuming wind speed of 0 km/h.")
    wind_speed = 0.0

# Get user input for time of day
time_of_day = input("What time of day is it? (morning/afternoon/evening/night): ").strip().lower()
if time_of_day not in ['morning', 'afternoon', 'evening', 'night']:
    print("Invalid input. Assuming it is afternoon.")
    time_of_day = 'afternoon'

# Decision logic for temperature
if temp < 10:
    advice_list.append("Wear a coat to stay warm.")
elif temp >= 10 and temp < 20:
    advice_list.append("Consider wearing a light jacket.")
else:
    advice_list.append("No need for a coat; the temperature is comfortable.")

# Decision logic for raining and umbrella
if raining == 'yes':
    if umbrella == 'yes':
        advice_list.append("Take your umbrella since it's raining.")
    else:
        advice_list.append("It's raining. Wait for the rain to stop or find shelter.")
else:
    advice_list.append("It's not raining, so enjoy the weather!")

# Decision logic for wind speed
if wind_speed > 30:
    advice_list.append("It's very windy; secure loose items and avoid open areas.")
elif wind_speed > 15:
    advice_list.append("Moderate wind; a windbreaker might be helpful.")
else:
    advice_list.append("Wind speed is calm; no special precautions needed.")

# Decision logic for time of day
if time_of_day in ['evening', 'night']:
    advice_list.append("It's getting dark; bring a flashlight or stay in well-lit areas.")
elif time_of_day == 'morning':
    advice_list.append("It's morning; a great time for outdoor activities.")
else:  # afternoon
    advice_list.append("It's afternoon; perfect for a walk if the weather permits.")

# Print a summary of the advice
print("\n=== Weather Advice Summary ===")
if advice_list:
    for i, advice in enumerate(advice_list, 1):
        print(f"{i}. {advice}")
else:
    print("No specific advice provided based on your inputs.")

# Final message
print("\nStay safe and enjoy your day!")