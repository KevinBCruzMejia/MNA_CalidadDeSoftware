


import sys
import os
import errno
import time
from collections import Counter
import pandas as pd


# pylint: disable=too-few-public-methods
# pylint: disable=C0103
# pylint: disable=W1514
# pylint: disable=R1728
# pylint: disable=R1732
# pylint: disable=W0631
# pylint: disable=C0114

try:
    # Convert the dictionary into DataFrame
    data = ["TC", "Mean", "Median", "Mode", "Variance", "STD"]
    df = pd.DataFrame(data)
    runingtime= 0
    for i, arg in enumerate(sys.argv[1:], start=1):
        mean = 0.0
        median = 0.0
        get_mode = 0.0
        variance = 0.0
        n = 0
        res = 0.0
        if len(arg) < 2:
            print("\n Error: missing argument in position:" + str(i))
            sys.exit(1)
        # print(f'Argument {i}:', arg)
        try:
            # abrimos el archivo en modo lectura.
            my_file = open(arg, "r")
            # leyendo el archivo
            data = my_file.read()
            # remplazando y dividiendo el texto
            # cuando la nueva linea ('\n') es visto
            data_into_list = data.split("\n")
            ValidFile = True
            for wr in data_into_list:
                try:
                    float(wr)
                except ValueError as e:
                    print(f"Archivo con datos invalidos parametro {i} dato {wr}")
                    ValidFile = False
                    break
            my_file.close()
        except IOError as e:
            if e.errno == errno.EACCES:
                print("Archivo existe pero no se puede acceder")
            elif e.errno == errno.ENOENT:
                print("Archivo no es leible porque no existe")
        if ValidFile:
            # print("\n Archivo valido \n")
            # Convertir float string list a float
            # Comprehension Usando float() + comprension de lista
            list_float = [float(ele) for ele in data_into_list]
            # creating a list
            my_list = []
            my_list.append("TC" + str(i))
            start = time.time()
            # Mean
            n = len(list_float)

            get_sum = sum(list_float)
            mean = get_sum / n
            mean = round(mean, 7)
            my_list.append(mean)
            # Median
            list_float.sort()
            if n % 2 == 0:
                median1 = list_float[n // 2]
                median2 = list_float[n // 2 - 1]
                median = (median1 + median2) / 2
            else:
                median = list_float[n // 2]
            my_list.append(median)
            # Mode
            data = Counter(list_float)
            get_mode = dict(data)
            mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
            if len(mode) == n:
                get_mode = "NA"
            else:
                get_mode = "[" + ", ".join(map(str, mode)) + "]"
            my_list.append(get_mode)
            # Variance and STD
            # Standard deviation of list
            # Using sum() + list comprehension
            variance = sum([((x - mean) ** 2) for x in list_float]) / len(list_float)
            variance = round(variance, 5)
            res = variance**0.5
            res = round(res, 7)
            end = time.time()
            aux = end * 1000 - start * 1000
            runingtime= runingtime+ aux
            my_list.append(variance)
            my_list.append(res)
            # Write on file
            # df.insert(i, str(i), my_list, allow_duplicates=True)
            # print(str(i))
            df.loc[:, str(i)] = my_list
    base_filename = "StatisticsResults.txt"
    dir_path = os.path.dirname(os.path.dirname(arg))
    with open(os.path.join(dir_path, base_filename), "w") as outfile:
        df.to_string(outfile, index=False, header=False)
        outfile.write("\n")
        runingtime= end * 1000 - start * 1000
        outfile.write("\n Time elapsed [ms]: " + str(runingtime))
        print(f"\n Time elapsed [ms]: {str(runingtime)} \n")
        # Neatly allocate all columns and rows to a .txt file

except (KeyboardInterrupt, EOFError) as err:
    print(err)
    print(err.args)
    sys.exit(0)
