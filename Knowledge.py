def main():
    sys_check = 0

    print("Welcome. This is a database of the things I'm learning.\n ")
    
    keywords = ["atomic", "hot air", ]

    explain = ["\nAtoms are made up of protons, neutrons, and electrons. Neutrons hold protons via gravity - neutrons are the quantum of gravity.\n", "Heat, at an atomic level, is simply the 'jiggle force' of the molecule. Heat causes the atoms to move fast, causing them to jiggle and have less of a connection to the surrounding atoms. Thus, the bonds aren't as strong, making the molecule 'lighter'. Air consists of these 'light' (hot) molecules, and 'heavy' (cold) molecules. Thus, in air, the lighter and less dense molecules float to the top, meaning.... heat rises. \n",]
    
    print(f"keywords are {keywords}\n ")
    
    searching = True
    while searching:
    
        query = input("So, what do you want to remember?\n ")


        for i in range(len(keywords)):
            if query == keywords[i]:
                print(explain[i])
                quit()
                
        
        print("sorry, item not found.")
        release = input("Would you like to search for something else? (y) (n) \n")
        if release.lower == "n":
            quit()
    
        
      
    
   



if __name__ == "__main__":
    main()
