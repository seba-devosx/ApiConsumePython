from helper.Constant import Constant
import requests
import json
class ApiconsumeRepository:


    def get_pokemon_data(self,numero_busqueda):
        url_get_pokemon = Constant.get_pokemon
        new_url_get=url_get_pokemon.replace("id",str(numero_busqueda))
        request= requests.get(new_url_get)
        response=request.json()
        return response

    def get_data_by_for(self,numero_busqueda):
        poke_api_url=Constant.pk_urls
        list_poke_data=[]
        for url in poke_api_url:
            new_url_raplace_id = url.replace("id",str(numero_busqueda))
            request_url= requests.get(new_url_raplace_id)
            response=request_url.json()
            list_poke_data.append(response)
        return list_poke_data
