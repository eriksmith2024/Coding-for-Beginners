basket = ['Apple', 'Bun','Cola']
crate = ['Egg', 'Fig','Grape']

print('\nBasket List:', basket)
print('\nBasket Elements:', len(basket))

basket.append('Damson')
print('\nAppended:', basket)
print('\nLast Item Removed:', basket.pop())
print('\nBasket List:', basket)

basket.extend(crate)
print('\nExtended:',basket)
del basket[1]
print('\nItem Removed:', basket)
del basket[1:3]
print('\nSlice Removed:', basket, '\n')