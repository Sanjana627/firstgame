import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = ("Please drink water"),
        message = ("Says nutritionist Venu Adhiya Hirani, “While the general belief is to drink eight to 10 glasses of water, it is advisable to drink 12 to 15 glasses of fluids which includes water, tea, buttermilk, soup, etc. This would amount to an intake of around 2.5 litres of fluids everyday."),
        timeout = 10,
        app_icon = ("C:\\Users\\EXPERT\\Downloads\\icon.ico"),

    )
