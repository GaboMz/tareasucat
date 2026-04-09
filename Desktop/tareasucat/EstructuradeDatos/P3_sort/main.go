package main

import "fmt"

// Primero se DIVIDE la lista en mitades

// MITAD #1
func mergeSort(lista []int) []int {
	if len(lista) <= 1 {
		return lista
	}
	// MITAD #2
	mitad := len(lista) / 2
	izquierda := mergeSort(lista[:mitad])
	derecha := mergeSort(lista[mitad:])
	return mezclar(izquierda, derecha)
}

// Función secundaria que MEZCLA las mitades comparando sus valores
func mezclar(izq []int, der []int) []int {
	resultado := []int{}
	i, j := 0, 0

	for i < len(izq) && j < len(der) {
		if izq[i] < der[j] {
			resultado = append(resultado, izq[i])
			i++
		} else {
			resultado = append(resultado, der[j])
			j++
		}
	}

	// Agregar los numeros que hayan sobrado
	for i < len(izq) {
		resultado = append(resultado, izq[i])
		i++
	}
	for j < len(der) {
		resultado = append(resultado, der[j])
		j++
	}

	return resultado
}

//Funcion principal para agregar los numeros antes de ordenarlos

func main() {
	numeros := []int{42, 23, 7, 4, 6, 63, 11, 15}
	fmt.Println("Lista original: ", numeros)

	numerosOrdenados := mergeSort(numeros)
	fmt.Println("Lista ordenada: ", numerosOrdenados)
}
