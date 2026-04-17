using System;
using System.Collections.Generic; 

class Program
{
    static void Main()
    {
        Stack<LlegadaF1> pilaResultados = new Stack<LlegadaF1>();

        Console.WriteLine("REGISTRANDO LLEGADAS CON PUSH");
       
        pilaResultados.Push(new LlegadaF1(1, "Max Verstappen"));
        pilaResultados.Push(new LlegadaF1(2, "Lando Norris"));
        pilaResultados.Push(new LlegadaF1(3, "Charles Leclerc"));
        pilaResultados.Push(new LlegadaF1(4, "Tsunoda"));
        Console.WriteLine("Se registraron 4 pilotos en la pila");

        Console.WriteLine("VER EL QUE ESTA ARRIBA CON PEEK");
        Console.WriteLine("El último en  ingresar es: " + pilaResultados.Peek());
        
        Console.WriteLine("SACAR DE LA PILA CON POP");
        LlegadaF1 ultimoRegistro = pilaResultados.Pop();
        Console.WriteLine("Se saco de la pila a: " + ultimoRegistro);
        Console.WriteLine("Ahora el que esta arriba es: " + pilaResultados.Peek());
    }
}

public class LlegadaF1
{
    public int Posicion { get; set; }
    public string Piloto { get; set; }

    public LlegadaF1(int posicion, string piloto)
    {
        Posicion = posicion;
        Piloto = piloto;
    }

  
    public override string ToString()
    {
        return "P" + Posicion + " - " + Piloto;
    }
}

