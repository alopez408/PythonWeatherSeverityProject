def main():
    total_rain = 0.0
    total_wind = 0.0
    count = 0

    while True:
        # Get input from the user
        try:
            rain, wind = map(float, input("Enter rain (in inches) and wind (in mph), or -1.0 to end: ").split())

            # Sentinel value to end the loop
            if rain == -1.0:
                break

            total_rain += rain
            total_wind += wind
            count += 1

        except ValueError:
            print("Invalid input. Please enter two decimal values separated by a space.")

    if count > 0:
        # Calculate average rain and wind
        avg_rain = total_rain / count
        avg_wind = total_wind / count

        # Calculate weather severity
        severity = (avg_rain * 10) + avg_wind

        # Output results
        print(f"The average rain is {avg_rain:.1f} inches")
        print(f"The average wind is {avg_wind:.1f} mph")
        print(f"The weather severity for these {count} readings is: {severity:.1f}")
    else:
        print("No valid data entered.")

# Run the program
main()