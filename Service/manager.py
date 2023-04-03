from Controleur.accueilView import AccueilView
from Controleur.session import Session

class Manager():
    def __init__(self):
        pass

    def prepare_context(self):
        session = Session()
        first_view = AccueilView(session)
        first_view.display_info()
        next_view = first_view.make_choice()
        while next_view != None :
            next_view.display_info()
            next_view = next_view.make_choice()

    def welcome(self):
        with open('assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def goodbye(self):
        with open('assets/cat.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())










