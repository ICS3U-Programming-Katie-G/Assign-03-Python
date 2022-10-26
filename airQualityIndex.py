#!/usr/bin/env python3
# Created by: Katie G
# Created on: October 3rd, 2022
# This program gets the location and air
# quality index from the user, then checks
# to make sure it is a valid input using a
# try...catch statement. Then, the program
# checks to see which category of warning
# the user's inputted air quality index falls
# under, and displays it back to the user along
# with the location of the user
# in a custom message.


# this function determines the air quality
# warning based on the air quality index
# the user inputted, along with a custom
# message based on the user's location.
# The program uses if...else if... else,
# nested if statements, and try...catch
# statements to perform all of this.
def main():
    # introductory text that explains to the
    # user what this program does. Includes
    # a little bit of lore about the hat man
    # just to keep things interesting :)
    print(
        "Hello! Have you heard of the hat man? "
        "The hat man wants to help you! Air can be "
        "dangerous sometimes, so this program, "
        "which is approved and sanctioned by the hat man, "
        "will tell you the advisory for the air quality. "
    )

    # getting the air quality index and the location
    # of the user.
    userIndex = input(
        "Please input the air quality index for your region "
        "and you will get the hat man’s special certified air warning :) "
    )
    userLocation = input(
        "Please input the name of your location. The hat man desires it :) "
    )

    # using a try...catch statement to check to see if the user inputted
    # a valid integer.
    try:
        userIndexAsInt = int(userIndex)
        # checks to see if the user's integer is between
        # 0 to 500.
        if userIndexAsInt >= 0 and userIndexAsInt <= 500:
            # uses an if...else if... else statement to see
            # which warning the user air quality index
            # falls under.
            if userIndexAsInt >= 0 and userIndexAsInt <= 50:
                print(
                    "The air quality index for the location '{}', "
                    "with the value you entered, ({}), is “Good”. "
                    "This means it is safe for you to go outside - "
                    "air pollution poses "
                    "little/no risk.".format(userLocation, userIndexAsInt)
                )
            elif userIndexAsInt >= 51 and userIndexAsInt <= 100:
                print(
                    "The air quality index for the location '{}', "
                    "with the value you entered, ({}), "
                    "is “Moderate”. This means it is still acceptable to go outside, "
                    "however there is a moderate risk for a small population of people "
                    "who are unusually sensitive "
                    "to air pollution.".format(userLocation, userIndexAsInt)
                )
            elif userIndexAsInt >= 101 and userIndexAsInt <= 150:
                print(
                    "The air quality index for the location '{}', "
                    "with the value you entered, ({}), "
                    "is “Unhealthy For Sensitive Groups”. This means that those in sensitive groups "
                    "may have moderate health effects. "
                    "The general population "
                    "is typically not affected.".format(userLocation, userIndexAsInt)
                )
            elif userIndexAsInt >= 151 and userIndexAsInt <= 200:
                print(
                    "The air quality index for the location '{}', "
                    "with the value you entered, ({}), "
                    "is “Unhealthy”. This means that all members "
                    "of the population will start experiencing "
                    "mild/moderate health effects, and those in sensitive"
                    "groups may experience severe effects. It is not "
                    "advisable to go outside.".format(userLocation, userIndexAsInt)
                )
            elif userIndexAsInt >= 201 and userIndexAsInt <= 300:
                print(
                    "The air quality index for the location '{}', "
                    "with the value you entered, ({}), "
                    "is “Very Unhealthy”. This means that all members of "
                    "the population will experience moderate/severe health "
                    "effects - it is not advisable "
                    "to go outside.".format(userLocation, userIndexAsInt)
                )
            elif userIndexAsInt >= 301 and userIndexAsInt <= 500:
                print(
                    "The air quality index for the location '{}', "
                    "with the value you entered, ({}), "
                    "is “Hazardous”. This means that the entire population "
                    "is almost surely to be affected - this level is "
                    "considered an emergency health warning. It is "
                    "not safe to go outside.".format(userLocation, userIndexAsInt)
                )
            else:
                print(
                    "I'm sorry, the value you entered, ({}), "
                    "is not valid. Please only enter an integer "
                    "from 0-500".format(userIndexAsInt)
                )
        else:
            print(
                "I'm sorry, the value you entered, ({}), "
                "is not valid. Please only enter an integer "
                "from 0-500".format(userIndexAsInt)
            )
    except Exception:
        print(
            "I'm sorry, the value you entered, ({}), is not valid. "
            "Please only input an integer from 0-500.".format(userIndexAsInt)
        )
    finally:
        print(
            "Regardless of your result, "
            "please be safe and follow all public health advisories for your region. "
            "The hat man thanks you for using this program."
        )


if __name__ == "__main__":
    main()