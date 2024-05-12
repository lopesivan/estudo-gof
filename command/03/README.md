Para criar um modelo baseado no padrão Command usando seu código como referência, vamos definir o arquivo `classes.yaml` e os templates apropriados para automatizar a geração do código de forma agnóstica, assim como você descreveu anteriormente.

### 1. Arquivo `classes.yaml`

Este arquivo YAML define os componentes essenciais para o padrão Command que você descreveu:

```yaml
ICommand: Command
Commands:
  - name: BashScriptCommand
    scriptPath: "./xpto.sh"
main: Main
```

### 2. Template `Command.tmpl`

Este template cria a interface `Command`.

```text
// Interface Command
public interface $data['ICommand'] {
    void execute();
}
```

### 3. Template `CommandClass.tmpl`

Este template gera a classe `BashScriptCommand` e outras classes de comando conforme necessário.

```text
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

### 4. Template `Main.tmpl`

Este template cria a classe `Main` que usa o comando.

```text
// Classe Main para demonstrar o uso do Command
public class $data['main'] {
    public static void main(String[] args) {
        $data['ICommand'] script = new ${data['Commands'][0]['name']}("${data['Commands'][0]['scriptPath']}");
        script.execute();
    }
}
```

### 5. Script `gen.py`

Este script Python lê o arquivo `classes.yaml` e usa os templates para gerar os arquivos `.java`.

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

# Gerar Main class
render_and_save("Main.tmpl", f"{data['main']}.java", data)
```

Neste modelo, você define todos os componentes e valores no arquivo YAML, e o script Python, juntamente com os templates, gera o código Java necessário para implementar o padrão Command de forma flexível e agnóstica.
