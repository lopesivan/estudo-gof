// BashScriptCommand implementa Command
public class BashScriptCommand implements Command {
    private String scriptPath;

    public BashScriptCommand(String scriptPath) {
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
