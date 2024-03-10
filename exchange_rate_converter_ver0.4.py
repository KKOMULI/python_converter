CNY = 184.9

input_str = input("请输入价格(元):")
input_float = float(input_str)

number = input_float * CNY

def round_to_nearest_100(number):
    return round(number / 100) * 100

rounded_num = round_to_nearest_100(number)
print(number,"원")
print("약",rounded_num,"원")