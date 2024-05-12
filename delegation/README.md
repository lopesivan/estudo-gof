Para criar um gerador de código que reproduza a estrutura e o conteúdo dos arquivos C++ fornecidos, vamos definir um `classes.yaml` para armazenar as definições e usar templates para gerar cada arquivo C++.

### Arquivo `classes.yaml`

Este arquivo define as classes e seus membros, bem como o arquivo `CMakeLists.txt`:

```yaml
project_name: delegation
compiler_flags: "-std=c++11"
source_files:
  - main.cpp
  - Shape.h
  - Rectangle.cpp
  - Rectangle.h
  - Window.cpp
  - Window.h
  - Circle.cpp
  - Circle.h
classes:
  - name: Circle
    header: Circle.h
    source: Circle.cpp
    includes:
      - Shape.h
    base_class: Shape
    properties:
      - name: radius
        type: double
    methods:
      - name: area
        return_type: double
  - name: Rectangle
    header: Rectangle.h
    source: Rectangle.cpp
    includes:
      - Shape.h
    base_class: Shape
    properties:
      - name: height
        type: double
      - name: width
        type: double
    methods:
      - name: area
        return_type: double
  - name: Window
    header: Window.h
    source: Window.cpp
    includes:
      - Shape.h
      - Rectangle.h
      - Circle.h
    properties:
      - name: shape
        type: Shape*
    methods:
      - name: area
        return_type: double
interfaces:
  - name: Shape
    header: Shape.h
    methods:
      - name: area
        return_type: double
        pure_virtual: true
main:
  file: main.cpp
  includes:
    - Window.h
```

### Templates para cada tipo de arquivo

#### Template `ClassHeader.tmpl`

```cpp
#ifndef DELEGATION_$data['name'].upper()_H
#define DELEGATION_$data['name'].upper()_H

#for $inc in $data['includes']
#include "$inc"
#end for

class $data['name']: public $data['base_class']
{
private:
#for $prop in $data['properties']
    $prop['type'] $prop['name'];
#end for

public:
#for $method in $data['methods']
    $method['return_type'] $method['name']();
#end for

    $data['name'] (#for $prop in $data['properties']$prop['type'] $prop['name']#if $prop.name != $data['properties'][-1].name#, #end if#end for);
};


#endif // DELEGATION_$data['name'].upper()_H
```

#### Template `ClassSource.tmpl`

```cpp
#include "$data['header']"

#for $method in $data['methods']
$data['return_type'] $data['name']::$method['name']()
{
    return $data['logic'];
}
#end for
```

#### Template `CMakeLists.tmpl`

```txt
cmake_minimum_required(VERSION 3.3)
project($data['project_name'])

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} $data['compiler_flags']")

set(SOURCE_FILES #for $file in $data['source_files']$file#sep, #end for)
add_executable($data['project_name'] ${SOURCE_FILES})
```

#### Template `MainSource.tmpl`

```cpp
#include <iostream>
#for $inc in $data['includes']
#include "$inc"
#end for

using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    #for $cls in $data['class_instances']
    $cls['type'] *$cls['var_name'] = new $cls['type']($cls['params']);
    cout << $cls['var_name']->area() << "\\n";
    #end for

    return 0;
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

# Exemplo de como gerar um header e source para Circle
render_and_save("ClassHeader.tmpl", f"{data['classes'][0]['name']}.h", data['classes'][0])
render_and_save("ClassSource.tmpl", f"{data['classes'][0]['name']}.cpp", data['classes'][0])
```

Este é um exemplo simplificado e genérico. Para implementar completamente este sistema, você precisaria expandir o script Python para gerar todos os arquivos com base nos dados do YAML, e possivelmente adaptar os templates para lidar com especificidades de cada classe ou método.
