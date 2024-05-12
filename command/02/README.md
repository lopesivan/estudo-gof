Para criar um modelo seguindo o padrão de design Command (Comando) que é agnóstico aos nomes das classes, utilizando um arquivo YAML para definir os componentes e templates para gerar o código, vamos seguir a estrutura que você forneceu. 

Aqui está o exemplo baseado no padrão Command:

### 1. Arquivo `classes.yaml`

Este arquivo contém a definição das classes, interfaces e o nome principal para o programa que demonstrará o uso do padrão Command.

```yaml
ICommand: Command
Commands:
  - name: LightOnCommand
    target: Light
    action: turnOn
  - name: LightOffCommand
    target: Light
    action: turnOff
  - name: FanOnCommand
    target: Fan
    action: turnOn
  - name: FanOffCommand
    target: Fan
    action: turnOff
Receivers:
  - Light
  - Fan
Invoker: RemoteControl
main: Main
```

### 2. Template `Command.tmpl`

Este template define a interface `Command` que todos os comandos concretos implementarão.

```text
// Interface Command
public interface $data['ICommand'] {
    void execute();
}
```

### 3. Template `CommandClass.tmpl`

Este template cria classes concretas para cada comando definido no YAML.

```text
// $data['classname'] implementa Command para o $data['target']
public class $data['classname'] implements $data['ICommand'] {
    private $data['target'] $data['target'].lower();

    public $data['classname']($data['target'] $data['target'].lower()) {
        this.$data['target'].lower() = $data['target'].lower();
    }

    @Override
    public void execute() {
        $data['target'].lower().$data['action']();
    }
}
```

### 4. Template `Invoker.tmpl`

Este template cria o `Invoker`, que chamará os comandos.

```text
// Classe $data['Invoker']
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

### 5. Template `Main.tmpl`

Este template cria a classe `Main` para demonstrar o uso dos comandos.

```text
// Classe Main para demonstrar o uso do Command
public class Main {
    public static void main(String[] args) {
        $data['Invoker'] invoker = new $data['Invoker']();
        $data['Light'] light = new $data['Light']();
        $data['Fan'] fan = new $data['Fan']();

        $data['ICommand'] lightOn = new LightOnCommand(light);
        $data['ICommand'] lightOff = new LightOffCommand(light);
        $data['ICommand'] fanOn = new FanOnCommand(fan);
        $data['ICommand'] fanOff = new FanOffCommand(fan);

        invoker.setCommand(lightOn);
        invoker.pressButton();

        invoker.setCommand(lightOff);
        invoker.pressButton();

        invoker.setCommand(fanOn);
        invoker.pressButton();

        invoker.setCommand(fanOff);
        invoker.pressButton();
    }
}
```

### 6. Script `gen.py`

Este script lê o YAML e gera os arquivos Java usando os templates.

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
        "target": command["target"],
        "action": command["action"]
    }
    render_and_save("CommandClass.tmpl", f"{command['name']}.java", context)

# Gerar Invoker class
render_and_save("Invoker.tmpl", f"{data['Invoker']}.java", data)

# Gerar Main class
render_and_save("Main.tmpl", f"{data['main']}.java", data)
```

Neste exemplo, os nomes e ações dos comandos, assim como as classes "recebedoras" dos comandos (`Light` e `Fan`), são definidos no arquivo YAML, permitindo que você ajuste ou adicione novos comandos e ações de maneira flexível sem alterar o código dos templates ou do script Python.
