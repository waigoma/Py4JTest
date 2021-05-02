# Py4JTest
> 自分的理解のもとに書く超雑イメージ
1. JavaでGatewayを立てる 
2. PythonでGatewayに接続する
3. Pythonで 1 をentry_pointとして設定
4. PythonでJavaで実装された機能を使える！

> コードを交えて解説 

`Main.java`
```Java
// Gatewayを立てるクラスをMainとする
public class Main {

  // Java実行時に最初に呼ばれるメソッド
  public static void main(String[] args) {
    // Mainクラスをインスタンス化
    Main app = new Main();
    
    // Gatewayを建てる準備(さっきインスタンス化したMainクラスを代入してる)
    GatewayServer server = new GatewayServer(app);
    // Gatewayを建てる！
    server.start();
    
    // わかりやすいようにコンソール出力
    System.out.println("Gateway Server Started.");
  }
  
  // 試験的にSystem.out.printlnで呼ばれたか確認するメソッドを作成
  public void println(String str) {
    System.out.prinln("System.out.println: " + str)
  }
}
```

<br>

`test.py`
```Python
import subprocess

from py4j.java_gateway import JavaGateway


# jarパスを指定して実行するコマンド文字列
# (コマンドを変えれば.classファイルでも可能)
cmd = (["java", "-jar", "jarファイルがある場所"])

# 上記コマンドをsubprocessを使って実行
subprocess.Popen(cmd)

# 実行完了(起動完了)待ち
time.sleep(3)

# Javaで建てたGatewayに接続
gateway = JavaGateway()

# Gatewayを建てる準備で代入したMainを取得
main = gateway.entry_point

# JavaのMainクラス内のprintlnを呼んでみる
main.println("PythonからJavaのメソッドを呼んでる！")

# すべての処理が終了したらGatewayを閉じる(閉じないとずっと開きっぱなしになる)
gateway.shutdown()
```

JavaはAPIみたいな感じになる(多分)。  
Pythonのコードでatexitという処理終了(exit)した時に関数を実行できる機能があるので、Gatewayを閉じるのはそれを使ったほうがいい。  
これを使うと、処理の途中でエラー落ちしてしまっても閉じることができる。

<br>

`例`
```Python
import atexit


def at_exit():
  gateway.shutdown()
  print("Gateway Server ShutDowned.)

gateway = JavaGateway()
atexit.register(at_exit)
```
