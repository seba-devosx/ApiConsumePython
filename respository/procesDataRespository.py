
from helper.Constant import Constant
class ProcesdataRepository:

    def proces_data_one_url_full_data(self,pokemon_data):
        #ingreso el cero para poder ingresar a la primera posicion
        #obtengo el nombre
        #print(pokemon_data)
        pokemon_name=pokemon_data["forms"][0]["name"]
        quantity_of_moves_show=Constant.quantity_show_moves
        print("tu pokemon se llama",pokemon_name )
        for moves in range(min(quantity_of_moves_show,len(pokemon_data["moves"]))):
            print("sus movimiento son: ", pokemon_data["moves"][moves]["move"]["name"])



    def process_data_request_two_urls(self, pokemon_data):
            print(pokemon_data[0])
            print(pokemon_data[1])