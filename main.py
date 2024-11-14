####
import random

###
def welcome_user(): 
    print("Welcome to the Pet Care Advisor Chatbot! My name is Py.")

####
def collect_user_info():
    print("I can't wait to get to know you and your pet better!")
    name = input("What is your name? ")
    age = input("How old are you? ")
    print("Prrfect! Nice to meet you, " + name + "!")
    print("I see you are " + age + " years old.")
    return name, age

###
def collect_pet_info():
    pet_name = input("What's your pet's name? ")
    pet_type = input("What type of animal is your pet? ")
    pet_age = input("How old is your pet? ")
    print("I see your pet's name is " + pet_name + ", it is a " + pet_type + ".")
    return pet_name, pet_type 

###
def display_menu():
    print("\nHow can I help you today?")
    print("1. Set a feeding reminder")
    print("2. Get health tips for your pet")
    print("3. Get training advice")
    print("4. Find pet-friendly places to visit")
    print("5. Get a fun pet fact")
    print("6. Exit")

###
def set_feeding_reminder():
    feeding_time = input("Please enter your preferred feeding time (e.g., 07:00 AM): ")
    print(f"Feeding reminder set for {feeding_time} each day!")

####
def provide_health_tips(pet_type):
    if pet_type.lower() == "dog":
        print("Health Tips for Dogs:")
        print("- Ensure regular vet check-ups.")
        print("- Maintain a balanced diet with essential nutrients.")
        print("- Exercise regularly to keep them active.")
    elif pet_type.lower() == "cat":
        print("Health Tips for Cats:")
        print("- Provide a scratching post for exercise.")
        print("- Keep litter boxes clean to prevent illness.")
        print("- Feed a high-protein diet.")
    elif pet_type.lower() == "bird":
        print("Health Tips for Birds:")
        print("- Provide a variety of foods, including fruits and vegetables.")
        print("- Ensure the cage is cleaned regularly.")
        print("- Allow daily out-of-cage time.")
    else:
        print("General Pet Health Tips:")
        print("- Regular check-ups with a vet.")
        print("- A balanced diet tailored to your pet's needs.")

####
def provide_training_advice(pet_type):
    if pet_type.lower() == "dog":
        print("Training Tips for Dogs:")
        print("- Start with basic commands like 'sit', 'stay', and 'come'.")
        print("- Use positive reinforcement with treats.")
        print("- Keep training sessions short and fun.")
    elif pet_type.lower() == "cat":
        print("Training Tips for Cats:")
        print("- Use treats to encourage litter box use.")
        print("- Reward them for using scratching posts.")
        print("- Be patient; training cats requires consistency.")
    elif pet_type.lower() == "bird":
        print("Training Tips for Birds:")
        print("- Teach them to step onto your finger using a treat.")
        print("- Use vocal cues consistently for desired behaviors.")
        print("- Keep training sessions short.")
    else:
        print("Training tips are currently unavailable for this pet type.")

####
def find_pet_friendly_places():
    print("Pet-friendly Places in Austin, Texas:")
    print("- Zilker Park: A huge park with lots of open space, great for dogs to run around and play.")
    print("- Red Bud Isle: An off-leash dog park on a small island.")
    print("- Yard Bar: A dog-friendly bar with an off-leash dog park.")
    print("- Auditorium Shores at Town Lake: Another popular off-leash area with a great view of downtown Austin.")
    print("- Woof Gang Bakery & Grooming: A pet store with grooming and treats for pets.")
    print("- Cosmic Coffee + Beer Garden: A pet-friendly cafe with outdoor seating.")
    print("- Buzz Mill Coffee: A rustic, pet-friendly coffee shop with outdoor seating.")

####
def fun_pet_fact():
    facts = [
        "Did you know? Dogs have a sense of smell that's 40 times better than humans!",
        "Fun fact: Cats can make over 100 different sounds!",
        "Did you know? Parrots can live for over 50 years with proper care.",
        "Fun fact: A group of kittens is called a 'kindle'.",
        "Did you know? Goldfish can recognize faces!"
    ]
    print(random.choice(facts))

###
def handle_choice(choice, pet_name, pet_type):
    if choice == '1':
        set_feeding_reminder()
    elif choice == '2':
        provide_health_tips(pet_type)
    elif choice == '3':
        provide_training_advice(pet_type)
    elif choice == '4':
        find_pet_friendly_places()
    elif choice == '5':
        fun_pet_fact()
    elif choice == '6':
        confirm_exit = input("Are you sure you want to exit? (yes/no): ")
        if confirm_exit.lower() == 'yes':
            print("Goodbye! Have a great day with your pet!")
            return True
        else:
            print("Returning to the main menu.")
    else:
        print("Sorry, I didn't understand that choice. Please try again.")
    return False

####
def main():
    welcome_user()
    user_name, user_age = collect_user_info()
    pet_name, pet_type = collect_pet_info()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if handle_choice(choice, pet_name, pet_type):
            break

main()
