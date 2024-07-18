class ErrHan:
    def syntaxE(self):
        print("Syntax errors are caught at compile time and cannot be handled at runtime.")
        
    def nameE(self):
        try:
            print(x)
        except NameError as e:
            print(f"NameError handled: {e}")

    def typeE(self):
        try:
            result = "2" + 3
        except TypeError as e:
            print(f"TypeError handled: {e}")

    def indexE(self):
        try:
            my_list = [1, 2, 3]
            print(my_list[5])
        except IndexError as e:
            print(f"IndexError handled: {e}")

    def keyE(self):
        try:
            my_dict = {'a': 1}
            print(my_dict['b'])
        except KeyError as e:
            print(f"KeyError handled: {e}")

    def valueE(self):
        try:
            int('abc')
        except ValueError as e:
            print(f"ValueError handled: {e}")

    def zero_divisionE(self):
        try:
            result = 10 / 0
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError handled: {e}")

    def importE(self):
        try:
            import non_existent_module
        except ImportError as e:
            print(f"ImportError handled: {e}")

    def file_not_foundE(self):
        try:
            open('non_existent_file.txt')
        except FileNotFoundError as e:
            print(f"FileNotFoundError handled: {e}")

    


ehan = ErrHan()
ehan.syntaxE()
ehan.nameE()
ehan.typeE()
ehan.indexE()
ehan.keyE()
ehan.valueE()
ehan.zero_divisionE()
ehan.importE()
ehan.file_not_foundE()




