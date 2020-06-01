# import pickle
#
# from couchbase.cluster import Cluster
#
# from Aiplatform.app.com.rs.routers.taxonomy_route import RequestItems
# from Aiplatform.app.com.rs.services.abstract_service_base import AbstractServiceBase
#
#
# class ProductTaxonomyClassification(AbstractServiceBase):
#     buck_name = "ac-bucket"
#     def __init__(self):
#         print("Product- Category MatchService Constructor ")
#         pass
#
#     def load_model(self, cluster: Cluster):
#         bucket = cluster.bucket(self.bucket_name)
#         self.coll = bucket.default_collection()
#
#         self.clf = pickle.load(open(self.get_blob_file_path() + '\\model.pickle', 'rb'))
#         self.enc = pickle.load(open(self.get_file_path() + '\\encoder.pickle', 'rb'))
#         self.features = pickle.load(open(self.get_blob_file_path() + '\\features.pickle', 'rb'))
#
#     def get_blob_file_path(self, service_name):
#         file_path = "D:\\Projects\\AiAnalyticPlatform\\Aiplatform\\app\\model"
#         return file_path
#
#     def pre_process_data(self, payload):
#         pass
#
#     def post_process_data(self, payload):
#         pass
#
#     def train(self):
#         return print("ProductCategoryMatchService Train Method")
#
#     def tune(self):
#         return print("ProductCategoryMatchService tune Method")
#
#     def score(self, payload: RequestItems):
#         # Extract model in correct order
#         data_dict = payload.dict()
#         to_predict = [data_dict[feature] for feature in features]
#
#         # Apply one-hot encoding
#         encoded_features = list(enc.transform(np.array(to_predict[-2:]).reshape(1, -1))[0])
#         to_predict = np.array(to_predict[:-2] + encoded_features)
#
#         # Create and return prediction
#         prediction = clf.predict(to_predict.reshape(1, -1))
#         return print("ProductCategoryMatchService score Method")
#
#
# class ClassificationObject:
#     model = dict()
