class Validator:
    @staticmethod
    def raise_if_len_is_len_than(obj,min_len,message):
        if len(obj) < min_len:
            raise ValueError(message)

    @staticmethod
    def raise_if_num_is_not_in_range(number,min_value,max_value,message):
        if number < min_value or number > max_value:
            raise ValueError(message)


