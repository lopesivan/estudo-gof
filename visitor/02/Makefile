

all: generate

generate:
	python gen.py

Main.java: generate

clean:
	rm *.java

test: Main.java
	java Main.java

