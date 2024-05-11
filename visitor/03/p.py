import yaml
from Cheetah.Template import Template

# Ler arquivo YAML
with open("classes.yaml", "r") as file:
    data = yaml.safe_load(file)


# Função para renderizar e salvar os templates
def render_and_save(template_file, output_file, context):
    with open(template_file, "r") as f:
        template_content = f.read()
    template = Template(template_content, searchList=[context])
    print("FILE:", output_file)
    print(str(template))


# Gerar Shape.java
render_and_save("Shape.tmpl", "Shape.java", {"className": data["shapeInterface"]})

# Gerar Circle.java, Square.java, Triangle.java, etc.
for shape in data["shapes"]:
    render_and_save(
        "ShapeClass.tmpl",
        f"{shape['name']}.java",
        {"className": shape["name"], "paramName": shape["paramName"]},
    )

# Gerar ShapeVisitor.java
render_and_save(
    "ShapeVisitor.tmpl",
    "ShapeVisitor.java",
    {"className": data["visitorInterface"], "shapes": data["shapes"]},
)

# Gerar DrawVisitor.java
render_and_save(
    "DrawVisitor.tmpl",
    "DrawVisitor.java",
    {"className": data["visitors"][0], "shapes": data["shapes"]},
)

# Gerar Main.java
render_and_save(
    "Main.tmpl", "Main.java", {"className": data["mainClass"], "shapes": data["shapes"]}
)
