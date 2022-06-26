# WRITE YOUR FUNCTIONS HERE
from http.client import REQUESTED_RANGE_NOT_SATISFIABLE


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
    breed_number = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_type:
            breed_number.append(breed_type)
    return breed_number

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet