


class ServiceFactory:
    def get_service(format):
        if format == 'probabilisticMatchService':
            return ProbabilisticMatchService()
        elif format == 'productCatergoyMatchService':
            return ProductCategoryMatchService()
        else:
            raise ValueError(format)