def all_model(collection,split_method):
    find_all(collection,split_method)


def find_all(collection,split_method,recover_condition=None):
    return [make_json(model,split_method) for model in collection if recover_condition is None or recover_condition()]


def make_json(model,split_method):
    return split_method(model)