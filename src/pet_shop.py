# WRITE YOUR FUNCTIONS HERE

from os import remove


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount_add):
    pet_shop["admin"]['total_cash'] += amount_add

def add_or_remove_cash(pet_shop, amount_subtract):
    pet_shop["admin"]['total_cash'] += amount_subtract
    

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold_pet):
    pet_shop["admin"]["pets_sold"] += sold_pet

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    breed_count = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_count.append(pet["name"])
    return breed_count

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, remove_by_name):
    for pets in pet_shop["pets"]:
        if pets["name"] == remove_by_name:
            pet_shop["pets"].remove(pets)
            break

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, remove_cash):
    customers["cash"] -= remove_cash

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, add_pet):
    customers["pets"].append(add_pet)

def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet is not None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)