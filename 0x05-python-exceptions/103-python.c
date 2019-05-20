#include <Python.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <listobject.h>
#include <math.h>
#include <object.h>


/**
 * print_python_bytes - print information about Python bytes objects
 * @p: pointer to a PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, limit;
	PyBytesObject *b;
	PyVarObject *o;

	b = (PyBytesObject *)p;
	o = (PyVarObject *)p;
	puts("[.] bytes object info");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		puts("  [ERROR] Invalid Bytes Object");
		return;
	}
	printf("  size: %ld\n", o->ob_size);
	printf("  trying string: %s\n", b->ob_sval);
	limit = o->ob_size + 1 > 10 ? 10 : o->ob_size + 1;
	printf("  first %ld bytes: ", limit);
	for (i = 0; i < limit; i++)
	{
		printf("%02hx", (unsigned char)b->ob_sval[i]);
		if (i < limit - 1)
			putchar(' ');
	}
	putchar('\n');
}


/**
 * print_python_float - print information about Python float objects
 * @p: pointer to a PyFloatObject (cast as a PyObject)
 */
void print_python_float(PyObject *p)
{
	double fval;
	long ival;
	PyFloatObject *f;

	f = (PyFloatObject *)p;
	puts("[.] float object info");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		puts("  [ERROR] Invalid Float Object");
		return;
	}
	fval = f->ob_fval;
	ival = (long)fval;
	printf("  value: ");
	if (fval < 0.0)
		printf("-%li", -ival);
	else
		printf("%li", ival);
	fval -= ival;
	fval *= 1000000000000000.0;
	ival = round(fval);
	while (ival % 10 == 0 && ival != 0)
		ival /= 10;
	if (ival < 0)
		printf(".%ld\n", -ival);
	else
		printf(".%ld\n", ival);
}


/**
 * print_python_list - print information about Python list objects
 * @p: pointer to a PyListObject (cast as a PyObject)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyListObject *l;
	PyVarObject *o;

	l = (PyListObject *)p;
	o = (PyVarObject *)p;
	puts("[*] Python list info");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		puts("  [ERROR] Invalid List Object");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", o->ob_size);
	printf("[*] Allocated = %ld\n", l->allocated);
	for (i = 0; i < o->ob_size; i++)
	{
		printf("Element %ld: %s\n", i, l->ob_item[i]->ob_type->tp_name);
		if (strcmp(l->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(l->ob_item[i]);
		else if (strcmp(l->ob_item[i]->ob_type->tp_name, "float") == 0)
			print_python_float(l->ob_item[i]);
	}
}
