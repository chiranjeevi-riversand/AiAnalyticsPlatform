

class Preprocess(object):

  def preprocess(self, data):
    """Performs custom pre processing.
    Pre process given dataset and return the processes data set.
    for Example :
    Args:
        instances: A list of prediction input instances.
        **kwargs: A dictionary of keyword args provided as additional
            fields on the predict request body.
    Returns:
        A list of outputs containing the prediction results. This list must
        be JSON serializable.
    """
    raise NotImplementedError()