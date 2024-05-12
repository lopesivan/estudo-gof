import yaml
from Cheetah.Template import Template

# Ler arquivo YAML
with open("c.yaml", "r") as file:
    data = yaml.safe_load(file)


# Função para renderizar e imprimir os templates
def render_and_save(template_file, output_file, context):
    with open(template_file, "r") as f:
        template_content = f.read()
    template = Template(template_content, searchList=[{"data": context}])
    # Aqui, vamos imprimir para demonstração, mas você pode querer salvar em um arquivo
    print("FILE:", output_file)
    print(str(template))


# Gerar o arquivo para IVisitor, passando todo o contexto do YAML
render_and_save("IVisitor.tmpl", f"{data['IVisitor']}.java", data)
