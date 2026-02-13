time = input("What day of week are you watching? [weekday/weekend]: ").strip().lower()
customer_type = input("Are you a student or regular?: ").strip().lower()
show_time = int(input("Show time (8am to 1am): "))
num_of_tickets = int(input("How many tickets do you have?: "))

base_ticket_price = 300.00
base_ticket_weekends = 200.00
student_discount_rate = 0.20
time_discount_rate = 0.10
group_discount_rate = 0.05


final_price = base_ticket_price
student_discount = base_ticket_price * student_discount_rate
maritime_discount = base_ticket_price * time_discount_rate
group_discount = base_ticket_price * group_discount_rate

if customer_type == "student":
    final_price *= (1 - student_discount_rate)
elif customer_type == "regular":
    final_price == base_ticket_price

 
if 8 <= show_time < 12:
    final_price *= (1 - time_discount_rate)

# Apply group discount
if num_of_tickets > 5:
    final_price *= (1 - group_discount_rate)
total_cost = final_price * num_of_tickets
print("------MOVIE TICKET PRICE ------")
print(f"day = {time}")
print(f"Number of Tickets = {num_of_tickets}")
print(f'Base Price {base_ticket_price} x 6 = {base_ticket_price * 6}')
print(f'Student Discount = {student_discount}')
print(f'Student Discount = {(base_ticket_price * 6) * student_discount_rate}')
print(f'Maritime Discount = {maritime_discount}')
print(f'Group discount = {group_discount}')


print("------MOVIE TICKET FINAL PRICE ------")
print(f"Base Ticket Price: {base_ticket_price} x 6 = ")
print(f"Final Ticket Price (after discounts): {final_price:.2f}")
print(f"Number of Tickets: {num_of_tickets}")
print(f"Total Cost: {total_cost:.2f}")
