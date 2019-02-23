# -*- coding: utf-8 -*-
import re
class DesafioExtra:
    def salva_no_arquivo(self, resultado, nome_arquivo):
        nome_arquivo_saida = str(nome_arquivo.replace('in', 'out'))
        arquivo = open(nome_arquivo_saida, 'w+')
        arquivo.write(str(resultado))

    def get_numeros(self, text, nome_arquivo):
        atomos = re.sub(r'([A-Z])', r' \1', str(text))
        if ')' not in str(atomos):
            return self.salva_no_arquivo(atomos, nome_arquivo)
        elif ')' in str(atomos):
            #antes
            atomo_antes_par   = re.findall("(.*?)\s*\(", str(atomos))
            atomo_antes_par   = re.findall("[A-Za-z]+", str(atomo_antes_par))
            numero_antes_par  = re.findall("(.*?)*\(", str(atomos))
            numero_antes_par  = re.findall("[0-9]+", str(numero_antes_par))
            #dentro
            numero_dentro_par = re.findall("\((.*?)\)", str(atomos))
            numero_dentro_par = re.findall("[0-9]+", str(numero_dentro_par))
            atomo_dentro_par  = re.findall("\((.*?)\)", str(atomos))
            atomo_dentro_par  = re.findall("[A-Za-z]+", str(atomo_dentro_par))
            #depois
            numero_depois_par = re.findall("[^)]+$", str(atomos))
            numero_depois_par = re.findall("[0-9]+", str(numero_depois_par))
            atomo_depois_par  = re.findall("[^)]+$", str(atomos)) 
            atomo_depois_par  = re.findall("([A-Za-z])+", str(atomo_depois_par))
            if not numero_antes_par:
                numero_antes_par.append('1')
            if not numero_dentro_par:
                for ele in atomo_dentro_par:
                    numero_dentro_par.append('1')
            if 'n' in atomo_depois_par:
                atomo_depois_par.remove('n')
        
        elem = []
        for ele in numero_dentro_par:
            ele  = int(ele)
            ele *= int(numero_depois_par[0])
            elem.append(ele)
        
        atomo_antes_par  = zip(atomo_antes_par, numero_antes_par)
        atomo_dentro_par = zip(atomo_dentro_par, elem)
        resultado        = *atomo_antes_par, *atomo_dentro_par
        self.salva_no_arquivo(resultado, nome_arquivo)
   
    def ler_arquivo(self, nome_arquivo):
        try:
            arquivo = open(nome_arquivo , 'r')
            text = arquivo.readline()
        except FileNotFoundError:
            print('erro ao abrir o arquivo')    
        self.get_numeros(text, nome_arquivo)