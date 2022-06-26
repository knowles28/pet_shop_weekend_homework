# WRITE YOUR FUNCTIONS HERE
from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from xxlimited import new


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, new_cash):
    pet_shop["admin"]["total_cash"] += new_cash
    return pet_shop["admin"]["total_cash"]


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, new_pets):
    pet_shop["admin"]["pets_sold"] += new_pets
    return pet_shop["admin"]["pets_sold"]


def get_stock_count(number_of_pets):
    return len(number_of_pets["pets"])


def get_pets_by_breed(pet_shop, breed_type):
    requested_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_type:
            requested_breed.append(breed_type)
    return requested_breed


def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet


def remove_pet_by_name(pet_shop, pet_to_remove):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_to_remove:
            pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    
    
def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, cash_to_take):
    customer["cash"] -= cash_to_take

    
def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return len(customer["pets"])


# --- OPTIONAL ---

def customer_can_afford_pet(customer, pet_shop):
    can_afford = False
    customer_cash = customer["cash"] 
    pet_price = pet_shop["price"]
    
    for pet in pet_shop:
        if customer_cash >= pet_price:
            can_afford = True
    return can_afford


def sell_pet_to_customer()