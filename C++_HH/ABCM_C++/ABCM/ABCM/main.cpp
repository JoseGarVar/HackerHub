//
//  main.cpp
//  ABCM
//
//  Created by José García Vargas on 01/02/12.
//  Copyright 2012 FIMEE. All rights reserved.
//

#include <iostream>
#include "Mathe.h"

int main ()
{
    int a, b,c;
    // insert code here...
    std::cout << "Hello, World!\n";
    std::cout << "Ingrese el valor de a: ";
    std::cin >> a;
    std::cout << "Ingrese el valor de b: ";
    std::cin >> b;
    
    c = Suma(a, b);
    std::cout << c;
    
    return 0;
}

