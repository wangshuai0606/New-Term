GREETING = "Hello Make Variables"
TARGET = hello.txt

.PHONY: all clean

all: $(TARGET)

$(TARGET):
	echo $(GREETING) > $@

clean:
	rm -f $(TARGET)
