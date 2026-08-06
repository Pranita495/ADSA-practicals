table_size = 10
hash_table = [None] * table_size

def insert_roll(roll_number):

    index = roll_number % table_size


    while hash_table[index] is not None:
        index = (index + 1) % table_size


    hash_table[index] = roll_number
    print(f"Inserted {roll_number} at Index {index}")


insert_roll(41)
insert_roll(45) 
insert_roll(43)  
print("Final Table:", hash_table)
