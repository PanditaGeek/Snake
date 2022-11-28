from pygame import mixer


#musica de fondo
mixer.music.load("nombre del archivo/ nombre de la musica.mp3")
mixer.music.play(-1) # (-1) para que se repita


#sonidos al mover al dragon

    #CODIGO DEL MOVIMIENTO HACIA ARRIBA
        Sonido_arriba = mixer.Sound("nombre del archivo/sonido_movimiento_AR.wav")
        Sonido_arriba.play()

    #CODIGO DEL MOVIMIENTO HACIA ABAJO
        Sonido_abajo = mixer.Sound("nombre del archivo/sonido_movimiento_AB.wav")
        Sonido_abajo.play()

    #CODIGO DEL MOVIMIENTO HACIA LA DERECHA
        Sonido_derecha = mixer.Sound("nombre del archivo/sonido_movimiento_DE.wav")
        Sonido_derecha.play()

    #CODIGO DEL MOVIMIENTO HACIA LA IZQUIERDA
        Sonido_izquierda = mixer.Sound("nombre del archivo/sonido_movimiento_IZ.wav")
        Sonido_izquierda.play()


#sonido al comer
sonido_comer = mixer.Sound("nombre del archivo/sonido al comer.wav")
sonido_comer.play()


#sonido al chocar
sonido_chocar = mixer.Sound("nombre del archivo/sonido al chocar.wav")
sonido_chocar.play()
