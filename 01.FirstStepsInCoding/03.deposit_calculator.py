deposit = float(input())
deposit_term = int(input())
annual_interest_rate = float(input())

deposit_term = deposit_term / 100
end_term_sum = deposit + deposit_term * ((deposit * annual_interest_rate) / 12)
print(end_term_sum)