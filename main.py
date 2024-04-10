from respository.ApiConsumeRepository import  ApiconsumeRepository
from respository.procesDataRespository import ProcesdataRepository
import random
def print_hi(name):
    apiConsume=ApiconsumeRepository()
    procesData= ProcesdataRepository()


    print("---------------------------------------------")
    print("1.-busca tu un pokemon")
    print("2.-busca un pokemon al azar")
    option=input("ingresa una de estas dos opciones")
    print(option)

    if option=="1":
        busqueda = input("ingrese un numero para buscar un pokemon")
        pokemon_data = apiConsume.get_pokemon_data(busqueda)
        processing_data_rquest = procesData.proces_data_one_url_full_data(pokemon_data)
        pokemon_data = apiConsume.get_data_by_for(busqueda)
        processing_data_rquest = procesData.process_data_request_two_urls(pokemon_data)

    elif option=="2":
        print("bucando pokemon al azar...")
        busqueda = random.randint(0, 100)

        pokemon_data = apiConsume.get_pokemon_data(busqueda)
        processing_data_rquest = procesData.proces_data_one_url_full_data(pokemon_data)

        pokemon_data = apiConsume.get_data_by_for(busqueda)
        processing_data_rquest = procesData.process_data_request_two_urls(pokemon_data)
    else:
        print("opcion no valida")



    print("---------------------------------------------")









if __name__ == '__main__':
    print_hi('PyCharm')


