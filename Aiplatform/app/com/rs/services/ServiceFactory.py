from com.rs.services.ProductCategoryMatchService import ProductCategoryMatchService
from com.rs.services.ProbabilisticMatchService import ProbabilisticMatchService


class ServiceFactory:
    def get_service(format):
        if format == 'probabilisticMatchService':
            return ProbabilisticMatchService
        elif format == 'productCatergoyMatchService':
            return ProductCategoryMatchService()
        else:
            raise ValueError(format)