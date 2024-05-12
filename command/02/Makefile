

all: generate

generate:
	python gen.py

Main.java: generate

clean:
	rm *.java *.class

test: Main.java
	javac Main.java && java Main

