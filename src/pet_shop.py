# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
        return pet_shop["name"]
    
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
       
    
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash  

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])
    # for number in pet_shop:
    #     if len(number) == 0:
    #         count += 1
    #         return count

# def get_pets_by_breed(pet_shop, breed):
#     for pets_by_breed in breed:
#         total_breeds += type_of_breed[breed]
#         return (pets_by_breed)



# def get_pets_by_breed(pet_shop, breed):
#     pass

# def remove_pet_by_name(pet_shop, pets):
#     pet_shop["name"].remove("Arthur") 


def add_pet_to_stock(pet_shop, new_pet):
    new_pet["name"].append("haribo"),
    new_pet["pet_type"].append("dog"),
    new_pet["breed"].append("cockerspaniel"),
    new_pet["price"].append("1500"),

    return pet_shop["new_pet"]
            
# def add_friend(person, friend):
#     person["friends"].append("friend")

    
