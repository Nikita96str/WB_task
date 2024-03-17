result_dict = {} # создаем пустой словарь для сохранения результатов
# Задаем количество повторов программы
t = int(input("Number of input data sets: "))
for repeat in range(t):
    # Задаём вводные данные: строку из клеток(Black or White) и количество желаемых Black клеток подряд
    print("Data set №", repeat+1)
    string = input("Enter the cell colors in the line(B or W): ").lower()
    wrong_line = True
    while wrong_line:
        for symbol in string:
            if symbol != "b" and symbol != "w":
                string = input(f"Wrong symbol in string - {symbol}. Please try again: ")
                wrong_line = True
                break
            wrong_line = False
    print(f"Your {len(string)}-character string has been accepted")
    k = int(input("Enter the desired number of consecutive black (B) cells in a row: "))


    b_list = [] # создаем пустой список для кол-ва Black в следующих k клетках
    str_index = 0 # счетчик для отсчета k клеток
    is_k = True # переменная флаг

    # Запускаем цикл, который который последовательно рассматривает каждую клетку в string,
    # пока после рассматриваемой клетки есть кол-во k клеток, включая её саму:
    while is_k:   
    # проверяем следующие k клеток
        try:
            count_b = 0 # счетчик количества Black клеток в диапазоне k
            for i in range(k):
                cur_ind = str_index + i
                if string[cur_ind] == "b": # если текущая клетка диапазона k является Black
                    count_b +=1 # в этом случае увеличиваем счетчик count_b
            b_list.append(count_b) # после того, как проверены все клетки в дипозаоне k сохраняем полученное количество count_b
    # если в диапазоне не хватает клеток до кол-ва равного k
        except:
            is_k = False # меняем значение переменной флаг и завершаем цикл
        # переходим к следующей клетке в string   
        str_index += 1 
    # после завершения цикла, сохраняем результат в result_dict
    needs_recollor = k - max(b_list)
    result_dict[string] = needs_recollor
# Выходные данные
print("Minimum number of cells that need to be repainted:")
for key in result_dict:
    print(f"In row {key}: {result_dict[key]}")

