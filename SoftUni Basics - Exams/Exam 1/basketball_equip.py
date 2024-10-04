yearly_tax = int(input())
sneakers = yearly_tax * (1 - 0.4)
suit = sneakers * (1 - 0.2)
ball = 1/4 * suit
accessories = 1/5 * ball
total_price = yearly_tax + suit + sneakers + ball + accessories
print(f'{total_price:.2f}')
