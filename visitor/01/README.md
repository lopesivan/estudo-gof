Para ilustrar o padrão Visitor de forma simples, considere um sistema de figuras geométricas onde você deseja aplicar diferentes operações (como desenhar e calcular a área) sem alterar as classes dessas figuras. Aqui está um exemplo em Java:

```java
// Interface Visitor
public interface ShapeVisitor {
    void visit(Circle circle);
    void visit(Square square);
}

// Interface Shape
public interface Shape {
    void accept(ShapeVisitor visitor);
}

// Circle implementa Shape
public class Circle implements Shape {
    public double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public void accept(ShapeVisitor visitor) {
        visitor.visit(this);
    }
}

// Square implementa Shape
public class Square implements Shape {
    public double side;

    public Square(double side) {
        this.side = side;
    }

    @Override
    public void accept(ShapeVisitor visitor) {
        visitor.visit(this);
    }
}

// Concrete Visitor que desenha as formas
public class DrawVisitor implements ShapeVisitor {
    @Override
    public void visit(Circle circle) {
        System.out.println("Desenhando um círculo de raio " + circle.radius);
    }

    @Override
    public void visit(Square square) {
        System.out.println("Desenhando um quadrado de lado " + square.side);
    }
}

// Classe Main para demonstrar o uso do Visitor
public class Main {
    public static void main(String[] args) {
        Shape[] shapes = {new Circle(5), new Square(10)};
        DrawVisitor drawVisitor = new DrawVisitor();

        for (Shape shape : shapes) {
            shape.accept(drawVisitor);
        }
    }
}
```

Neste exemplo:
- **ShapeVisitor**: Define as operações (`visit`) para cada tipo de forma (`Circle`, `Square`).
- **Shape**: Interface comum que todas as formas implementam, permitindo a aceitação de um visitor (`accept`).
- **Circle** e **Square**: Classes concretas de formas que implementam a interface `Shape`.
- **DrawVisitor**: Um visitor concreto que implementa a lógica para desenhar cada tipo de forma.
- **Main**: Demonstra como aplicar o visitor a um array de formas.

Esse design permite que você adicione novas operações (outros visitors) sem alterar as classes das formas.
