def make_sandwich(*foods):
    print("\n三明治中包括：")
    for food in foods:
        print("-" + food)


make_sandwich('鸡蛋')
make_sandwich('鸡蛋', '火腿')
make_sandwich('鸡蛋', '火腿', '培根')
