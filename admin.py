from omniport.admin.site import omnipotence

from new_pseudoc.models import App, Field, NumericField, TextField, Query, DropdownField

omnipotence.register(App)
omnipotence.register(Field)
omnipotence.register(NumericField)
omnipotence.register(TextField)
omnipotence.register(DropdownField)
omnipotence.register(Query)
