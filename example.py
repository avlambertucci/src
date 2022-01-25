from abc import ABC, abstractmethod
import pprint


class IMedia(ABC):
    """
    Media interface.
    """
    payload = [
        {
            "name": "bcgov",
            "location": "http://govbc.ca",
            "rating": 5
        },
        {
            "name": "albertagov",
            "location": "http://govbc.ca",
            "rating": 2
        },
        {
            "name": "promotion",
            "location": "C:/medias/pdf/promotion.pdf",
            "rating": 4
        },
        {
            "name": "flyer",
            "location": "C:/medias/pdf/flyer.pdf",
            "rating": 5
        },
    ]

    @abstractmethod
    def set_item(self, payload):
        """Set an specific item"""

    @abstractmethod
    def get_item(self, payload):
        """"Get an specific item"""

    @abstractmethod
    def play(self, payload):
        """"play an specific item"""

    @abstractmethod
    def play_by_name(self, payload):
        """"play an specific item by name"""

    @abstractmethod
    def play_by_rating(self, payload):
        """"Play an specific item by rating"""

class FileMedia(IMedia):
 
    """Set an specific item"""
    def set_item(self, payload):
        print('TESTING FILE METHODS')
        print(f"Media list: {payload}")
        #TODO set another parameter if rating is 5, create, topclass = true on file location items
        for idx, item in enumerate(payload):
            if item['rating']==5 and item['location'].startswith("C:",0,2):
                item['topclass'] = True
                
        print("Result of the list with the new toprated an item set by the most rated")
        pp.pprint(payload)

    def get_item(self, payload):
        print('TESTING FILE METHODS')
        # I will get every items that has C: and rating 5
        print(f"Media list: {payload}")
        result = ([(i) for i in payload if i['rating']>=5 and i['location'].startswith("C:",0,2)])
        print("Result of an item set by its rating")
        if not result:
            print('no data!')
            return {'msg': 'no data!'}
        else:
            print(result)

    def play(self, payload):
        print('TESTING FILE METHODS')
        print('Now playing all file items!')
        result = ([(i) for i in payload if i['location'].startswith("C:",0,2)])
        print(result)

    def play_by_name(self, payload):
        print('TESTING FILE METHODS')
        print('Now playing items from bcgov')
        result = ([(i) for i in payload if i['name']=="bcgov" and i['location'].startswith("C:",0,2)])
        print(result)

    def play_by_rating(self, payload):
        print('TESTING FILE METHODS')
        print('Now playing items from bcgov')
        result = ([(i) for i in payload if i['rating']==3 and i['location'].startswith("C:",0,2)])
        print(result)
        
class WebMedia(IMedia):
    """This WeHandler will inherance from the general media factory its methods, but it could have another factory, with especificately methods regarding web files, 
    the positive thing to use pattern factory is that you can decouple the code in blocks, due to that it's easyer to add an feature or another media type in the future
    """
    
    def set_item(self, payload):
        print('TESTING WEB METHODS')
        pass

    def get_item(self, payload):
        print('TESTING WEB METHODS')
        pass

    def play(self, payload):
        print('TESTING WEB METHODS')
        pass

    def play_by_name(self, payload):
        print('TESTING WEB METHODS')
        pass

    def play_by_rating(self, payload):
        print('TESTING WEB METHODS')
        pass
        

def read_factory()-> IMedia:
    """Constructs a factory based on the user's preference."""
    methods = {
        "get", "play", "set", "playname", "playrating"
    }
    while True:
        export_quality = input("Enter a type of file: (File or Web)")
        method = input("Which method do you wanna test? get, set, play, playname or playrating?")
        
        if method in methods:
            if export_quality.lower() == "file":
                return {"func": FileMedia(), "method":method}
                print('its a file')
            elif export_quality.lower() == "web":
                return {"func": WebMedia(), "method": method}
            # We can implement other media types here
            else:
                print(f"Error - you should choose ONE OF EACH media types (File or Web")
        else:
            print(f"Error - you should choose a CORRECT method.")
            
def main(fac: IMedia) -> None:
    """Main function."""

    method = fac.get("method")
    func = fac.get("func")
    payload = func.payload

    
    if method.lower() =='get':
        get_item = func.get_item(payload)
    elif method.lower() =='set':
        set_item = func.set_item(payload)
    elif method.lower() =='play':
        play = func.play(payload)
    elif method.lower() =='playname':
        play_by_name = func.play_by_name(payload)
    elif method.lower() =='playrating':
        play_by_rating = func.play_by_rating(payload)
    
if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    # create the factory
    factory = read_factory()

    main(factory)
    
    