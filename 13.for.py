# for 迴圈

# for 變數 in 字串or列表:
#     要重複執行的程式碼

# for letter in "小白你好":
#     print(letter)
# 小
# 白
# 你
# 好

# for num in [0, 1, 2, 3, 4]:
#     print(num)
# 0
# 1
# 2
# 3
# 4

# for num in range(5):
#     print(num)
# 0
# 1
# 2
# 3
# 4

# for num in range(2, 7):
#     print(num)
# 2
# 3
# 4
# 5
# 6

def power(base_num, pow_num):
  if base_num == 0 and pow_num == 0:
    return ("未定義")
  if pow_num >= 0:
    result = 1
    for i in range(pow_num):
      result *= base_num
  else:
    result = 1
    for i in range(abs(pow_num)):
      result /= base_num
  return (result)

print(power(2, 2))
print(power(2, 0))
print(power(2, -2))
print(power(0, 0))