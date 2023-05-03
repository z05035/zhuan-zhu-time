import time   //输入时间

work_time = 25
rest_time = 5

for i in range(4):
    # Work session
    print("Work session: {} minutes".format(work_time))
    for j in range(work_time * 60):
        time.sleep(1)
        print("\r{:2d} minutes {} seconds left".format((work_time * 60 - j) // 60, (work_time * 60 - j) % 60), end="")
    print("\nGood job! Take a rest.")
    
    # Rest session
    print("Rest session: {} minutes".format(rest_time))
    for j in range(rest_time * 60):
        time.sleep(1)
        print("\r{:2d} minutes {} seconds left".format((rest_time * 60 - j) // 60, (rest_time * 60 - j) % 60), end="")
    print("\nLet's get back to work.")
