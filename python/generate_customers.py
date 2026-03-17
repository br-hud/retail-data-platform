import pandas as pd
from faker import Faker

fake = Faker()

NUM_CUSTOMERS = 10000

customers = []

for i in range(NUM_CUSTOMERS):
    customers.append({
        "customer_id": i + 1,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "signup_date": fake.date_between(start_date='-5y', end_date='today')
    })

df = pd.DataFrame(customers)

output_path = "data/sample/customers.csv"

df.to_csv(output_path, index=False)

print(f"Generated {NUM_CUSTOMERS} customers")
print(f"Saved to {output_path}")