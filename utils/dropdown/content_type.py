from django.apps import apps


def get_model_names():
    all_models = apps.get_models(include_swapped=True)
    model_list = [
        {
            'displayName': f'{model._meta.app_label} | {model.__name__}', 
            'value': {
                'app': model._meta.app_label,
                'model': model._meta.model_name,
                'modelVerbose': model.__name__
            }
        }
        for model in all_models
    ]
    return model_list
