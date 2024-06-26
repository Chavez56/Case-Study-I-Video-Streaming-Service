# Import package
from tabulate import tabulate


# Convert dictionary data to list data
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

data_list = []

for i in data.values():
    data_list.extend(i)

data_converted = data_list


# Class for New User
class New_User:
    """
    A class to represent new user for registration data.
    
    Attributes
    ----------
    new_username (list): data list type for storing new username
    new_username (str): variable to store new username
    DISCOUNT (float): constant variable for calculating discount price

    Methods
    -------
    check_benefit(): 
        Display benefit from each plan (Basic, Standard, Premium)

    pick_plan(new_plan,referral_code):
        Display the chosen plan and calculated price. 
        Get discount 4% if new user has valid referral code from the existing user.

    """

    DISCOUNT = 0.04
    new_username = []

    def __init__(self,new_username: str):

        """
        Construct all the necessary attributes for new user object

        Parameters
        ----------
        new_username (str): variable to store new username
        
        """

        self.new_username = new_username

    def check_benefit(self):
        """
        Display benefit from each plan (Basic, Standard, Premium)

        Parameters
        ----------
        None

        Returns
        -------
        None 

        """

        self.column_name = ["Services", "Basic Plan", "Standard Plan", "Premium Plan"]

        self.content_1 = ['Streaming', '✓', '✓', '✓']
        self.content_2 = ['Download', '✓', '✓', '✓']
        self.content_3 = ['SD Quality', '✓', '✓', '✓']
        self.content_4 = ['HD Quality', ' ', '✓', '✓']
        self.content_5 = ['UHD Quality', ' ', ' ', '✓']
        self.content_6 = ['Number of Devices', 1, 2, 4]
        self.content_7 = ['Content', "3rd party movie only", 
                          "Basic Plan Content \n+ \nSports \n(F1, Football, Basketball)", 
                          "Basic Plan \n+ \nStandard Plan \n+ \nPacFlix Original Series or Movie" 
                          ]
        self.content_8 = ['Price', f"Rp {120_000},-", f"Rp {160_000},-", f"Rp {200_000},-"]

        self.table_content = [self.content_1, 
                              self.content_2,
                              self.content_3,
                              self.content_4,
                              self.content_5,
                              self.content_6,
                              self.content_7,
                              self.content_8
                              ]
    
        print(tabulate(self.table_content,self.column_name, tablefmt="fancy_grid",colalign=('center','center','center','center')))

    def pick_plan(self,new_plan: str,referral_code: str):
        """
        Display the chosen plan and calculated price. 
        Get discount 4% if new user has valid referral code from the existing user.

        Parameters
        ----------
        new_plan (str): the plan that will be chosen
        referral_code (str): the code from the existing user would share with a friend they want to refer to

        Returns
        -------
        None 
        """

        self.new_plan = new_plan.title() + " " + "Plan"
        self.referral_code = referral_code

        New_User.new_username += [self.new_username]

        if self.referral_code !="":
            if self.referral_code in data_converted:
                if self.new_plan in data_converted:
                    if self.new_plan == "Basic Plan":
                        price = int(self.content_8[1].replace('Rp','').replace(',-','')) - New_User.DISCOUNT * int(self.content_8[1].replace('Rp','').replace(',-',''))
                        print(f"Total Price: Rp {int(price)},-")

                    elif self.new_plan == "Standard Plan":
                        price = int(self.content_8[2].replace('Rp','').replace(',-','')) - New_User.DISCOUNT * int(self.content_8[2].replace('Rp','').replace(',-',''))
                        print(f"Total Price: Rp {int(price)},-")

                    elif self.new_plan == "Premium Plan":
                        price = int(self.content_8[3].replace('Rp','').replace(',-','')) - New_User.DISCOUNT * int(self.content_8[3].replace('Rp','').replace(',-',''))
                        print(f"Total Price: Rp {int(price)},-")

                    else:
                        print("Your plan is not exist!")

                elif self.new_plan not in data_converted:
                    print("Check your data input!")

            else:
                raise Exception("Referral Code doesn't exist")
            
        elif self.referral_code =="":
            if self.new_plan in data_converted:
                if self.new_plan == "Basic Plan":
                    price = int(self.content_8[1].replace('Rp','').replace(',-',''))
                    print(f"Total Price: Rp {int(price)},-")

                elif self.new_plan == "Standard Plan":
                    price = int(self.content_8[2].replace('Rp','').replace(',-','')) 
                    print(f"Total Price: Rp {int(price)},-")

                elif self.new_plan == "Premium Plan":
                    price = int(self.content_8[3].replace('Rp','').replace(',-',''))
                    print(f"Total Price: Rp {int(price)},-")

                else:
                    print("Your plan is not exist!")

            elif self.new_plan not in data_converted:
                print("Check your data input!")