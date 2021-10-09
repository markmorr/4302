main: main.o random_module.o matrix_module.o
	gfortran -o main main.o random_module.o matrix_module.o

random_module.o: random_module.f90
	gfortran -c random_module.f90

matrix_module.o: matrix_module.f90
	gfortran -c matrix_module.f90

main.: main.f90 random_module.0 matrix_module.o
	gfortran -c main.f90