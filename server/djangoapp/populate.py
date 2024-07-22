from .models import CarMake, CarModel


def initiate():
    
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))


    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name":"Pathfinder", "cartype":"SUV", "year": 2023, "carmake":car_make_instances[0]},
      {"name":"Qashqai", "cartype":"SUV", "year": 2023, "carmake":car_make_instances[0]},
      {"name":"XTRAIL", "cartype":"SUV", "year": 2023, "carmake":car_make_instances[0]},
      {"name":"A-Class", "cartype":"SUV", "year": 2023, "carmake":car_make_instances[1]},
      {"name":"C-Class", "cartype":"SUV", "year": 2023, "carmake":car_make_instances[1]},
      {"name":"E-Class", "cartype":"SUV", "year": 2023, "carmake":car_make_instances[1]},
      {"name":"A4", "cartype":"SUV", "year": 2023, "carmake":car_make_instances[2]},
      {"name":"A5", "cartype":"SUV", "year": 2023, "carmake":car_make_instances[2]},
      {"name":"A6", "cartype":"SUV", "year": 2023, "carmake":car_make_instances[2]},
      {"name":"Sorrento", "cartype":"SUV", "year": 2023, "carmake":car_make_instances[3]},
      {"name":"Carnival", "cartype":"SUV", "year": 2023, "carmake":car_make_instances[3]},
      {"name":"Cerato", "cartype":"Sedan", "year": 2023, "carmake":car_make_instances[3]},
      {"name":"Corolla", "cartype":"Sedan", "year": 2023, "carmake":car_make_instances[4]},
      {"name":"Camry", "cartype":"Sedan", "year": 2023, "carmake":car_make_instances[4]},
      {"name":"Kluger", "cartype":"SUV", "year": 2023, "carmake":car_make_instances[4]},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
        
            CarModel.objects.create(name=data['name'], carmake=data['carmake'], cartype=data['cartype'], year=data['year'])
