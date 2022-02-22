def string_to_modified_binary(string):
    '''Recebe uma string e retorna um binario com 9 na frente e 8 no lugar dos espacos'''
    com_espacos = (" ".join(f"{ord(i):08b}" for i in string))
    com_8_no_lugar_dos_espacos = com_espacos.replace(" ", "8")
    com_8_no_lugar_dos_espacos_com_9_na_frente = '9' + com_8_no_lugar_dos_espacos
    return com_8_no_lugar_dos_espacos_com_9_na_frente    

def modified_binary_to_string(modified_binary):
    primeira_alteracao = str(modified_binary).replace('9', '')
    binary = primeira_alteracao.replace('8', ' ')
    return ("".join([chr(int(binary, 2)) for binary in binary.split(" ")]))