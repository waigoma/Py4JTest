package waigoma;

import py4j.GatewayServer;
import waigoma.sub.Sub;

public class Main {
    private static Sub sub;

    public Sub getSub() {
        return sub;
    }

    public int mainAdd(int first, int second){
        Sub sub = new Sub();
        System.out.println("System.out.println(Main): " + first + ", " + second);
        return sub.subAdd(first, second);
    }

    public static void main(String[] args){
        Main app = new Main();
        sub = new Sub();

        GatewayServer server = new GatewayServer(app);
        server.start();
        System.out.println("Gateway Server Started.");
    }
}

/*
  sub = gateway.jvm.waigoma.sub.Sub()
  上記を呼ぶ場合
  getSub()いらない
 */
