airline = input()
adult_tickets = int(input())
kids_tickets = int(input())
ticket_price_adult = float(input())
service_fee = float(input())

ticket_price_kids = ticket_price_adult * 0.3

ticket_price_adult += service_fee
ticket_price_kids += service_fee

total_adult_tickets = adult_tickets * ticket_price_adult
total_kids_tickets = kids_tickets * ticket_price_kids

total_tickets_sale = total_kids_tickets + total_adult_tickets

agency_profit = 0.2 * total_tickets_sale

print(f"The profit of your agency from {airline} tickets is {agency_profit:.2f} lv.")
