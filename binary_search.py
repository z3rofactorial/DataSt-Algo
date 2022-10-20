# we used a dictionary to pass the input for easier testing
test={
    'input':{
        'cards':[13,11,10,6,4,3,1,0],
        'query':7
    },
    'output':3
}


# in order to prepare the edge test cases, We would create a list and then add multiple test cases for us to check
test_cases = []
test_cases.append(test)

# case 1: The query is at the edges of the list.
test_cases.append({
    'input':{
        'cards':[13,11,10,2,4,3,1,7],
        'query':7
    },
    'output':7
})
# case 2: The query is in near the middle of the list.
test_cases.append({
    'input':{
        'cards':[13,11,10,2,4,3,1,7],
        'query':2
    },
    'output':3
})
# case 3: The list is empty
test_cases.append({
    'input':{
        'cards':[],
        'query':1
    },
    'output':-1
})
# case 4: The list has only one element
test_cases.append({
    'input':{
        'cards':[3],
        'query':3
    },
    'output':0
})
#case 5: The list contains repeating query elements.
test_cases.append({
    'input':{
        'cards':[13,11,10,2,4,2,1,7],
        'query':2
    },
    'output':5
})
#case 6: The list contains only same elements, it being query.
test_cases.append({
    'input':{
        'cards':[1,1,1,1,1,1,1,1],
        'query':1
    },
    'output':6
})
# case 7: The list contains only same elements, it not being query.
test_cases.append({
    'input':{
        'cards':[3,3,3,3,3,3,3,3],
        'query':2
    },
    'output':-1
})


def binary_search(cards,query):
    i=0
    while True:
        if cards[i]== query:
            return i
        i=i+1

        
# binary_search(test['input']['cards'],test['input']['query'])==test['output']
# instead of this we can use,
# binary_search(**test['input']) == test['output']

# if (binary_search(**test['input']) == test['output'])==test['output']:
#     print("yes")
# else:
#     print("NO")

result=binary_search(test['input']['cards'],test['input']['query'])
print(result)