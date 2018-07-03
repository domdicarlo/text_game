from main import Location

# Testing script for Text Adventure game

def main():
    """core testing function"""
    print('BEGIN TESTING')
    # testing length and width
    my_loc = Location('hell', 'burning', 'rot', '55-42')
    print('should print 55, enter, 42')
    print(my_loc.length)
    print(my_loc.width)

if __name__ == "__main__":
    main()
