# Meat Market Shipping Prices
# Bryan A Quero

weight = 15 
GrndflatCharge = 20.0  # Ground flat rate

# Ground Shipping"
if weight <= 2:         
  cost_ground = weight * 1.5 + GrndflatCharge   # cost_ground is the cost of ground Shipping  
  
elif weight <= 6:
  # more calculation
  cost_ground = weight * 3.0 + GrndflatCharge                 
elif weight <= 10:
  # more calculation
  cost_ground = weight * 4.00 + GrndflatCharge
else:
  # last calculation
  cost_ground = weight * 4.75 + GrndflatCharge
print("Ground Shipping:$",cost_ground)

cost_ground_Premium = 125.00          # cost_ground_Premium is the cost of ground Shipping Premium

print("Ground Shipping Premium Cost:$", cost_ground_Premium)   # print the cost of ground Shipping Premium

# Drone Shipping                    

if weight <= 2:
  cost_drone_shipping = weight * 4.50

elif weight <= 6:
  cost_drone_shipping = weight * 9.0
elif weight <= 10:
  cost_drone_shipping = weight * 12.0
else:
  cost_drone_shipping = weight *14.25

# Drone Shipping price total
print("Drone Shipping:$",cost_ground)