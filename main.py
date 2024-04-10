from respository.ApiConsumeRepository import  ApiconsumeRepository
from respository.procesDataRespository import ProcesdataRepository

def print_hi(name):
    apiConsume=ApiconsumeRepository()
    procesData= ProcesdataRepository()

    #busqueda=input("ingrese un numero para buscar un pokemon")


    pokemon_data = apiConsume.get_pokemon_data(int(2))
    processing_data_rquest = procesData.proces_data_one_url_full_data(pokemon_data)
    #pokemon_data = apiConsume.get_data_by_for(int(2))
    #processing_data_rquest=procesData.process_data_request(pokemon_data)






if __name__ == '__main__':
    print_hi('PyCharm')


