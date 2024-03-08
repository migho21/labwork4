'''
 Program purpose: To analyse flower shop sales and customer satisfaction
 Developer: Muhammad Amirul Aiman Bin Muhamad Azani
 Date: 8 March 2024
'''

# Dataset
product_name = [
    "Rose", "Tulip", "Daisy", "Orchid", "Lily",
    "Sunflower", "Peony", "Lavender", "Marigold", "Carnation",
    "Chrysanthemum", "Gerbera", "Hyacinth", "Iris", "Jasmine",
    "Lilac", "Magnolia", "Narcissus", "Oleander", "Pansy"
]
unit_sold = [
    150, 200, 100, 75, 250,
    300, 50, 175, 90, 80,
    60, 220, 85, 95, 180,
    70, 55, 120, 130, 110
]
customer_reviews = [
    4.5, 3.8, 2.2, 4.0, 3.5,
    4.8, 3.0, 4.3, 3.7, 3.4,
    2.5, 4.6, 3.8, 4.1, 3.9,
    3.2, 2.9, 4.2, 3.1, 2.8
]

# Variables for calculations
total_units = sum(unit_sold)
average_review_score = sum(customer_reviews) / len(customer_reviews)
average_sales = total_units / len(unit_sold)
highest_sales = max(unit_sold)
highest_sales_index = unit_sold.index(highest_sales)
flowers_above_average_reviews = []
flowers_below_average_sales = []

# Highest Sales Identification
print(f"Highest sales flower: {product_name[highest_sales_index]} with {highest_sales} units")

# Total Units Sold Calculation
print(f"Total units sold: {total_units}")

# Average Customer Review Score Calculation
print(f"Average customer review score for all flowers: {average_review_score:.2f}")

# Above-Average Customer Reviews Identification
for i in range(len(product_name)):
    if customer_reviews[i] > average_review_score:
        flowers_above_average_reviews.append(product_name[i])

print("\nFlowers with above-average customer reviews:")
for flower in flowers_above_average_reviews:
    print(flower)

# Below-Average Sales Identification
for i in range(len(product_name)):
    if unit_sold[i] < average_sales:
        flowers_below_average_sales.append((product_name[i], unit_sold[i], customer_reviews[i]))

print("\nFlowers with below-average sales:")
for flower in flowers_below_average_sales:
    print(f"Name: {flower[0]}, Units Sold: {flower[1]}, Customer Reviews: {flower[2]}")
