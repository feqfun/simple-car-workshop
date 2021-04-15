import time


class Car:
    def __init__(self, name, surname, mark, model, registration, age=None, mileage=None, color=None):
        self.name = name
        self.surname = surname
        self.mark = mark
        self.model = model
        self.registration = registration
        self.age = age
        self.mileage = mileage
        self.color = color

    @classmethod
    def car_input(cls):
        print("INPUT CAR DATA")
        return cls(
            input("Owner's name: "),
            input("Owner's surname: "),
            input("Mark: "),
            input("Model: "),
            input("Registration number: ").upper(),
            input("Year of production (optional): "),
            input("Mileage (optional): "),
            input("Colour (optional): "))

    def show_owner(self):
        print(f"Car owner is: {self.name} {self.surname}\n")

    def show_car_info(self):
        print(
            f"Owner's name: {self.name}\nOwner's surname: {self.surname}\n"
            f"Mark: {self.mark} \nModel: {self.model} \nRegistration number: {self.registration}\n"
            f"Year of production: {self.age}\Mileage: {self.mileage}km\nColour: {self.color}\n")


# get values from dictionary for full option service
def get_all_values(dic):
    values = dic.values()
    return values


currency = "PLN"
services = {"carReview": 100,
            "timing": 150,
            "changTires": 70,
            "oil": 70,
            "filters": 90,
            "breaks": 200,
            "electronics": 70}

# boolens to controle state
doneCarReview = False
doneTiming = False
doneChangTires = False
doneOil = False
doneFilters = False
doneBreaks = False
doneElectronics = False
doneFullOption = False
payment = []
rabat = 0.9  # discount coefficient for full option service

# main menu
menu = """Choose:

1. Car review
2. Timing gear
3. Tires swap
4. Oil change
5. Replacement of filters
6. Replacement of brake pads
7. Car computer diagnostics
8. FULL SERVICE ({0}% DISCOUNT)
9. Show owner's data
10. Show car's data
11. Summary
""".format((int(100 - (rabat * 100))))

add_msg = " has been added to list of services."
already_chosen_msg = "You have already chosen "

newCar = Car.car_input()
if len(newCar.name) <= 0 or len(newCar.surname) <= 0 \
        or len(newCar.registration) <= 0 \
        or len(newCar.model) <= 0 \
        or len(newCar.mark) <= 0:
    print("Give all required parameters ")
else:
    while True:
        time.sleep(1)
        print(menu)
        try:
            command = int(input("> "))
            if command == 1:
                if doneCarReview == False and doneFullOption == False:
                    payment.append(services["carReview"])
                    doneCarReview = True
                    print("Car review" + add_msg)
                else:
                    print(already_chosen_msg + "car review.")

            elif command == 2:
                if doneTiming == False and doneFullOption == False:
                    payment.append(services["timing"])
                    doneTiming = True
                    print("Timing gear" + add_msg)
                else:
                    print(already_chosen_msg + "timing gear.")

            elif command == 3:
                if doneChangTires == False and doneFullOption == False:
                    payment.append(services["changTires"])
                    doneChangTires = True
                    print("Tires swap" + add_msg)
                else:
                    print(already_chosen_msg + "tires swap.")

            elif command == 4:
                if doneOil == False and doneFullOption == False:
                    payment.append(services["oil"])
                    doneOil = True
                    print("Oil change" + add_msg)
                else:
                    print(already_chosen_msg + "oil change.")

            elif command == 5:
                if doneFilters == False and doneFullOption == False:
                    payment.append(services["filters"])
                    doneFilters = True
                    print("Replacement of filters" + add_msg)
                else:
                    print(already_chosen_msg + "replacemetn of filters.")

            elif command == 6:
                if doneBreaks == False and doneFullOption == False:
                    payment.append(services["breaks"])
                    doneBreaks = True
                    print("Replacement of brake pads" + add_msg)
                else:
                    print(already_chosen_msg + "replacement of brake pads.")

            elif command == 7:
                if doneElectronics == False and doneFullOption == False:
                    payment.append(services["electronics"])
                    doneElectronics = True
                    print("Car computer diagnostics" + add_msg)
                else:
                    print(already_chosen_msg + "car computer diagnostics.")

            elif command == 8:
                if doneFullOption == False:
                    payment.clear()
                    payment = get_all_values(services)
                    doneFullOption = True
                    print("FULL SERVICE has been chosen")
                else:
                    print(already_chosen_msg + "FULL SERVICE")

            elif command == 9:
                newCar.show_owner()

            elif command == 10:
                newCar.show_car_info()

            elif command == 11:
                bill = sum(payment)
                newCar.show_owner()
                if doneFullOption == False:
                    print(f"TO BY PAID: {bill}{currency}")
                    break
                else:
                    rabatBill = int(rabat * bill)
                    print(
                        f"BASE PRICE {bill}{currency}\nTO BE PAID AFTER DISCOUNT:{rabatBill}{currency}")
                    break

            else:
                print("You cannot choose that.\nPlease choose another option.")

        except ValueError:
            print("Choose one of options")
