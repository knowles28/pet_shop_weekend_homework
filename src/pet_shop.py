# WRITE YOUR FUNCTIONS HERE
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


# def get_pets_by_breed(pet_shop, breed_type):
#     breed_in_stock = []
#     for pet in pet_shop:
#         if pet == breed_type:
#             breed_in_stock.append("breed")
#     return len(breed_in_stock)

# def get_pets_by_breed(pet_shop, breed_type):
#     total_of_breed = 0
#     for pet in pet_shop["pets"]:
#         if pet == breed_type:
#             number_of_breed += 1
    
#     return int(number_of_breed)