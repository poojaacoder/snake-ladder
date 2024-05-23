def canPlaceFlowers() -> bool:
    flowerbed = [1,0,0,0,1,0,0]
    count = 2
    for i in range(len(flowerbed)-1):
        print("value",i, flowerbed[i])

        if i == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
            print("first")
            flowerbed[i] = 1
            count -=1
        elif flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0 :
            print("second")
            flowerbed[i] = 1
            count -=1

        print(count, flowerbed ,"count ")
        print(flowerbed)
    if count == 0:
        return True
    else:
        return False
    
print(canPlaceFlowers())
            