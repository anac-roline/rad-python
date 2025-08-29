

# .strip() remove espaços e quebras de linha nas extremidades
nome_sujo = "  João \n"
nome_limpo = nome_sujo.strip()
print("Antes:", repr(nome_sujo), "Depois:", repr(nome_limpo))

# .split() divide a string em lista com base em um delimitador
linha = "Maria,8.5"
partes = linha.split(",")  # ["Maria", "8.5"]
print("Split:", partes)

# .join() junta itens de uma lista em uma string usando um delimitador
campos = ["a", "b", "c"]
linha_csv = "/ ".join(campos)
print("Join:", linha_csv) #"a/b/c"

# Validações simples: isalpha() e isnumeric()
print("isalpha('Maria') =>", "Maria".isalpha())
print("isnumeric('12345') =>", "12345".isnumeric())
print("isnumeric('8.5') =>", "8.5".isnumeric(), "  # Atenção: ponto decimal não é dígito puro!")