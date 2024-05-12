import yaml
from Cheetah.Template import Template

# Ler arquivo YAML
with open("classes.yaml", "r") as file:
    data = yaml.safe_load(file)


# Função para renderizar e salvar os templates
def render_and_save(template_file, output_file, context):
    with open(template_file, "r") as f:
        template_content = f.read()
    template = Template(template_content, searchList=[{"data": context}])
    with open(output_file, "w") as f:
        f.write(str(template))


# Gerar o arquivo para IVisitor, passando todo o contexto do YAML
render_and_save("IVisitor.tmpl", f"{data['IVisitor']}.java", data)


# Gerar Circle.java, Square.java, Triangle.java, etc.
for e in data["Element"]:
    context = {
        "IElements": data["IElements"],
        "IVisitor": data["IVisitor"],
        "classname": e["name"],
        "paramName": e["paramName"],
    }
    render_and_save("Element.tmpl", f"{e['name']}.java", context)


# Gerar o arquivo para IElements, passando todo o contexto do YAML
render_and_save("IElements.tmpl", f"{data['IElements']}.java", data)


# Gerar o arquivo para Visitor, passando todo o contexto do YAML
render_and_save("Visitor.tmpl", f"{data['Visitor']}.java", data)


# Gerar o arquivo Main, passando todo o contexto do YAML
render_and_save("Main.tmpl", f"{data['main']}.java", data)
