#include <Python.h>
#include "bubble.h"
//mozliwe sygnatury funkcji stanowiącej "interfejs" pomiędzy pythonem i C
//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){
static PyObject *mod_met(PyObject *self, PyObject *args){
	PyObject *a;
	if(!PyArg_ParseTuple(args, "O", &a)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	int r=PyList_Size(a);
	int list[r];
	for(int i=0; i<r; ++i) list[i]=PyLong_AsLong(PyList_GetItem(a, i));
	BubbleSortC(list,r);
	PyObject *pyList = PyList_New(0);
    for(int i=0;i<r;++i) PyList_Append(pyList, PyLong_FromLong(list[i]));
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("O", pyList);
}

//tablica metod
static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."}, 
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
