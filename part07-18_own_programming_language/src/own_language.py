# Write your solution here
def run(program):
  # Initialize variables A to Z
  variables = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
  output = []
  labels = {}
  pc = 0  # Program counter

  # First pass: collect all labels
  for i, line in enumerate(program):
      if '::' in line:
          label = line.split('::')[0]
          labels[label] = i
      elif ':' in line:
          label = line.split(':')[0]
          labels[label] = i

  def get_value(val):
      if val.isalpha():
          return variables[val]
      else:
          return int(val)

  # Second pass: execute the program
  while pc < len(program):
      line = program[pc]
      parts = line.split()

      if parts[0] == 'PRINT':
          output.append(get_value(parts[1]))
      elif parts[0] == 'MOV':
          variables[parts[1]] = get_value(parts[2])
      elif parts[0] == 'ADD':
          variables[parts[1]] += get_value(parts[2])
      elif parts[0] == 'SUB':
          variables[parts[1]] -= get_value(parts[2])
      elif parts[0] == 'MUL':
          variables[parts[1]] *= get_value(parts[2])
      elif parts[0] == 'JUMP':
          pc = labels[parts[1]]
          continue
      elif parts[0] == 'IF':
          left = get_value(parts[1])
          op = parts[2]
          right = get_value(parts[3])
          condition = False
          if op == '==':
              condition = left == right
          elif op == '!=':
              condition = left != right
          elif op == '<':
              condition = left < right
          elif op == '<=':
              condition = left <= right
          elif op == '>':
              condition = left > right
          elif op == '>=':
              condition = left >= right
          if condition:
              pc = labels[parts[5]]
              continue
      elif parts[0] == 'END':
          break

      pc += 1

  return output

# # Test case
# program = [
#   "MOV A 10",
#   "start:",
#   "PRINT A",
#   "SUB A 1",
#   "IF A > 0 JUMP start",
#   "END"
# ]
# print(run(program))  # Expected output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]