import traceback
from typing import List

import jsonpath_rw_ext

from Aiplatform.app.com.rs.bean import RequestItems, RequestData
from Aiplatform.app.com.rs.config.load_config import ConfigReader

from Aiplatform.app.com.rs.services.predictor import Predictor

import logging

from Aiplatform.app.com.rs.services.utils import get_class

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TenantConfigManager:
    __status = "ACTIVE"
    __model = "productTaxonomy"

    __path_pick_version: str = "tenants[?(id=$myTenant)].model[?(name=$myModel)].versions[?(id=$myVersion)]"
    __path_pick_tenant: str = "tenants[?(id=$myTenant)]"

    def __init__(self):
        pass

    def tenant(self, tenant_id: str):
        self.__tenant_id = tenant_id
        self.__tenant_info = ConfigReader.getInstance().get_tenant_config_info()
        return self

    def version(self, version: str
                ):
        self.__version = version
        return self

    def model(self, model: str):
        self.__model = model
        return self

    def given_tenant_get_model_info(self):

        if  self.__tenant_id is None:
            raise Exception("please provide Tenant Id ")

        str = self.__path_pick_tenant.replace("$myTenant", self.__tenant_id)

        model_obj: List = [match.value for match in (jsonpath_rw_ext.parse(str).find(self.__tenant_info))]

        if model_obj is None or len(model_obj) == 0:
            print(" there is no model found for this tenant ")
            raise Exception("Could not find model object or this tenant, version combination")

        model_info = dict(model_obj.__getitem__(0))
        return model_info

    def given_version_get_model_info(self):

        if self.__model is None and self.__version is None and self.__tenant_id is None:
            raise Exception("please provide Tenant Id, version Id and Model name ")

        str = self.__path_pick_version.replace("$myTenant", self.__tenant_id)\
            .replace("$myModel", self.__model).replace("$myVersion", self.__version)
        print("please provide Tenant Id, version Id and Model name ", str)

        model_obj: List = [match.value for match in (jsonpath_rw_ext.parse(str).find(self.__tenant_info))]

        if model_obj is None or len(model_obj) == 0:
            print(" there is no model found for this tenant ")
            raise Exception("Could not find model object or this tenant, version combination")

        model_info = dict(model_obj.__getitem__(0))
        return model_info

    def extract(self, item: RequestItems):

        self.__input_data = ([data.data for data in item.items])
        print("transform ---> \n", self.__input_data)
        return self

    def predict(self):
        try:
            model_info = self.given_version_get_model_info()

            predictor_class = model_info.get("class")
            model_path = model_info.get("modelPath")

            predictor_pkl = model_info.get("predictor").get("object")
            preprocess_pkl = model_info.get("preprocess").get("object")

            print(predictor_pkl, predictor_class, preprocess_pkl, model_path)

            predictor:Predictor = get_class(predictor_class).load_model_from_path(model_path)

            ls = predictor.predict(self.__input_data,probabilities=True)

            return ls
        except Exception as err:
            logger.exception(err)
            print("the code is broken ")
            traceback.print_exc()


# with open(ConfigReader.config_file_root + ConfigReader.tenant_config_json_file) as f:
#     data = json.load(f)
#
# lst_1 = [ match.value for match in (jsonpath_rw_ext.parse('tenants[?(id=1)].versions[?(status="INACTIVE")]').find(data))]
#
# lst_2 = [ match.value for match in (jsonpath_rw_ext.parse('tenants[?(id=1)].versions[?(id=="v1")]').find(data))]

# lst = [match.value for match in (parse('tenants[*]').find(data))]
# self.tenant_config_info =

# $.tenants[?(@.id==1)].versions

# $.tenants[?(@.id==1)].versions[?(@.id== 'v1')]

# instances = [
#   [6.7, 3.1, 4.7, 1.5],
#   [4.6, 3.1, 1.5, 0.2],
# ]
#
# t : Predictor= TenantConfigManager().tenant("1").version("v1").model("product_taxonomy").execute()
#
# print("--------> ",t.predict(instances))

# for i in lst_2:
#     print(i)
