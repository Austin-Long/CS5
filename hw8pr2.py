def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      count += 1
  return count

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
    total = 0
    for x in nums:
        total += x
    return (total - max(nums) - min(nums))/(len(nums) - 2)


def sum13(nums):
  if len(nums) == 0:
    return 0
  for i in range(len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if i + 1 < len(nums):
        nums[i + 1] = 0
  return sum(nums)


def sum67(nums):
  for i in range(0, len(nums)):
    if nums[i] == 6:
      nums[i] = 0
      for j in range(i+1, len(nums)):
        temp = nums[j]
        nums[j] = 0
        if temp == 7:
          i = j + 1
          break
  return sum(nums)

def has22(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False

def double_char(str):
  result = ''
  for c in str:
    result += c*2
  return result

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      count += 1
  return count

def cat_dog(str):
  dog = 0
  cat = 0
  for i in range(len(str)-2):
    if str[i:i+3] == "dog":
      dog += 1
    if str[i:i+3] == 'cat':
      cat += 1
  return cat == dog

def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
  return count

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a[-(len(b)):] == b or a == b[-(len(a)):]

def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
  if str[0:3] == 'xyz':
    return True
  return False
