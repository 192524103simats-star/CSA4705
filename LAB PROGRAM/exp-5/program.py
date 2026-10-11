import numpy as np
usd = np.array([10, 20, 30, 40, 50])
inr = usd * 83.5
discount = inr * 0.10
final_price = inr - discount
print("USD Prices:", usd)
print("INR Prices:", inr)
print("Discount:", discount)
print("Final Prices after 10% Discount:", final_price)
expected = 0.9 * 83.5 * usd
print("Check:", np.allclose(final_price, expected))
