# -*- coding: utf-8 -*-
import re
class DesafioExtra:
    
    def getNumeros(self, text):
        # indice_numero = re.search("\d+", str(text))
        # print(numero_atomos)
        atomo = re.findall("[A-Za-z]+", str(text))
        # numero_dentro_par = ''
        tem_num_in = False
        n_a = []
        elem = []
        # maiuscula = re.search('[A-Z]', str(atomos))
        # for i in range(len(atomos)):
        #     if len(atomos[i]) >= 2 and atomos[i].isupper():
        #         atomos.append(atomos[i].split(str(maiuscula)))
        atomos = re.sub(r'([A-Z])', r' \1', str(text))
        if ')' not in str(atomos):
            return print(atomos)
        elif ')' in str(atomos):
            # if re.search("^\((.*?)\)", str(atomos)) == True:
            numero_dentro_par = re.findall("\((.*?)\)", str(atomos))
            numero_dentro_par = re.findall("\d+", str(numero_dentro_par))
            atomo_dentro_par  = re.findall("\((.*?)\)", str(atomos))
            atomo_dentro_par  = re.findall("[A-Za-z]+", str(atomo_dentro_par))
            # tem_num_in = True
            numero_fora_par = re.findall("[^)]+$", str(atomos))
            numero_fora_par = re.findall("\d+", str(numero_fora_par))
            atomo_fora_par  = re.findall("(.*?)\s*\(", str(atomos))
            atomo_fora_par  = re.findall("[A-Za-z]+", str(atomo_fora_par))
            # print(numero_fora_par)
            print(numero_dentro_par)
            print(atomo_dentro_par)
            print(atomo_fora_par)
            for ele in numero_dentro_par:
                ele  = int(ele)
                ele *= int(numero_fora_par[0])
                elem.append(ele)

            atomo_dentro_par = zip(atomo_dentro_par, elem)
            list_resultado = atomo_fora_par[0], 1, *atomo_dentro_par
            print(list_resultado)    
                # print(atomo, elem)
        # if tem_num_in == True:
        # else:
        #     tamanhofinal = atomo[len(atomo)-1]
        #     firstpart, secondpart = atomo[len(atomo)-1][:len(tamanhofinal)/2], atomo[len(atomo)-1][len(tamanhofinal)/2:]
        #     return print(firstpart, secondpart)
        #     # return print(atomo, atomo[len(atomo)-1], numero_fora_par)
            # return print('lil')
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
                # n_a += ele
            # atomos = str(atomos).replace(str(numero_dentro_par), str(ele))
            # atomo = zip(atomo, ele)
            # print(atomo, ele)
        # for i in range(len(atomo)):
        #     print(atomo[i], elem[i])
        
                # print(ele)
            
            # print(atomos)
            # "([a-zA-Z0-9])"    

        # print(numero_atomos)
        # print(indice_numero)
        # print(indice_atomo)
        # self.organiza_atomos(text, numero_atomos)
        # print (text)
        # resultado = zip(atomos, numero_atomos)
        # print(*resultado)
    


    
    def ler_arquivo(self, nome_arquivo):
        try:
            arquivo = open(nome_arquivo , 'r')
            text = arquivo.read()
        except FileNotFoundError:
            print('erro ao abrir o arquivo')    
        self.getNumeros(text)