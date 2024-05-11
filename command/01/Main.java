public class Main
{
    public static void main (String[] args)
    {
        Command script = new BashScriptCommand ("./xpto.sh");
        script.execute();
    }
}
