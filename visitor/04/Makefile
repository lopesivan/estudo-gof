

all: generate

generate:
	python gen.py
show:
	python p.py

Main.java: generate

clean:
	rm *.java *.class

test: Main.java
	java Main.java

