# WRITE YOUR FUNCTIONS HERE
#1
def get_pet_shop_name(pet_shop):
        return pet_shop["name"]
 #2   
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#10 #11
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
       
 #4   
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash  

#5
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

#6
def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold

#7
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])
    

#8
# def get_pets_by_breed(pet_shop, breed):
#     return pet_shop["pets"]


# #9
# def get_pets_by_breed(pet_shop, breed):
#     if len("breed") == 0 
#     return pet_shop["pets"]["breed"]

#attempt 2 (9)
# def get_pets_by_breed(pet_shop, breed):
#   breed_type = 0
#   for breeds, in breed:
#       breed_type += (0)
#   return breed_type


#12
def remove_pet_by_name(pet_shop, pets):
    del pet_shop(["pets"]["name"]("Arthur"))

#13
# def add_pet_to_stock(pet_shop, new_pet):
#     new_pet["name"].append("haribo"),
#     new_pet["pet_type"].append("dog"),
#     new_pet["breed"].append("cockerspaniel"),
#     new_pet["price"].append("1500"),

#     return pet_shop["new_pet"]

#13 (attempt 2)
# def add_pet_to_stock(pet_shop, new_pet):
#     pet_shop("new_pet").append
#     return len(pet_shop["pets"])

#14            
# def add_friend(person, friend):
#     person["friends"].append("friend")

#15
# def get_customer_cash(pet_shop, cash):
#     return pet_shop[0]["cash"]
   

#16
def remove_customer_cash(pet_shop, cash):
     pet_shop["cash"] -= cash 

#17
# def get_customer_pet_count(pet_shop, customers):
#     return ["customers"]["pets"] == 0

# def add_pet_to_customer(new_pet):
#     pass
