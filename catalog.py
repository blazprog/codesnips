# -*- coding: utf-8 -*-

class CatalogData(object):
    def __init__(self):
        self.book = Bookclass()
        
    def get_value(self, class_name_list, obj_property):
        parent = self
        try:
            for cls in class_name_list:
                parent = getattr(parent, cls)
            return getattr(parent, obj_property)
        except Exception as e:
            print e
            return ''


class Bookclass(object):
    def __init__(self):
      self.author = "Gambardella, Matthew"
      self.title = "XML Developer's Guide"
      self.genre = "Computer"
      self.price = "44.95"
      self.publish_date = "200-10-01"
      self.description = "An in-depth look at creating applications with XML"

