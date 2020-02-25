class EanValidator:

    def validate(self, ean_number):
        sum = self.calculate_ean_algorithm(ean_number)
        checksum = self.calculate_checksum(sum)
        is_valid_checksum = False
        if int(ean_number[12]) == checksum:
            is_valid_checksum = True
        return is_valid_checksum

    def calculate_ean_algorithm(self, ean_number):
        number_list = list(ean_number)
        odd_sum = int(number_list[0])
        even_sum = int(number_list[1]) * 3
        counter = 2
        while counter < len(number_list) - 1:
            if counter % 2 == 0:
                odd_sum += int(number_list[counter]) * 1
            else:
                even_sum += int(number_list[counter]) * 3
            counter += 1
        return odd_sum + even_sum

    def calculate_checksum(self, sum):
        sum_module = sum % 10
        checksum = 10 - sum_module
        return checksum
