import random
from time import time


def Burbuja(a,n):
    for i in range(1,n):
        for j in range(0,n-i):
            if(a[j] > a[j+1]):
                k = a[j+1]
                a[j+1] = a[j]
                a[j] = k;

def Insercion(a,n):
    for i in range(1,n):
        v=a[i]
        j=i-1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j=j-1
        a[j+1]=v

def Seleccion(a,n):
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if a[min] > a[j]:
                min=j
        aux=a[min]
        a[min]=a[i]
        a[i]=aux

def QuickSort(a,iz,de):
    i=iz
    j=de
    x=a[int((iz + de)/2)]
 
    while( i <= j ):
        while a[i]<x and j<=de:
            i=i+1
        while x<a[j] and j>iz:
            j=j-1
        if i<=j:
            aux = a[i]; a[i] = a[j]; a[j] = aux;
            i=i+1;  j=j-1;
 
    if iz < j:
        QuickSort( a, iz, j );
    if i < de:
        QuickSort( a, i, de );

def MergeSort(a,n):
    if n>1:
        m = n//2;
        l = a[:m]
        r = a[m:]

        MergeSort(l,len(l))
        MergeSort(r,len(r))

        i=0; j=0; k=0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                a[k]=l[i]
                i=i+1
            else:
                a[k]=r[j]
                j=j+1
            k=k+1

        while i < len(l):
            a[k]=l[i]
            i=i+1
            k=k+1

        while j < len(r):
            a[k]=r[j]
            j=j+1
            k=k+1


