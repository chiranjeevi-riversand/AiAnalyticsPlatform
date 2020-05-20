from com.rs.services.AbstractServiceBase import AbstractServiceBase


class ProductCategoryMatchService(AbstractServiceBase):

    def __init__(self):
        print("Product- Category MatchService Constructor ")
        pass

    def train(self):
        return print("ProductCategoryMatchService Train Method")

    def tune(self):
        return print("ProductCategoryMatchService tune Method")

    def score(self):
        return print("ProductCategoryMatchService score Method")