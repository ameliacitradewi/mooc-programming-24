# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        if not my_list:
            return None
        
        frequency = {}
        for item in my_list:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1
        
        most_common_item = None
        max_count = 0
        for item, count in frequency.items():
            if count > max_count:
                max_count = count
                most_common_item = item
        
        return most_common_item

    @classmethod
    def doubles(cls, my_list: list):
        frequency = {}
        for item in my_list:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1
        
        count_doubles = 0
        for count in frequency.values():
            if count >= 2:
                count_doubles += 1
        
        return count_doubles

# Example Usage
numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))