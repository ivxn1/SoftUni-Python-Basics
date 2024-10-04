pool_volume_litres = int(input())
debit_pipe_1 = int(input())
debit_pipe_2 = int(input())
hours_no_worker = float(input())

water_from_pipe1 = debit_pipe_1 * hours_no_worker
water_from_pipe2 = debit_pipe_2 * hours_no_worker

water_from_pipes_after_Nhours = water_from_pipe2 + water_from_pipe1
if water_from_pipes_after_Nhours <= pool_volume_litres:
    print(f'The pool is{(water_from_pipes_after_Nhours / 1000) * 100: .2f}% full.'
          f' Pipe 1:{(water_from_pipe1 / water_from_pipes_after_Nhours) * 100: .2f}%. '
          f'Pipe 2:{water_from_pipe2 / water_from_pipes_after_Nhours * 100: .2f}%.')
else:
    print(f'For{hours_no_worker: .2f} hours the pool'
          f' overflows with{water_from_pipes_after_Nhours - pool_volume_litres: .2f} liters.')
