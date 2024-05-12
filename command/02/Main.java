// Classe Main para demonstrar o uso do Command
public class Main {
    public static void main(String[] args) {
        RemoteControl invoker = new RemoteControl();


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
