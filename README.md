# 🔩Payload-Simulator

根据某张图片模拟出 TiDB 的负载，使得用 Key Visualizer 组件观测该负载时，可以呈现出该图片的图案

## 🔑Usage
利用本地 Mac 或者单机 Linux 环境快速部署 TiDB 集群。可以体验 TiDB 集群的基本架构，以及 TiDB、TiKV、PD、监控等基础组件的运行。
**在本项目目录下：**
1. 下载并安装 TiUP。

`$ curl --proto '=https' --tlsv1.2 -sSf https://tiup-mirrors.pingcap.com/install.sh | sh`

2. 声明全局环境变量。

`$ source .bash_profile`
  > 注意：TiUP 安装完成会提示对应的 profile 文件的绝对路径，source 操作需要根据实际位置进行操作。
3. 在当前 session 执行以下命令启动集群。

`$ tiup playground --db.config config.toml`

4. 通过 http://127.0.0.1:2379/dashboard 访问 TiDB 的 Dashboard 页面，默认用户名为 root，密码为空。
5. 运行脚本文件 simulator.py 或 simulator_m.py ，后者是使用多线程的版本。
6. 在 Dashboard 页面的流量可视化界面下等待至少 200 min，可看到结果。等待时间与图片的宽度有关，如果想缩短时间，可以把脚本文件中的变量 width 改为更小的数值。

## 😄Result
原图

![avatar](https://github.com/ZHANGWENTAI/Payload-Simulator/blob/master/offer.jpeg)

结果

![avatar](https://github.com/ZHANGWENTAI/Payload-Simulator/blob/master/result.png)

## 📘Reference
[使用 TiUP 部署 TiDB 集群](https://pingcap.com/docs-cn/stable/quick-start-with-tidb/#%E7%AC%AC%E4%BA%8C%E7%A7%8D%E4%BD%BF%E7%94%A8-tiup-playground-%E5%BF%AB%E9%80%9F%E9%83%A8%E7%BD%B2%E6%9C%AC%E5%9C%B0%E6%B5%8B%E8%AF%95%E7%8E%AF%E5%A2%83)

[Key Visualizer 流量可视化](https://pingcap.com/docs-cn/stable/key-visualizer-monitoring-tool/#key-visualizer-%E6%B5%81%E9%87%8F%E5%8F%AF%E8%A7%86%E5%8C%96)

[TiDB 悲观事务模型常见问题](https://pingcap.com/docs-cn/stable/pessimistic-transaction/#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)

[TiDB 配置文件样例](https://github.com/pingcap/tidb/blob/master/config/config.toml.example)
