

class Error(Exception):
    """Classe de base pour les exceptions dans ce module."""
    @staticmethod
    def isinstance_all_class(object, *class_name):
        for class_ in class_name:
            if not isinstance(object, class_):
                raise TypeError(f"Expected {class_.__name__} but got {type(object).__name__}")
    
    