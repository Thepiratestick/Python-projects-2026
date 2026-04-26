import datetime

question = input("Hello stark at your service: ").strip().lower()
if question == "what time is it":
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("The current time is:", current_time)
else:
    print("I can answer 'what time is it' for now.")
