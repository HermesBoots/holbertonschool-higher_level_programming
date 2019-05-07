#include <Python.h>
#include <listobject.h>
#include <object.h>


void print_python_list_info(PyObject *p)
{
	Py_ssize_t index, length;
	PyListObject *l;
	PyObject *item;
	PyVarObject *o;

	l = (PyListObject *)p;
	o = (PyVarObject *)p;
	length = Py_SIZE(o);
	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %li\n", l->allocated);
	for (index = 0; index < length; index++)
	{
		item = PyList_GetItem(p, index);
		printf("Element %li: %s\n", index, Py_TYPE(item)->tp_name);
	}
}
