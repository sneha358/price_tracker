import argparse
from ntpath import join
arg_parser = argparse.ArgumentParser(description='Price tracker options')

arg_parser.add_argument('-a','--add', type=str, help='add a product url')
arg_parser.add_argument('-r','--rmv', type=int, help='remove a product')
arg_parser.add_argument('-l','--all', action='store_true', help='list all product')

args = arg_parser.parse_args()

DB_PATH = "db.txt"

def add_to_db(url, db):
    with open(db, "a") as f:
        f.writelines(url)

def read_from_db(db):
    results = []
    with open(db,"r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            results.append(line)
    return results        

product_url = args.add
product_id = args.rmv
product_list = args.all

# print(product_list)
# print("found ",product_url)
# print("removed ", product_id )

if(product_url):
    add_to_db([product_url+"\n"],DB_PATH)

if(product_list):
    products = read_from_db(DB_PATH)
    print("\n".join(products))