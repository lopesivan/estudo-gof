public class Main
{
    public static void main (String[] args)
    {
        Command runScript = new RunBashScriptCommand ("./xpto.sh");
        runScript.execute();
    }
}
