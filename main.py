# Import module
from src.Existing_User import User
from src.New_User import New_User

# Username data
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}


print("EXISTING USER")
print("--------------")

# Calling class and defining each parameter
user_1 = User(username="Shandy", duration_plan=data["Shandy"][1], current_plan=data["Shandy"][0].replace(" ","").replace("Plan",""))

# Print username, duration plan and current plan
print((user_1.username, user_1.duration_plan, user_1.current_plan))
print()

# Display benefit table for user 1
print("Benefit of the Plan")
print("-----------------------------")
user_1.check_benefit()
print()

# Display benefit of current plan for user 1
print("Summary of Subscription Plan")
print("-----------------------------")
user_1.check_plan()

# Total price if duration plan less than or equal to 12 months
print("-----------------------------")
user_1.upgrade_plan(username="Shandy", current_plan="Basic", new_plan="Standard")

print()
print("------------------------------------------------------------------------------------------------------------------------")
print()

# Calling class and defining each parameter
user_2 = User(username="Cahya", duration_plan=data["Cahya"][1], current_plan=data["Cahya"][0].replace(" ","").replace("Plan",""))

# Print username, duration plan and current plan
print((user_2.username, user_2.duration_plan, user_2.current_plan))
print()

# Display benefit table for user 2
print("Benefit of the Plan")
print("-----------------------------")
user_2.check_benefit()
print()

# Display benefit of current plan for user 2
print("Summary of Subscription Plan")
print("-----------------------------")
user_2.check_plan()

# Total price if duration plan greater than 12 months
print("-----------------------------")
user_2.upgrade_plan(username="Cahya", current_plan="Standard", new_plan="Premium")


print()
print("NEW USER")
print("--------------")


# Calling class and defining parameter
Faizal = New_User(new_username="faizal_icikiwir")
print(f"New User: {Faizal.new_username}")
print()

# Display benefit table for new user
print("Benefit of the Plan")
print("-----------------------------")
Faizal.check_benefit()

# Total price if new user does not have a referral code
print("-----------------------------")
Faizal.pick_plan(new_plan="Basic",referral_code="")

# Total price if new user has a valid referral code
print("-----------------------------")
Faizal.pick_plan(new_plan="Basic",referral_code="shandy-2134")

# Display error if referral code invalid
print("-----------------------------")
Faizal.pick_plan(new_plan="Basic",referral_code="shandy-1234")
