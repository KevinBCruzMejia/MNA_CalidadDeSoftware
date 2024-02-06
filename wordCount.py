


import sys
import os
import errno
import time
import string
import pandas as pd


# pylint: disable=too-few-public-methods
# pylint: disable=C0303
# pylint: disable=C0103
# pylint: disable=W1514
# pylint: disable=R1728
# pylint: disable=R1732
# pylint: disable=W0631
# pylint: disable=W0611
# pylint: disable=C0114
# pylint: disable=C0116
# pylint: disable=C0209
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
try:

    for i, arg in enumerate(sys.argv[1:], start=1):
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
                    str(wr)
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
            runingtime= 0
            # print("\n Archivo valido \n")
            # Convert the dictionary into DataFrame
            data = ['Row Labels', 'Count of TC'+str(i)]
            df = pd.DataFrame(columns = data)
            start = time.time()
            # Create an empty dictionary 
            d = {} 
            # Loop through each line of the file 
            for line in data_into_list: 
                # Remove the leading spaces and newline character 
                line = line.strip() 
                # Convert the characters in line to 
                # lowercase to avoid case mismatch 
                line = line.lower() 
                # Remove the punctuation marks from the line 
                line = line.translate(line.maketrans("", "", string.punctuation)) 
                # Split the line into words 
                words = line.split(" ") 
                # Iterate over each word in line 
                for word in words: 
                    # Check if the word is already in dictionary 
                    if word in d: 
                        # Increment count of word by 1 
                        d[word] = d[word] + 1
                    else: 
                        # Add the word to dictionary with count 1 
                        d[word] = 1
            x=1
            for key in list(d.keys()):
                #creating a list
                my_list = []
                my_list.append(key)
                my_list.append(d[key])
                df.loc[x] = my_list
                x=x+1
            end = time.time()
            aux = end * 1000 - start * 1000
            runingtime = runingtime + aux
            base_filename = "WordCountResults.txt"
            dir_path = os.path.dirname(os.path.dirname(arg))
            with open(os.path.join(dir_path, base_filename), "a") as outfile:
                outfile.write("\n")
                df.to_string(outfile, index=False, header=True)
                outfile.write("\n")
                #outfile.write(dfAsString)
                outfile.write("\n Time elapsed [ms]: " + str(runingtime) + "\n")
                print(f"\n Time elapsed [ms]: {str(runingtime)} \n")
                outfile.write("\n")
                # Neatly allocate all columns and rows to a .txt file

except (KeyboardInterrupt, EOFError) as err:
    print(err)
    print(err.args)
    sys.exit(0)
