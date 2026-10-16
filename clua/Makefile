# gcc main.c -o app -llua -lraylib -lm -ldl -lpthread
#./app
# gcc test.c fun.c -o test_app -llua -lraylib -lm -ldl -lpthread
# gcc main.c fun.c -o app -llua -lraylib -lm -ldl -lpthread

# Compilador, opções de compilação, bibliotecas e nome do executável
CC = gcc
CFLAGS = -Wall -Wextra -pedantic -std=c99 -MMD -MP -g -fsanitize=address,undefined
LIBS = -lraylib -lGL -lm -lpthread -ldl -lrt -lX11 -llua -fsanitize=address,undefined 
TARGET = mamilo

# Arquivos fonte do projeto e seus objetos correspondentes
SRC = $(wildcard *.c)
OBJ = $(SRC:.c=.o)
DEP = $(SRC:.c=.d)

# Regra padrão: compila o executável final
all: $(TARGET)

# Cria o executável a partir dos arquivos objeto
$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $(TARGET) $(LIBS)

# Compila cada arquivo .c em .o usando as flags definidas
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

-include $(DEP)

# Remove arquivos de compilação gerados
clean:
	rm -f $(OBJ) $(DEP) $(TARGET)
