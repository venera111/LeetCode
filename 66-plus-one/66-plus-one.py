class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        for i in range(len(digits)-1, -1, -1): #итерация по индексам с конца массива
            total = digits[i] + add #увеличиваем число на единицу
            digits[i] = total % 10 #остаток от деления на 10 записываем в виде новой цифры
            add = total // 10 #add передается в следующий цикл, если сумма больше 9
        if add: #может остаться add, если в массиве 1 элемент
            digits.insert(0, add) #добавление нулевого элемента массива со значением add
        return digits
            