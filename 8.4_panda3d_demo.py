# 8.4 Panda3D 三维渲染示例
try:
    from direct.showbase.ShowBase import ShowBase
except ModuleNotFoundError:
    print("❌ Panda3D 未正确安装，无法运行！")
    exit()

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.model = self.loader.loadModel("models/environment")
        self.model.reparentTo(self.render)
        self.model.setScale(0.25, 0.25, 0.25)
        self.model.setPos(-8, 42, 0)

if __name__ == "__main__":
    print("启动Panda3D窗口，关闭窗口结束程序")
    app = MyApp()
    app.run()