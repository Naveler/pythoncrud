from flask_table import Table, Col, LinkCol
 
class Results(Table):
    car_id = Col('Id', show=False)
    car_name = Col('Name')
    car_year = Col('Year')
    car_driver = Col('Driver')
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='car_id'))
    delete = LinkCol('Delete', 'delete_car', url_kwargs=dict(id='car_id'))

class DriverResults(Table):
    driver_id = Col('Id', show=False)
    driver_name = Col('Name')
    driver_lastname = Col('Lastname')
    edit = LinkCol('Edit', 'edit_driver', url_kwargs=dict(id='drivers_id'))
    delete = LinkCol('Delete', 'delete_driver', url_kwargs=dict(id='drivers_id'))
