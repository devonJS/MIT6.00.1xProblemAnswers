'''
Assumes each item is separated by space, returns count of salad, hamburger and water
showing up in the list of items in a string
'''

def item_order(s):
    count = {
        'salad': 0,
        'hamburger': 0,
        'water': 0
    }
    
    order_array = s.split(' ')
    
    for i in xrange(len(order_array)):
        if order_array[i] == 'salad':
            count['salad'] += 1
        elif order_array[i] == 'hamburger':
            count['hamburger'] += 1
        elif order_array[i] == 'water':
            count['water'] += 1
    
    return 'salad: ' + str(count['salad']) + ' hamburger: ' + str(count['hamburger']) + ' water: ' + str(count['water'])
    
print item_order('salad water hamburger salad hamburger')