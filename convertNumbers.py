


import sys
import os
import errno
import time
import pandas as pd


# pylint: disable=too-few-public-methods
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
                    int(wr)
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
            data = [' Posicion', 'Numero de TC'+str(i),'BIN','HEX']
            df = pd.DataFrame(columns = data)
            def decimal_to_binary(decimal):
                bin_num = []                                 # create a list
                while len(bin_num) < 32:                     # less than 32
                    if decimal != 0:
                        bin_num.append(str(decimal % 2))     # conv to binary
                        decimal = decimal // 2               # divided for two
                    else:
                        bin_num.append('0')                  # 0 incase of more than 32

                bin_num.reverse()                            # order last to first
                string = ''.join(bin_num)                    # get one string
                #print(string)
                return string
            def bin_to_hex(binary_string):
                n = sum( 2**i for i, b in enumerate(binary_string[::-1]) if b == '1' )
                #print('{:x}'.format(n))
                return '{:x}'.format(n)
            start = time.time()
            for x, cant in enumerate(data_into_list, start=1):
                #creating a list
                my_list = []
                result = decimal_to_binary(int(cant))
                result2 = bin_to_hex(result).upper()
                if len(cant) < 4:
                    binario = result[-10:]
                else:
                    binario = result
                my_list.append(str(x))
                my_list.append(str(cant))
                my_list.append(binario)
                my_list.append(result2)
                df.loc[x] = my_list
            end = time.time()
            aux = end * 1000 - start * 1000
            runingtime= runingtime+ aux
            base_filename = "ConvertionResults.txt"
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
