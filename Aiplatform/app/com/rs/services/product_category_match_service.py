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
        # Extract model in correct order
        data_dict = data.dict()
        to_predict = [data_dict[feature] for feature in features]

        # Apply one-hot encoding
        encoded_features = list(enc.transform(np.array(to_predict[-2:]).reshape(1, -1))[0])
        to_predict = np.array(to_predict[:-2] + encoded_features)

        # Create and return prediction
        prediction = clf.predict(to_predict.reshape(1, -1))
        return print("ProductCategoryMatchService score Method")


class ClassificationObject:
    model = dict()
