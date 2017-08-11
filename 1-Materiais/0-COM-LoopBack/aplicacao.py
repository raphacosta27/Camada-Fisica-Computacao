#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
# Prof. Rafael Corsi
#  Abril/2017
#  Aplicação
####################################################

from enlace import *
import time

def main():
    # Inicializa enlace
    com = enlace("/dev/ttyACM0")            # Ubuntu
    #com = enlace("/dev/tty.usbmodem1411")  # Mac
    #com = enlace("COM3")                   # Windows
    com.enable()

    # Imagem a ser transmitida
    imageR = "./imgs/imageC.png"

    # Imagem a ser salva
    imageW = "./imgs/recebida.png"

    # Testa se porta foi aberta
    if not com.fisica.port is None:

        # Log
        print("-------------------------")
        print("Comunicação inicializada")
        print("  porta : {}".format(com.fisica.name))
        print("-------------------------")

        # Carrega imagem
        print ("Carregando imagem para transmissão :")
        print (" - {}".format(imageR))
        print("-------------------------")
        txBuffer = open(imageR, 'rb').read()
        txLen    = len(txBuffer)
        print(txLen)

        # Transmite imagem
        print("Transmitindo .... {} bytes".format(txLen))
        com.sendData(txBuffer)

        # espera o fim da transmissão
        while(com.tx.getIsBussy()):
            pass

        # Atualiza dados da transmissão
        txSize = com.tx.getStatus()
        print ("Transmitido       {} bytes ".format(txSize))

        # Faz a recepção dos dados
        print ("Recebendo dados .... ")
        rxBuffer, nRx = com.getData(txLen)

        # log
        print ("Lido              {} bytes ".format(nRx))

        # Salva imagem recebida em arquivo
        print("-------------------------")
        print ("Salvando dados no arquivo :")
        print (" - {}".format(imageW))
        f = open(imageW, 'wb')
        f.write(rxBuffer)

        # Fecha arquivo de imagem
        f.close()

        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com.disable()

    else:
        print("Falha ao abrir a porta")

if __name__ == "__main__":
    main()
