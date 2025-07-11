def demo(n):
    if n>0:
        print("This is a recursive function")
        demo(n-1)
    
demo(5)