fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
def count(fruit_name):
    count = 0
    for(fruit in fruits):
        if fruit == fruit_name:
            count +=1
    return count

count("사과")
