# Copyright 2019 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import numpy as np

from Aiplatform.app.com.rs.services.preprocess import Preprocess


class MySimpleScaler(Preprocess):
  def __init__(self):
    self._means = None
    self._stds = None

  def preprocess(self, data):
    if self._means is None: # during training only
      self._means = np.mean(data, axis=0)

    if self._stds is None: # during training only
      self._stds = np.std(data, axis=0)
      if not self._stds.all():
        raise ValueError('At least one column has standard deviation of 0.')

    return (data - self._means) / self._stds