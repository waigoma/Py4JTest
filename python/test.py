import atexit
import subprocess
import time

from py4j.java_gateway import JavaGateway


# 処理終了時実行関数
def at_exit():
    gateway.shutdown()
    print("Gateway Server ShutDowned.")


# jarパスを指定して実行
cmd = (["java", "-jar", "../out/artifacts/Py4JTest_jar/Py4JTest.jar"])
p = subprocess.Popen(cmd)

# サーバー起動待ち
time.sleep(3)

# JVMへ接続
gateway = JavaGateway()

# 処理終了時処理登録
atexit.register(at_exit)

# java.util.Randomインスタンスを生成
random = gateway.jvm.java.util.Random()

# Random.nextIntを呼び出し
num1 = random.nextInt(10)
num2 = random.nextInt(10)

print("print: ", num1, num2)

# Mainのインスタンス取得
main = gateway.entry_point

# MainクラスのmainAdd呼び出し
sum_num = main.mainAdd(num1, num2)

print("print: ", sum_num)

# Subクラスを取得
# sub = main.getSub()でも可
sub = gateway.jvm.waigoma.sub.Sub()

# Subクラスのprintln呼び出し
sub.println("Hello World!")
