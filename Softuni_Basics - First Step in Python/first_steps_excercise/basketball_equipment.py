yearly_tax = int(input())
sneakers = yearly_tax * (1 - 0.4)
suit = sneakers * (1 - 0.2)
ball = 0.25 * suit
accessories = 0.20 * ball
total_razhodi_za_godina = yearly_tax \
                          + sneakers \
                          + suit \
                          + ball \
                          + accessories
print(total_razhodi_za_godina)
