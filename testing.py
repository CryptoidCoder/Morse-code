char = getch()
     if (char == "q"):
        StopMotors()
        exit(0)  
    
    
    elif (char == "s"):
        print 'Down pressed'      
        Backwards()
        time.sleep(button_delay)  
