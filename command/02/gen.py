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

# Gerar Command interface
render_and_save("Command.tmpl", f"{data['ICommand']}.java", data)

# Gerar Command classes
for command in data["Commands"]:
    context = {
        "ICommand": data["ICommand"],
        "classname": command["name"],
        "target": command["target"],
        "action": command["action"]
    }
    render_and_save("CommandClass.tmpl", f"{command['name']}.java", context)

# Gerar Invoker class
render_and_save("Invoker.tmpl", f"{data['Invoker']}.java", data)

# Gerar Main class
render_and_save("Main.tmpl", f"{data['main']}.java", data)
