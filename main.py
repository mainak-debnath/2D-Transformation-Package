from two_d_transformations import transformation

while True:
    print("Enter:\n1. Translation\n2. Scaling\n3. Rotation\n4. Shearing\n5. Reflection\n6.Exit")
    ch = int(input("Enter your choice:"))
    t = []
    v = []
    if ch == 1:
        n = int(input("Enter the number of vertices:"))
        for i in range(n):
            print("For vertex ", i + 1, ",", end="")
            x = list(map(int, input("enter x and y coordinates :").split()))
            v.append(x)
            print(v)
        trans = list(map(float, input("enter translation vectors :").split()))
        print(trans)
        transformation.translation(v, trans)
    elif ch == 2:
        n = int(input("Enter the number of vertices:"))
        for i in range(n):
            print("For vertex ", i + 1, ",", end="")
            x = list(map(int, input("enter x and y coordinates :").split()))
            v.append(x)
            print(v)
        scale = list(map(float, input("Enter scaling factors :").split()))
        print(scale)
        transformation.scaling(v, scale)
    elif ch == 3:
        n = int(input("Enter the number of vertices:"))
        angle = int(input("Enter the angle of rotation:"))
        for i in range(n):
            print("For vertex ", i + 1, " :")
            x = list(map(int, input("Enter x and y coordinates :").split()))
            v.append(x)
            print(v)
        origin = list(map(int, input("Enter x and y coordinates of origin :").split()))
        print(origin)
        print("1. Clockwise\n2. Anticlockwise")
        d = int(input("Enter your choice:"))
        if d == 1:
            transformation.rotation(v, origin, angle, cr=True)
        else:
            transformation.rotation(v, origin, angle)
    elif ch == 4:
        n = int(input("Enter the number of vertices:"))
        for i in range(n):
            print("For vertex ", i + 1, ",", end="")
            x = list(map(int, input("enter x and y coordinates :").split()))
            v.append(x)
            print(v)
        print("1. Along X-axis\n2. Along Y-axis")
        axis = int(input("Enter your choice:"))
        if axis == 1:
            shearx = int(input("Enter shearing parameter along x-direction:"))
            transformation.shearingx(v, shearx)
        else:
            sheary = int(input("Enter shearing parameter along y-direction:"))
            transformation.shearingy(v, sheary)
    elif ch == 5:
        n = int(input("Enter the number of vertices:"))
        for i in range(n):
            print("For vertex ", i + 1, ",", end="")
            x = list(map(int, input("enter x and y coordinates :").split()))
            v.append(x)
            print(v)
        print("Reflection about\n1. X-axis\n2. Y-axis\n3. Passing through Origin\n4. X=Y")
        ref = int(input("Enter your choice:"))
        if ref == 1:
            transformation.reflectionx(v)
        elif ref == 2:
            transformation.reflectiony(v)
        elif ref == 3:
            transformation.reflectionorigin(v)
        elif ref == 4:
            transformation.reflectionxy(v)
    elif ch == 6:
        break
    else:
        print("Warning : Enter a valid choice!!!")
