思睿是一款基于python语言的 AI web接口轻量级开发框架， 其已经集成了langchain\langgrah模型框架，flask web框架，以及postgre-sql结构化数据库服务。
目前集成的大模型包括chat-gpt， 以及deepseek。当然，由于该项目已经集成了langchain框架，因此开发者只需要通过引入langchain的对应的Model类，即可自行创建新的大模型对象。
开发者在克隆框架后，只需要在.env文件中配置对应的postgre-sql服务地址、端口、登录密码等信息，思睿框架就可以为你自动连接数据库。当然，如果你希望修改postgre的基本参数，比如连接池数量，那么你完全可以在.env文件中进行对应的配置参数修改。
思睿框架已经通过flask蓝图工具实现了全系统的web router路由注册。当开发者希望创建一个新的路由接口时，你只需要在/internal/router/router.py文件中直接通过bp对象创建一个新的路由路径，并绑定对应的接口函数即可。
与此同时，思睿框架还集成了wtf插件，以实现前端交互过程中接口参数的校验功能。还实现了自定义的Response标准化响应工具等等。更多精彩、实用的功能，等待你的开发与应用。

当你已经将该项目clone到本地，并完成环境配置后， 你只需要在项目根目录下执行：python -m app.http.app 命令就可以启动思睿项目的web服务。看到如下命令行界面，表示当前思睿服务已经启动成功。

<img width="1209" height="332" alt="image" src="https://github.com/user-attachments/assets/eb9b340d-fafb-4485-beeb-b51f1699def5" />

这时，项目应该会启动在你的127.0.0.1地址上，端口号是5000。 那么， 你就可以通过浏览器，或其他接口测试工具访问127.0.0.1:5000/ping这个地址。得到如下响应结果，就说明当前项目已经联通成功。
<img width="548" height="250" alt="image" src="https://github.com/user-attachments/assets/57af03a5-ddcc-4af7-aaf9-aa4e2ee44dc2" />
