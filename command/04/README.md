Aqui estão todos os templates e o script necessário para gerar os arquivos Java seguindo o padrão Command, baseado nas especificações fornecidas.

### Arquivo `classes.yaml`
```yaml
ICommand: Command
Commands:
  - name: BashScriptCommand
    scriptPath: "./xpto.sh"
Invoker: RemoteControl
main: Main
```

### Template `Command.tmpl`
```java
// Interface Command
public interface $data['ICommand'] {
    void execute();
}
```

### Template `CommandClass.tmpl`
```java
// $data['classname'] implementa Command
public class $data['classname'] implements $data['ICommand'] {
    private String scriptPath;

    public $data['classname'](String scriptPath) {
        this.scriptPath = scriptPath;
    }

    @Override
    public void execute() {
        try {
            ProcessBuilder builder = new ProcessBuilder("/bin/bash", this.scriptPath);
            builder.inheritIO();
            Process process = builder.start();
            process.waitFor();
        } catch (Exception e) {
            System.out.println("Error executing the bash script: " + e.getMessage());
        }
    }
}
```

### Template `Invoker.tmpl`
```java
// Classe Invoker
public class $data['Invoker'] {
    private $data['ICommand'] command;

    public void setCommand($data['ICommand'] command) {
        this.command = command;
    }

    public void pressButton() {
        command.execute();
    }
}
```

### Template `Main.tmpl`
```java
// Classe Main para demonstrar o uso do Command
public class Main {
    public static void main(String[] args) {
        $data['ICommand'] script = new ${data['Commands'][0]['name']}("${data['Commands'][0]['scriptPath']}");
        $data['Invoker'] remote = new $data['Invoker']();
        remote.setCommand(script);
        remote.pressButton();
    }
}
```

### Script Python `gen.py`
```python
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
        "scriptPath": command["scriptPath"]
    }
    render_and_save("CommandClass.tmpl", f"{command['name']}.java", context)

# Gerar Invoker class
render_and_save("Invoker.tmpl", f"{data['Invoker']}.java", data)

# Gerar Main class
render_and_save("Main.tmpl", f"{data['main']}.java", data)
```

Estes são os templates e o script Python necessários para automatizar a geração de código no padrão Command conforme descrito.
