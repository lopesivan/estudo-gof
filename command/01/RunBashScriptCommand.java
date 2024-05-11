public class RunBashScriptCommand implements Command
{
    private String scriptPath;

    public RunBashScriptCommand (String scriptPath)
    {
        this.scriptPath = scriptPath;
    }

    @Override
    public void execute()
    {
        try
        {
            ProcessBuilder builder = new ProcessBuilder ("/bin/bash", scriptPath);
            builder.inheritIO();
            Process process = builder.start();
            process.waitFor();
        }
        catch (Exception e)
        {
            System.out.println ("Error executing the bash script: " + e.getMessage());
        }
    }
}
