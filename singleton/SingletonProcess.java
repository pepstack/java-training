/**
 * SingletonProcess
 *
 *   $ javac SingletonProcess.java
 *   $ java SingletonProcess hello
 */
public class SingletonProcess {

    private static enum Singleton {
        INSTANCE;

        private static final SingletonProcess singleton = new SingletonProcess();

        public SingletonProcess getSingleton() {
            return singleton;
        }
    }


    private SingletonProcess() {

    }


    public static SingletonProcess getInstance() {
        return SingletonProcess.Singleton.INSTANCE.getSingleton();
    }


    public void startupService(String arg) {
        System.out.println("SingletonProcess startupService: " + arg);
    }


    /**
     * main app entry
     */
    public static void main(String args[]) throws Exception {
        SingletonProcess.getInstance().startupService(args[0]);
    }
}
