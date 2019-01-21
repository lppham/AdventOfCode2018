# COMPLETE

import re
def do_cmd(fn):
    def final(before, instr):
        after = list(before)
        after[instr[3]] = fn(before, instr[1], instr[2])
        return after
    return final

addr = do_cmd(lambda before,x,y: before[x]+before[y])
addi = do_cmd(lambda before,x,y: before[x]+y)
mulr = do_cmd(lambda before,x,y: before[x]*before[y])
muli = do_cmd(lambda before,x,y: before[x]*y)
banr = do_cmd(lambda before,x,y: before[x] & before[y])
bani = do_cmd(lambda before,x,y: before[x] & y)
borr = do_cmd(lambda before,x,y: before[x] | before[y])
bori = do_cmd(lambda before,x,y: before[x] | y)
setr = do_cmd(lambda before,x,y: before[x])
seti = do_cmd(lambda before,x,y: x)
gtir = do_cmd(lambda before,x,y: 1 if x > before[y] else 0)
gtri = do_cmd(lambda before,x,y: 1 if before[x] > y else 0)
gtrr = do_cmd(lambda before,x,y: 1 if before[x] > before[y] else 0)
eqir = do_cmd(lambda before,x,y: 1 if x == before[y] else 0)
eqri = do_cmd(lambda before,x,y: 1 if before[x] == y else 0)
eqrr = do_cmd(lambda before,x,y: 1 if before[x] == before[y] else 0)

cmds = [ addr, addi
       , mulr, muli
       , banr, bani
       , borr, bori
       , setr, seti
       , gtir, gtri, gtrr
       , eqir, eqri, eqrr
       ]
cmd_idx = {'addr': 0, 'addi': 1
          , 'mulr': 2, 'muli': 3
          , 'banr': 4, 'bani': 5
          , 'borr': 6, 'bori': 7
          , 'setr': 8, 'seti': 9
          , 'gtir': 10, 'gtri': 11, 'gtrr': 12
          , 'eqir': 13, 'eqri': 14, 'eqrr': 15
          }


program = open('input/dec21').read().strip().split('\n')
ip = int(program[0].split()[1])
program = program[1:]

registers = [0,0,0,0,0,0]
t = 0
seen = set()
prev = 0

r3 = 0
def machine(r3):
  r3 |= 65536
  r5 = 733884
  r5 = r5 + (r3 & 255)
  r5 &= 16777215
  r5 *= 65899
  r5 &= 16777215
  r5 += (r3 >> 8) & 255
  r5 &= 16777215
  r5 *= 65899
  r5 &= 16777215
  r5 += (r3 >> 16) & 255
  r5 &= 16777215
  r5 *= 65899
  r5 &= 16777215
  return r5


while True:
  r5 = machine(r3)
  if r5 in seen: 
    print r3
    break
  else:
    seen.add(r5)
  r3 = r5

exit()

while True:
    if registers[ip] < 0 or registers[ip] >= len(program):
        break


    instr, a, b, c = program[registers[ip]].split()
    
    #if instr == "eqrr":
    if registers[ip] == 28:
      #print registers[5]
      r5 = registers[5]
      if r5 in seen:
        print prev
        break
      else:
        seen.add(r5)
      prev = r5

    registers = cmds[cmd_idx[instr]](registers, [0, int(a), int(b), int(c)])
    registers[ip] += 1
    #print registers, program[registers[ip]].split()
    #t += 1
    #if t >= 30:
    #    break
print prev
print registers

#(733884 + (255 & r3)) & 16777215 * 65899 16777215