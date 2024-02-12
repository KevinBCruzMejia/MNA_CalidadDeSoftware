"""This file is to compute sales from a list of products."""
import sys
import os
import errno
import time
import json
from difflib import SequenceMatcher
import pandas as pd
# pylint: disable=too-few-public-methods


def matchmaking(a, b):
    """Allow matches titles."""
    result = SequenceMatcher(None, a, b).ratio()
    return result


def get_total_cost(product_list, sales_summary):
    """Sum all records from sales area."""
    total_amount = 0
    for record in sales_summary:
        product_name = record["Product"]
        product_lost = True
        for price_product in product_list:
            coincidence = matchmaking(product_name, price_product["title"])
            if coincidence >= 0.85:
                price = price_product["price"]
                quantity = record["Quantity"]
                total_amount += + price * quantity
                product_lost = False
                break
        if product_lost:
            print(f"Error: No se encontro el producto '{product_name}' \
            en la lista de productos")
    return total_amount


try:
    if len(sys.argv[1]) < 2:
        print("\n Error: Argumento perdido en posicion:" + str(1))
        sys.exit(1)
    with open(sys.argv[1], encoding='utf-8') as g:
        aux = json.load(g)
    data_list = aux
    try:
        str(g)
    except ValueError as e:
        print(f"Archivo con datos invalidos parametro {1} error {e}")
        VALID = False
    FILENAME = "SalesResults.txt"
    data = ['Total']
    df = pd.DataFrame(columns=data)
    for i, arg in enumerate(sys.argv[2:], start=1):
        my_list = []
        if len(arg) < 2:
            print("\n Error: Argumento perdido en posicion:" + str(i))
            sys.exit(1)
        try:
            with open(arg, encoding='utf-8') as data_into_list:
                data_sales = json.load(data_into_list)
                VALID = True
                for wr in data_into_list:
                    try:
                        int(wr)
                    except ValueError as e:
                        print(f"Archivo con datos invalidos \
                        parametro {i} dato {wr} error {e}")
                        VALID = False
                        break
        except IOError as e:
            if e.errno == errno.EACCES:
                print("Archivo existe pero no se puede acceder")
            elif e.errno == errno.ENOENT:
                print("Archivo no es leible porque no existe")
        if VALID:
            RUNINGTIME = 0
            start = time.time()
            total_cost = get_total_cost(data_list, data_sales)
            end = time.time()
            aux = end * 1000 - start * 1000
            RUNINGTIME = RUNINGTIME + aux
            OUTCOME = "TC" + str(i) + " $" + str(round(total_cost, 2))
            my_list.append(OUTCOME)
            df.loc[i] = my_list
            dir_path = os.path.dirname(os.path.dirname(arg))
    with open(os.path.join(dir_path, FILENAME),
              "w", encoding='utf-8') as outfile:
        outfile.write("\n")
        df.to_string(outfile, index=False, header=True)
        outfile.write("\n")
        outfile.write("\n Time elapsed [ms]: " + str(RUNINGTIME) + "\n")
        print(f"\n Time elapsed [ms]: {str(RUNINGTIME)} \n")
        outfile.write("\n")
except (KeyboardInterrupt, EOFError) as err:
    print(err)
    print(err.args)
    sys.exit(0)
