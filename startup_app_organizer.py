import os
import json

print("Welcome to the Startup App Organizer!")
print("Select the app group you want to launch: ")
user_input = input("Enter a group name: ")


def launch_app(user_input):
    try:
        with open('./groups/' + user_input + '.json', 'r') as file:
            apps_data = json.load(file)
            for app in apps_data:
                os.system(app['command'])
    except Exception as e:
        print(f"Error: {e}")

# Call the function to launch Slack
launch_app(user_input)
