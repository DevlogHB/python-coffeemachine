import data;

# 커피 머신에 재료가 있는지 확인
def resourec_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= data.resources[item]:
            print(f"Sorry there is not enuohg {item}.");
            return False;
    return True;

# 자판기에 넣은 금액
def process_wons():
    print("Please insert won.");
    total = int(input("How many won: "));
    return total;

# 반환 금액
def transcation_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = money_received - drink_cost;
        print(f"Here is {change} in change.")
        data.profit += drink_cost; #자판기 금액 업데이트
        return True;
    else:
        print(f"Sorry that's not enuough money, Money refunded.{drink_cost - money_received} won");

def make_coffee(drink_name, order_ingreduents):
    for item in order_ingreduents:
        data.resources[item] -= order_ingreduents[item];
    print(f"Here is your {drink_name}");

is_continue = True;
while is_continue:
    choice = input("What would you like? (expresso/latte/cappuccino:) ").lower();
    
    if choice == "off":
        is_continue = False;
    elif choice == "report":
        print(f"Water : {data.resources["water"]}");
        print(f"Milk  : {data.resources["milk"]}");
        print(f"Coffee: {data.resources["coffee"]}");
        print(f"Money : {data.profit}");
    else:
        if choice not in data.MENU:
          print("You entered the wrong coffee menu.");
        else:
            drink = data.MENU[choice];
            if resourec_sufficient(drink["ingredients"]):
                patment = process_wons();
                if transcation_successful(patment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"]);