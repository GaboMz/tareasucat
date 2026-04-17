package main

import "fmt"

func main() {

	var notas [5]int

	// Asignamos valores a cada posición
	notas[0] = 85
	notas[1] = 92
	notas[2] = 78
	notas[3] = 100
	notas[4] = 88

	fmt.Println("Arreglo de puntuaciones:", notas)

	colores := [3]string{"Rojo", "Verde", "Azul"}

	fmt.Println("Arreglo de colores:", colores)
}
