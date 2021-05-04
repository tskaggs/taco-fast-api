from deta import Deta  # Import Deta
import os

# Initialize with a Project Key
deta = Deta(os.environ['DETA_ACCESS_TOKEN'])


def connect_toppings():
    # This how to connect to or create a database.
    return deta.Base("taco_toppings")


def connect_tacos():
    # Initialize with a Project Key
    # deta = Deta(os.environ['DETA_ACCESS_TOKEN'])

    # This how to connect to or create a database.
    return deta.Base("taco_tacos")


def connect_user():
    # Initialize with a Project Key
    deta = Deta(os.environ['DETA_ACCESS_TOKEN'])

    # This how to connect to or create a database.
    return deta.Base("taco_user")


class DetaBase:
    pass
