all: build/libfoo.a

build:
	mkdir -p build

build/foo.o: build
	gcc -c -O2 -fPIC -o build/foo.o src/foo.c

build/libfoo.a: build/foo.o
	cd build && ar rcs libfoo.a foo.o
