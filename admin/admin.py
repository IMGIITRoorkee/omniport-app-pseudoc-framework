from django.contrib.admin.sites import AlreadyRegistered

from omniport.admin.site import omnipotence
from new_pseudoc.models import (
    App,
    Field,
    NumericField,
    TextField,
    Query,
    DropdownField
)

models = [
    App,
    Field,
    NumericField,
    TextField,
    Query,
    DropdownField
]

# Register all models

for model in models:
    try:
        omnipotence.register(model)
    except AlreadyRegistered:
        # A custom ModelAdmin has already registered it
        pass
