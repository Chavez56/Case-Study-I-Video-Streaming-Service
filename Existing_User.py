# Import package
from tabulate import tabulate


# Username data
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

# Class for the existing user
class User:
    """
    A class to represent the existing user.
    
    Attributes
    ----------
    username (str): the existing username
    duration_plan (float): duration of subscribed plan (in months)
    current_plan (str): current subcribed plan (Basic, Standard, Premium)
    DISCOUNT (float): constant variable for calculating discount price

    Methods
    -------
    check_benefit(): 
        Display benefit from each plan (Basic, Standard, Premium)

    check_plan(username): 
        Display current plan from the existing user

    upgrade_plan(username,current_plan,new_plan):
        Display upgraded plan and calculated price. 
        Get discount 5% if duration subscribed plan greater than 12 months
        (for existing user).

    """

    DISCOUNT = 0.05

    def __init__(self,username: str,duration_plan: float,current_plan: str):
        """
        Construct all the necessary attributes for the existing user object

        Parameters
        ----------
        username (str): the existing username
        duration_plan (float): duration of subscribed plan (in months)
        current_plan (str): current subcribed plan (Basic, Standard, Premium)

        """
       
        self.username = username.title()
        self.duration_plan = duration_plan
        self.current_plan = current_plan.title()

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

    def check_plan(self):
        """
        Display current plan from the existing user

        Parameters
        ----------
        username (str): the existing username

        Returns
        -------
        None 
        
        """
        
        if self.username in data.keys():

            if self.current_plan == "Basic":
                print(f"Current Plan: {self.current_plan} Plan")
                print()
                print(f"Duration Plan: {self.duration_plan} months")
                print()
                print(f"{self.current_plan} Pacflix Benefit List")
                print("----------------------------------------------")
                col_name = ["Services",self.current_plan]
                benefit_list = [[self.table_content[i][0],self.table_content[i][1]] for i in range(len(self.table_content))]
                print(tabulate(benefit_list, col_name,tablefmt="fancy_grid",colalign=('center','center')))

            elif self.current_plan == "Standard":
                print(f"Current Plan: {self.current_plan} Plan")
                print()
                print(f"Duration Plan: {self.duration_plan} months")
                print()
                print(f"{self.current_plan} Pacflix Benefit List")
                print("----------------------------------------------")
                col_name = ["Services",self.current_plan]
                benefit_list = [[self.table_content[i][0],self.table_content[i][2]] for i in range(len(self.table_content))]
                print(tabulate(benefit_list, col_name,tablefmt="fancy_grid",colalign=('center','center')))

            elif self.current_plan == "Premium":
                print(f"Current Plan: {self.current_plan} Plan")
                print()
                print(f"Duration Plan: {self.duration_plan} months")
                print()
                print(f"{self.current_plan} Pacflix Benefit List")
                print("----------------------------------------------")
                col_name = ["Services",self.current_plan]
                benefit_list = [[self.table_content[i][0],self.table_content[i][3]] for i in range(len(self.table_content))]
                print(tabulate(benefit_list, col_name,tablefmt="fancy_grid",colalign=('center','center')))

            else:
                print("No available benefit for your current plan, try again!")

        else:
            print("Username is not found!")

    def upgrade_plan(self,username: str,current_plan: str,new_plan: str):
        """
        Display upgraded (new) plan and calculated price. 
        Get discount 5% if duration subscribed plan greater than 12 months
        (for existing user).

        Parameters
        ----------
        username (str): the existing username
        current_plan (str): current subcribed plan (Basic, Standard, Premium)
        new_plan (str): new plan that will be chosen

        Returns
        -------
        None 
        
        """

        self.new_plan = new_plan.title()

        try:

            if self.username in data.keys():
                if self.current_plan == 'Basic':
                    if self.new_plan == 'Standard':

                        if self.duration_plan <= 12:
                             price = int(self.content_8[2].replace('Rp','').replace(',-',''))
                             print(f"Total Price: Rp {int(price)},-")

                        elif self.duration_plan > 12:
                            price = int(self.content_8[2].replace('Rp','').replace(',-','')) - User.DISCOUNT * int(self.content_8[2].replace('Rp','').replace(',-',''))
                            print(f"Total Price: Rp {int(price)},-")

                    elif self.new_plan == "Premium":

                        if self.duration_plan <= 12:
                            price = int(self.content_8[3].replace('Rp','').replace(',-',''))
                            print(f"Total Price: Rp {int(price)},-")

                        elif self.duration_plan > 12:
                            price = int(self.content_8[3].replace('Rp','').replace(',-','')) - User.DISCOUNT * int(self.content_8[3].replace('Rp','').replace(',-',''))
                            print(f"Total Price: Rp {int(price)},-")

                        elif self.new_plan == "Basic":
                            print("Your new plan is same to current plan")

                
                elif self.current_plan == "Standard":
                    if self.new_plan == "Premium":

                        if self.duration_plan <= 12:
                            price = int(self.content_8[3].replace('Rp','').replace(',-',''))
                            print(f"Total Price: Rp {int(price)},-")

                        elif self.duration_plan > 12:
                            price = int(self.content_8[3].replace('Rp','').replace(',-','')) - User.DISCOUNT * int(self.content_8[3].replace('Rp','').replace(',-',''))
                            print(f"Total Price: Rp {int(price)},-")

                    elif self.new_plan == "Standard":
                        print("Your new plan is same to current plan")

                    elif self.new_plan == "Basic":
                        print("You can upgrade plan only, try again!")

                elif self.current_plan == "Premium":
                    print("This is the latest plan")

                else:
                    print("Your plan is not found, try again!")

            else:
                print("Username is not found!")

        except:
            print("Check your input data!") 