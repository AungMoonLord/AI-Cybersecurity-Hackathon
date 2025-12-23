from faker import Faker

num = 100000

fake = Faker()

with open("names.txt", "a", encoding="utf-8") as f:
    for i in range(num):
        print(f"Progress: {i/num*100:.03f}")
        f.write(fake.name() + "\n")
print("Finished")
