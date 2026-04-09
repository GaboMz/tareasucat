# Practica 3: Sort: Merge Sort (Ordenamiento por Mezcla)

Tarea de la materia de Estructura de Datos. 

# Codigo para la implementacion de Merge Sort en Go


## Paso 1: Preparar el ENTORNO

Abrir la terminal y asegurarse de estar dentro de la carpeta correspondiente a esta practica:

```bash
cd P3_sort

### Cómo ejecutarlo
Abre tu terminal en esta carpeta y escribe:
```bash
go run main.go


## Paso 2: Crear el ARCHIVO FUENTE 

Crea un nuevo archivo llamado main.go


## Paso 3: CODIGO, copiar el siguiente codigo, dentro del archivo main.go : 

package main

import "fmt"

## Primero se DIVIDE la lista en mitades

### MITAD#1
func mergeSort(lista []int) []int {
    if len(lista) <= 1 {
        return lista
    }
### MITAD#2
    mitad := len(lista) / 2
    izquierda := mergeSort(lista[:mitad])
    derecha := mergeSort(lista[mitad:])
    return mezclar(izquierda, derecha)
}

## Función secundaria que MEZCLA las mitades comparando sus valores
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

## Agregar los numeros que hayan sobrado
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

## Funcion principal para agregar los numeros antes de ordenarlos 

func main() {
    numeros := []int{42, 23, 7, 4, 6, 63, 11, 15}
    fmt.Println("Lista original: ", numeros)
    
    numerosOrdenados := mergeSort(numeros)
    fmt.Println("Lista ordenada: ", numerosOrdenados)
}

# RESUMEN: El codigo almacena una lista de numeros ingresados de forma manual, los mismos mediante el mergeSort, son divididos en dos partes y luego con una funcion auxiliar los numeros son agregados de nuevo mediante un ordenamiento comparativo mediante un for y la condicional if, posteriormente se agregan mediante otros dos ciclos for los sobrantes que no pudieron ser comparados mediante el if. Con el resultado anterior la funcion main muestra la lista original "numeros" y la nueva lista "numerosOrdenados"  